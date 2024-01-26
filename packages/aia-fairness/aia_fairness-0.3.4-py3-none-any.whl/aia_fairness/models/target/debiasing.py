import os
from os.path import abspath
from inspect import getsourcefile
import pickle
from pathlib import Path
import numpy as np
import silence_tensorflow.auto
from fairlearn.adversarial import AdversarialFairnessClassifier 
from fairlearn.adversarial import AdversarialFairnessRegressor 
import tensorflow as tf

def get_alpha(dset, attrib):
    lib = os.path.dirname(abspath(getsourcefile(lambda:0)))
    path = Path(lib,"alpha.pickle")
    with open(path, 'rb') as f:
        alphas = pickle.load(f)
    return alphas[dset][attrib]

# Générer des données tabulaires de démonstration
# Remplacez cela par vos propres données
class predictor:
    def __init__(self, num_features):
        # Création du modèle de réseau de neurones
        self.model = tf.keras.Sequential([
            tf.keras.layers.Input(shape=(num_features,)),
            tf.keras.layers.Dense(64, activation='relu'),
            tf.keras.layers.Dense(32, activation='relu'),
            tf.keras.layers.Dense(1, activation='sigmoid')
        ])

        # Compilation du modèle
        self.model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
        

    def fit(self, x,y):

        # Entraînement du modèle
        self.model.fit(x, y, epochs=5, batch_size=100)

    def predict_proba(self, x):
        return self.model.predict(x)

    def predict(self, x):
        return (self.predict_proba(x)>0.5).astype(int).reshape(-1)



class adversary:
    def __init__(self):
        # Création du modèle de réseau de neurones
        self.model = tf.keras.Sequential([
            tf.keras.layers.Input(shape=(1,)),
            tf.keras.layers.Dense(1, activation='relu'),
            tf.keras.layers.Dense(32, activation='relu'),
            tf.keras.layers.Dense(32, activation='relu'),
            tf.keras.layers.Dense(32, activation='relu'),
            tf.keras.layers.Dense(1, activation='sigmoid')
        ])

        # Compilation du modèle
        self.model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])


    def set_sizes(self, sizes):
        self.model = tf.keras.Sequential([
            tf.keras.layers.Input(shape=(1,)),
            tf.keras.layers.Dense(1, activation='relu'),
            tf.keras.layers.Dense(sizes[0], activation='relu'),
            tf.keras.layers.Dense(sizes[1], activation='relu'),
            tf.keras.layers.Dense(sizes[2], activation='relu'),
            tf.keras.layers.Dense(1, activation='sigmoid')
        ])

        # Compilation du modèle
        self.model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])



    def fit(self, x,y):

        # Entraînement du modèle
        self.model.fit(x,y, epochs=10, batch_size=32)

    def predict_proba(self, x):
        return self.model.predict(x)

    def predict(self, x):
        return (self.predict_proba(x)>0.5).astype(int).reshape(-1)

class debiasing:
    def __init__(self, dset,attrib,alpha=None):
        from . import predictors
        self.predictor = predictors.get_tensorflow(dset)()
        self.adversary = adversary()
        if alpha==None:
            alpha_in_use = get_alpha(dset, attrib)
        else:
            alpha_in_use = alpha

        self.model = AdversarialFairnessClassifier(alpha=alpha_in_use,learning_rate=self.predictor.lr,epochs=self.predictor.epochs,batch_size=self.predictor.bs)


    def fit(self, x, y, z):
        #n = np.shape(y)[0]
        #u =np.random.normal(0,00.1,n)
        self.model.fit(x, y, sensitive_features=z)

    def predict_proba(self,x):
        return self.model.decision_function(x)

    def predict(self, x):
        return self.model.predict(x)

