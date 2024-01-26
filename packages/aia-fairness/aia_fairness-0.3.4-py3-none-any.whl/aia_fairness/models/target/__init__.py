import numpy as np
from fairlearn.reductions import DemographicParity 
from fairlearn.reductions import ExponentiatedGradient
from sklearn.ensemble import RandomForestClassifier
import pickle
from pathlib import Path

from . import fairgrad
from .import debiasing
from .import debiasing_custom
from .. import BaseClassifier
from .. import config as config

class RandomForest(BaseClassifier):
    def __init__(self, dset=None,attrib=None):
        super().__init__(dset)
        self.model = RandomForestClassifier(random_state=config.random_state)

    def fit(self,x,y):
        self.model.fit(x,y)

    def predict_proba(self,x):
        return self.model.predict_proba(x)[:,0]

    def predict(self,x):
        return self.model.predict(x)

class NeuralNetwork(BaseClassifier):
    def __init__(self,dset=None,attrib=None):
        super().__init__(dset)

    def fit(self,x,y):
        input_size = np.shape(x)[1]
        self.model = fairgrad.target_model(self.dset)
        self.model.set_fair(False)
        self.model.fit(x,y)

    def predict_proba(self,x):
        return self.model.predict_proba(x)[:,0]

    def predict(self,x):
        return self.model.predict(x)

class NeuralNetwork_Fairgrad(NeuralNetwork):
    def __init__(self, dset=None,attrib=None):
        super().__init__(dset)
        self.need_z = True

    def fit(self,x,y,z):
        input_size = np.shape(x)[1]
        self.model = fairgrad.target_model(self.dset)
        self.model.set_fair(True)
        self.model.fit(x,y.astype(int),z=z.astype(int))

class NeuralNetwork_AdversarialDebiasing(BaseClassifier):
    def __init__(self, dset=None,attrib=None,alpha=None):
        super().__init__(dset,attrib)
        self.need_z = True
        self.alpha=alpha

    def fit(self,x,y,z):
        input_size = np.shape(x)[1]
        self.model = debiasing.debiasing(dset=self.dset,attrib=self.attrib,alpha=self.alpha)
        self.model.fit(x,y,z)

    def predict_proba(self,x):
        return self.model.predict_proba(x)

    def predict(self, x):
        return self.model.predict(x)

class NeuralNetwork_AdversarialDebiasing_Custom(BaseClassifier):
    def __init__(self, dset=None,attrib=None,alpha=None):
        super().__init__(dset,attrib)
        self.need_z = True
        self.alpha=alpha

    def fit(self,x,y,z):
        input_size = np.shape(x)[1]
        self.model = debiasing_custom.debiasing(dset=self.dset,attrib=self.attrib,alpha=self.alpha)
        self.model.fit(x,y,z)

    def predict_proba(self,x):
        return self.model.predict_proba(x)[:,0]

    def predict(self, x):
        return self.model.predict(x)
        
class RandomForest_EGD(RandomForest):
    def __init__(self,dset=None,attrib=None):
        super().__init__(dset)
        constraint = DemographicParity()
        self.model = ExponentiatedGradient(self.model, constraint)
        self.need_z = True

    def fit(self,x,y,z):
        self.model.fit(x,y,sensitive_features=z)

    def predict_proba(self,x):
        return self.model._pmf_predict(x)[:,0]

class NeuralNetwork_EGD(NeuralNetwork):
    def __init__(self, dset=None,attrib=None):
        super().__init__(dset)
        self.need_z = True

    def fit(self,x,y,z):
        input_size = np.shape(x)[1]
        model = fairgrad.target_model(self.dset)
        constraint = DemographicParity()
        model.set_fair(False)
        model.set_sample_weight(True)
        self.model = ExponentiatedGradient(model, constraint)
        self.model.fit(x,y,sensitive_features=z)

    def predict_proba(self,x):
        return self.model._pmf_predict(x)[:,0]

class Dry1(BaseClassifier):
    def __init__(self,dset=None,attrib=None):
        super().__init__(dset)

class Dry2(BaseClassifier):
    def __init__(self,dset=None,attrib=None):
        super().__init__(dset)
        self.need_z = True

    def fit(self, x,y,z):
        pass
