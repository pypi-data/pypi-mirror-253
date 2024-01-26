import numpy as np

from .__init__ import load_format
from .__init__ import split

def dp_lvl(dset, attrib):
    data = load_format(dset, attrib)
    a0 = np.mean(data["y"][data["z"]==0]==0)
    a1 = np.mean(data["y"][data["z"]==1]==1)
    return np.abs(a0-a1)


def counting(dset):
    data = load_format(dset, "sex")
    count = {}
    count["total"] = np.shape(data["y"])[0]
    count["features"] = np.shape(data["x"])[1]
    T = split(data)
    count["target"] = {"train":np.shape(T["train"]["y"])[0], "test":np.shape(T["test"]["y"])[0]}
    aux = T["test"]
    U = split(aux)
    count["aux"] = {"train":np.shape(U["train"]["y"])[0], "test":np.shape(U["test"]["y"])[0]}
    return count

