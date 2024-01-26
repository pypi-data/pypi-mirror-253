"""Trains a target random forest
return the predictions for each dataset and test set"""
#In this script we train a target with various models
import numpy as np
import concurrent.futures as fu
from pathlib import Path

from .. import dataset_processing as dp
from ..models import target as targets
from ..models import attack as attacks
from .. import evaluation as evaluations
from .. import config as config

print("RUN MODE")

dsets = config.dsets
attribs = config.attribs
target_models = config.target_models

def loop(dset,attrib, target_models):
    for target_model in target_models:

        data = dp.load_format(dset, attrib)
        if config.small:
            print("small")
            data["x"] = data["x"][:10]
            data["y"] = data["y"][:10]
            data["z"] = data["z"][:10]

        #Initalize the metrics
        utility = evaluations.utility()
        fairness = evaluations.fairness()
        classif_eval = evaluations.attack("classification")
        regression_eval = evaluations.attack("regression")
        
        for k in range(config.NN):
            T = dp.split(data, k=k)
            target = target_model(dset)
            if target.need_z:
                target.fit(T["train"]["x"], T["train"]["y"],T["train"]["z"])
            else:
                target.fit(T["train"]["x"], T["train"]["y"])
            yhat = target.predict(T["test"]["x"])
            print(np.mean(yhat==T["test"]["y"]))
            #print(f"[{type(target).__name__} {dset}] yhat : {np.shape(yhat)}, y : {np.shape(T['test']['y'])}")
            #print(np.unique(T["test"]["y"]))
            utility.add_result(T["test"]["y"], yhat)
            soft = target.predict_proba(T["test"]["x"])
            aux = {"y":T["test"]["y"],
                   "z":T["test"]["z"],
                   "yhat":yhat,
                   "soft":soft}

            for l in range(config.NN):
                #split auxiliary data
                aux_split = dp.split(aux,k=l)
                    
                #train attack
                classif = attacks.Classification()
                regression = attacks.Regression()

                classif.fit(aux_split["train"]["yhat"], aux_split["train"]["z"])
                regression.fit(aux_split["train"]["soft"], aux_split["train"]["z"])
                zhat_classif = classif.predict(aux_split["test"]["yhat"])
                zhat_regression = classif.predict(aux_split["test"]["soft"])
                classif_eval.add_result(aux_split["test"]["z"],zhat_classif)
                regression_eval.add_result(aux_split["test"]["z"],zhat_regression)

                fairness.add_result(aux_split["test"]["soft"],aux_split["test"]["yhat"],aux_split["test"]["z"])


        utility.save(type(target).__name__,dset,attrib)
        fairness.save(type(target).__name__,dset,attrib)
        classif_eval.save(type(target).__name__,dset,attrib)
        regression_eval.save(type(target).__name__,dset,attrib)

for dset in dsets:
    for attrib in attribs:
        if config.para:
            ex = fu.ThreadPoolExecutor()
            ex.submit(loop, dset, attrib, target_models)
        else:
            loop(dset,attrib,target_models)
