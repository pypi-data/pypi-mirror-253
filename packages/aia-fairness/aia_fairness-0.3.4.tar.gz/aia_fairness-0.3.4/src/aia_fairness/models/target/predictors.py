import torch.nn as nn
import torch.nn.functional as F
import silence_tensorflow.auto
import tensorflow as tf


def get_pytorch(dset):
    """Bridges the name (str) of the dataset with the specific prodictor class"""
    if dset=="LAW":
        return LAW
    elif dset=="UTKflat":
        return UTKflat
    elif dset=="CENSUS":
        return CENSUS
    elif dset=="COMPAS":
        return COMPAS
    else :
        raise ValueError(f"The dataset {dset} doesn't have a dedicated neural network achitecture in pytorch")

class LAW(nn.Module):
    def __init__(self,l1=10,l2=5):
        super().__init__()
        self.config = {"lr":0.01,"bs":100,"epoch":10}
        self.fc1 = nn.Linear(9, l1)
        self.fc2 = nn.Linear(l1, l2)
        self.fc3 = nn.Linear(l2, 2)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        x = self.fc1(x)
        x = F.relu(x)
        x = self.fc2(x)
        x = F.relu(x)
        x = self.fc3(x)
        output = self.sigmoid(x)

        return output

class CENSUS(nn.Module):
    def __init__(self,l1=10,l2=5):
        super().__init__()
        self.config = {"lr":0.01,"bs":100,"epoch":10}
        self.fc1 = nn.Linear(8, l1)
        self.fc2 = nn.Linear(l1, l2)
        self.fc3 = nn.Linear(l2, 2)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        x = self.fc1(x)
        x = F.relu(x)
        x = self.fc2(x)
        x = F.relu(x)
        x = self.fc3(x)
        output = self.sigmoid(x)

        return output
    
class COMPAS(nn.Module):
    def __init__(self,l1=10,l2=5):
        super().__init__()
        self.config = {"lr":0.01,"bs":100,"epoch":10}
        self.fc1 = nn.Linear(6, l1)
        self.fc2 = nn.Linear(l1, l2)
        self.fc3 = nn.Linear(l2, 2)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        x = self.fc1(x)
        x = F.relu(x)
        x = self.fc2(x)
        x = F.relu(x)
        x = self.fc3(x)
        output = self.sigmoid(x)

        return output

class UTKflat(nn.Module):
    def __init__(self):
        super().__init__()
        self.config = {"lr":0.0005,"bs":200,"epoch":10}
        self.fc1 = nn.Linear(1600, 1000)
        self.fc2 = nn.Linear(1000, 500)
        self.fc3 = nn.Linear(500, 500)
        self.fc4 = nn.Linear(500, 100)
        self.fc5 = nn.Linear(100, 10)
        self.fc6 = nn.Linear(10, 2)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        x = self.fc1(x)
        x = F.relu(x)
        x = self.fc2(x)
        x = F.relu(x)
        x = self.fc3(x)
        x = F.relu(x)
        x = self.fc4(x)
        x = F.relu(x)
        x = self.fc5(x)
        x = F.relu(x)
        x = self.fc6(x)
        output = self.sigmoid(x)

        return output

def get_tensorflow(dset):
    if dset=="LAW":
        return LAWpredictor
    elif dset=="UTKflat":
        return UTKflatpredictor
    elif dset=="CENSUS":
        return CENSUSpredictor
    elif dset=="COMPAS":
        return COMPASpredictor
    else:
        raise ValueError(f"The dataset {dset} doesn't have a dedicated neural network achitecture in tensorflow")

class LAWpredictor:
    def __init__(self):
        self.lr = 0.01
        self.epochs=10
        self.bs = 100
        # Création du modèle de réseau de neurones
        self.model = tf.keras.Sequential([
            tf.keras.layers.Input(shape=(9,)),
            tf.keras.layers.Dense(10, activation='relu'),
            tf.keras.layers.Dense(5, activation='relu'),
            tf.keras.layers.Dense(1, activation='sigmoid')
        ])

        # Compilation du modèle
        optimizer = tf.keras.optimizers.Adam(learning_rate=0.01)
        self.model.compile(optimizer=optimizer, loss='binary_crossentropy', metrics=['accuracy'])
        

    def fit(self, x,y):

        # Entraînement du modèle
        self.model.fit(x, y, epochs=10, batch_size=100)

    def predict_proba(self, x):
        return self.model.predict(x)

    def predict(self, x):
        return (self.predict_proba(x)>0.5).astype(int).reshape(-1)

class CENSUSpredictor:
    def __init__(self):
        self.lr = 0.01
        self.epochs=10
        self.bs = 100
        # Création du modèle de réseau de neurones
        self.model = tf.keras.Sequential([
            tf.keras.layers.Input(shape=(8,)),
            tf.keras.layers.Dense(10, activation='relu'),
            tf.keras.layers.Dense(5, activation='relu'),
            tf.keras.layers.Dense(1, activation='sigmoid')
        ])

        # Compilation du modèle
        optimizer = tf.keras.optimizers.Adam(learning_rate=0.01)
        self.model.compile(optimizer=optimizer, loss='binary_crossentropy', metrics=['accuracy'])
        

    def fit(self, x,y):

        # Entraînement du modèle
        self.model.fit(x, y, epochs=10, batch_size=100)

    def predict_proba(self, x):
        return self.model.predict(x)

    def predict(self, x):
        return (self.predict_proba(x)>0.5).astype(int).reshape(-1)

class COMPASpredictor:
    def __init__(self):
        self.lr = 0.01
        self.epochs=10
        self.bs = 100
        # Création du modèle de réseau de neurones
        self.model = tf.keras.Sequential([
            tf.keras.layers.Input(shape=(6,)),
            tf.keras.layers.Dense(10, activation='relu'),
            tf.keras.layers.Dense(5, activation='relu'),
            tf.keras.layers.Dense(1, activation='sigmoid')
        ])

        # Compilation du modèle
        optimizer = tf.keras.optimizers.Adam(learning_rate=0.01)
        self.model.compile(optimizer=optimizer, loss='binary_crossentropy', metrics=['accuracy'])
        

    def fit(self, x,y):

        # Entraînement du modèle
        self.model.fit(x, y, epochs=10, batch_size=100)

    def predict_proba(self, x):
        return self.model.predict(x)

    def predict(self, x):
        return (self.predict_proba(x)>0.5).astype(int).reshape(-1)

class UTKflatpredictor:
    def __init__(self):
        self.lr = 0.0005
        self.epochs=10
        self.bs = 200
        # Création du modèle de réseau de neurones
        self.model = tf.keras.Sequential([
            tf.keras.layers.Input(shape=(1600,)),
            tf.keras.layers.Dense(1000, activation='relu'),
            tf.keras.layers.Dense(500, activation='relu'),
            tf.keras.layers.Dense(100, activation='relu'),
            tf.keras.layers.Dense(10, activation='relu'),
            tf.keras.layers.Dense(1, activation='sigmoid')
        ])

        # Compilation du modèle
        optimizer = tf.keras.optimizers.Adam(lr=0.0005)
        self.model.compile(optimizer=optimizer, loss='binary_crossentropy', metrics=['accuracy'])
        

    def fit(self, x,y):

        # Entraînement du modèle
        self.model.fit(x, y, epochs=10, batch_size=200)

    def predict_proba(self, x):
        return self.model.predict(x)

    def predict(self, x):
        return (self.predict_proba(x)>0.5).astype(int).reshape(-1)
