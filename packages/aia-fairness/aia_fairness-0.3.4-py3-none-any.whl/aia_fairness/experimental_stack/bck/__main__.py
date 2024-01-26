import sys
print("__main__")

if len(sys.argv)>1:
    if sys.argv[1]=="plot":
        #In this mode we only create the box plots
        print("plot mode")
        from ..result import *
        from ..import config
        dsets = config.dsets
        attribs = config.attribs
        evaltypes = ["utility", "fairness", "attack"]
        metrics={"utility":["accuracy", "balanced_accuracy"],
                 "fairness":["dp_lvl","rct_dp_lvl"],
                 "classification":["accuracy", "balanced_accuracy"],
                 "regression":["accuracy", "balanced_accuracy"]}

        for dset in dsets:
            for attrib in attribs:
                for evaltype in ["utility", "fairness"]:
                    for metric in metrics[evaltype]:
                        boxplot(dset, attrib, evaltype, metric)

                for evaltype in ["classification", "regression"]:
                    for metric in metrics[evaltype]:
                        boxplot(dset, attrib, Path("attack",evaltype), metric)

                histogram(dset, attrib)

        latex()
        quit()

#in this mode we run the experiments
print("run mode")
quit()

