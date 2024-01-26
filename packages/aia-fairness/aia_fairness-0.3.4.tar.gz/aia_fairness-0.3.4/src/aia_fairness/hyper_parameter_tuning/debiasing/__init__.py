import pickle
import sys

if len(sys.argv)>1:
    if sys.argv[1]=="plot":
        print("plot mode")
        from .alpha_optimization import rule 
        from .. import config
        from .plot import *
        dsets = config.dsets
        attribs = config.attribs
        alphas = {}
        for dset in dsets:
            alphas[dset] = {}
            for attrib in attribs:
                alpha, fair, util, lim= rule(dset,attrib)
                alphas[dset][attrib] = alpha
                plot(dset,attrib)
                latex()
        with open("alpha.pickle", 'wb') as f:
            pickle.dump(alphas,f)

        quit()

    if sys.argv[1] == "update":
        print("Update mode, debiasing hyperparameter will be update in your local virtual environement")
        #Merge alphas 
        from .alpha_manager import *
        from .. import config
        alphas = load_alpha_dct()
        for dset in config.dsets:
            try :
                alphas[dset]
            except:
                alphas[dset] = {}
            for attrib in config.attribs:
                alphas[dset][attrib] = load_alpha(dset,attrib)
            print(alphas)

        #Copy to venv
        set_alpha_dct(alphas)
        print("New alpha set, you need to push new alphas to package distribution")
        quit()

print("run mode")
