import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
import numpy as np

from .debiasing import get_alpha

class adversary(nn.Module):

    def __init__(self, n_sensitive, n_hidden=32):
        super(adversary, self).__init__()
        self.network = nn.Sequential(
            nn.Linear(2, n_hidden),
            nn.ReLU(),
            nn.Linear(n_hidden, n_hidden),
            nn.ReLU(),
            nn.Linear(n_hidden, n_hidden),
            nn.ReLU(),
            nn.Linear(n_hidden, n_sensitive),
        )

    def forward(self, x):
        return torch.sigmoid(self.network(x))

class debiasing:
    def __init__(self, dset, attrib, alpha=None):
        from . import predictors
        self.predictor = predictors.get_pytorch(dset)()
        self.predictor_optimizer = optim.Adam(self.predictor.parameters())
        self.predictor_criterion = nn.CrossEntropyLoss()
        self.adversary = adversary(2)
        self.adversary_optimizer = optim.Adam(self.adversary.parameters())
        self.adversary_criterion = nn.CrossEntropyLoss()
        if alpha==None:
            alpha_in_use = get_alpha(dset,attrib)
        else:
            alpha_in_use = alpha

    def fit(self, x,y,z):
        #GPU
        use_cuda = torch.cuda.is_available()
        use_mps = torch.backends.mps.is_available()


        if use_cuda:
            device = torch.device("cuda")
        elif use_mps:
            device = torch.device("mps")
        else:
            device = torch.device("cpu")

        train_kwargs = {'batch_size': self.predictor.config["bs"]}
        if use_cuda:
            cuda_kwargs = {'num_workers': 1,
                           'pin_memory': True,
                           'shuffle': True}
            train_kwargs.update(cuda_kwargs)

        #Data
        from .fairgrad import LFWdset
        dataset = LFWdset(x,y,z)
        data_loader = torch.utils.data.DataLoader(dataset, **train_kwargs)
        lambdas = torch.Tensor([130, 30])

        #Pretrain predictor model 
        for epoch in range(2):
            for x, y, _ in data_loader:
                self.predictor.zero_grad()
                p_y = self.predictor(x)
                loss = self.predictor_criterion(p_y, y.long())
                loss.backward()
                self.predictor_optimizer.step()

        #Pretrain adversary model 
        for epoch in range(5):
            for x, _, z in data_loader:
                p_y = self.predictor(x).detach()
                self.adversary.zero_grad()
                p_z = self.adversary(p_y)
                loss = (self.adversary_criterion(p_z, z.long()) * lambdas).mean()
                loss.backward()
                self.adversary_optimizer.step()


        #Train both in adversarial setting
        for epoch in range(self.predictor.config["epoch"]):
            # Train adversary
            for x, y, z in data_loader:
                p_y = self.predictor(x)
                self.adversary.zero_grad()
                p_z = self.adversary(p_y)
                loss_adv = (self.adversary_criterion(p_z, z.long()) * lambdas).mean()
                loss_adv.backward()
                self.adversary_optimizer.step()

            # Train classifier on single batch
            for x, y, z in data_loader:
                pass
            p_y = self.predictor(x)
            p_z = self.adversary(p_y)
            self.predictor.zero_grad()
            p_z = self.adversary(p_y)
            loss_adv = (self.adversary_criterion(p_z, z.long()) * lambdas).mean()
            clf_loss = self.predictor_criterion(p_y, y.long()) - (self.adversary_criterion(self.adversary(p_y), z.long()) * lambdas).mean()
            clf_loss.backward()
            self.predictor_optimizer.step()

    def predict_proba(self, x):
        #GPU
        use_cuda = torch.cuda.is_available()
        use_mps = torch.backends.mps.is_available()

        #torch.manual_seed(args.seed)

        if use_cuda:
            device = torch.device("cuda")
        elif use_mps:
            device = torch.device("mps")
        else:
            device = torch.device("cpu")

        x = torch.from_numpy(x).float()
        x = x.to(device)

        with torch.no_grad():
            predictions = self.predictor(x).cpu().detach().numpy()

        return predictions

    def predict(self, x):
        prediction = self.predict_proba(x)
        yhat = np.argmax(prediction, axis=1)
        return yhat



