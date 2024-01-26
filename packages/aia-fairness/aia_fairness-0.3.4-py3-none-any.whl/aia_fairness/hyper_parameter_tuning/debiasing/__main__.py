import pickle
import numpy as np
import concurrent.futures as fu
from pathlib import Path
import os

from .. import target
from .. import dp
from .. import config

from . import metric

dsets = config.dsets
attribs = config.attribs

def loop(dset, attrib):
    data = dp.load_format(dset,attrib)
    if config.small:
        print("small")
        data["x"] = data["x"][:10]
        data["y"] = data["y"][:10]
        data["z"] = data["z"][:10]
    T = dp.split(data)
    alphas = np.linspace(0,1,11)
    p = 0.2 #percentage of loss in accuracy allowed
    #Train without debiasing 
    h = target.NeuralNetwork(dset, attrib)
    h.fit(T["train"]["x"],T["train"]["y"])
    yhat = h.predict(T["test"]["x"])
    #a = balanced accuracy without debiasing
    a = np.mean([np.mean(yhat[T["test"]["y"]==y]==y) for y in np.unique(T["test"]["y"])])
    
    path = Path("tuning","debiasing","alpha")
    path = Path(path,dset,attrib)
    os.makedirs(path,exist_ok=True)
    with open(Path(path,"base_utility.pickle"),'wb') as f:
        pickle.dump(a,f)

    fairness = metric.fairness()
    utility = metric.utility()
    for ai,alpha in enumerate(alphas):
        h = target.NeuralNetwork_AdversarialDebiasing(dset, attrib,alpha=alpha)
        #Train debiasing with alpha 
        h.fit(T["train"]["x"],T["train"]["y"],T["train"]["z"])
        yhat = h.predict(T["test"]["x"])
        fairness.add_result(alpha,T["test"]["y"], yhat,T["test"]["z"])
        utility.add_result(alpha,T["test"]["y"], yhat)

    utility.save(dset, attrib)
    fairness.save(dset, attrib)

    #choosen alpha = argmin_{alpha,y>=x-p(x-0.5)}f[ai]
    #mask = b>=a-p*(a-0.5)
    #idx = np.linspace(0,len(alphas)-1, len(alphas)).astype(int)
    #i = np.argmin(f[mask])
    #alpha = alphas[idx[mask][i]]

for dset in dsets:
    for attrib in attribs:
        if config.para:
            ex = fu.ThreadPoolExecutor()
            ex.submit(loop, dset, attrib)
        else:
            loop(dset, attrib)
