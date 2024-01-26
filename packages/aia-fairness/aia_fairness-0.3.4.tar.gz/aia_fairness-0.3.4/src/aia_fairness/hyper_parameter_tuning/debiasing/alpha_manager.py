from pathlib import Path
import os
from inspect import getsourcefile
from os.path import abspath
import pickle


def load_alpha_dct():
    dct_path = os.path.dirname(abspath(getsourcefile(lambda:0)))
    dct_path = os.path.dirname(os.path.dirname(dct_path))
    dct_path = Path(dct_path,"models","target")
    with open(Path(dct_path,"alpha.pickle"), 'rb') as f:
        return pickle.load(f)

def set_alpha_dct(alphas):
    dct_path = os.path.dirname(abspath(getsourcefile(lambda:0)))
    dct_path = os.path.dirname(os.path.dirname(dct_path))
    dct_path = Path(dct_path,"models","target")
    with open(Path(dct_path,"alpha.pickle"), 'wb') as f:
        pickle.dump(alphas,f)

def load_alpha(dset, attrib):
    path = Path("tuning","debiasing","alpha")
    path = Path(path,dset,attrib)
    with open(Path(path,"alpha.pickle"), 'rb') as f:
        return pickle.load(f)
