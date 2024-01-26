import os
from pathlib import Path
import pickle
import numpy as np

class fairness:
    def __init__(self):
        self.values = {"alpha":np.array([]),"f":np.array([])}

    def add_result(self,alpha,y,yhat,z):
        f0 = np.mean(yhat[z==0]==0)
        f1 = np.mean(yhat[z==1]==0)
        f = np.abs(f0-f1)
        self.values["alpha"] = np.append(self.values["alpha"],alpha)
        self.values["f"] = np.append(self.values["f"],f)

    def save(self,dset,attrib):
        path = Path("tuning","debiasing","alpha")
        path = Path(path,dset,attrib)
        os.makedirs(path,exist_ok=True)
        with open(Path(path,"fairness.pickle"),'wb') as f:
            pickle.dump(self.values,f)

class utility:
    def __init__(self):
        self.values = {"alpha":np.array([]),"ba":np.array([])}

    def add_result(self, alpha, y, yhat):
        ba = np.mean([np.mean(yhat[y==yy]==yy) for yy in np.unique(y)])
        self.values["alpha"] = np.append(self.values["alpha"],alpha)
        self.values["ba"] = np.append(self.values["ba"],ba)

    def save(self,dset,attrib):
        path = Path("tuning","debiasing","alpha")
        path = Path(path,dset,attrib)
        os.makedirs(path,exist_ok=True)
        with open(Path(path,"utility.pickle"),'wb') as f:
            pickle.dump(self.values,f)
