import numpy as np
from pathlib import Path
import pickle

def rule(dset, attrib):
    """Chooses best alpha to balance utility and fairness
    utility_neural (float) : balanced accuracy neural network without debiasing
    utility_debiasing (array of float) : balanced accuracy with debiasing
    alpha (array of float) : array of tested alpha
    fairness (array of float) : dempar_lvl 
    """
    path = Path("tuning","debiasing","alpha")
    path = Path(path,dset,attrib)
    with open(Path(path,"fairness.pickle"),'rb') as f:
        fairness = pickle.load(f)
    with open(Path(path,"utility.pickle"),'rb') as f:
        utility = pickle.load(f)
    with open(Path(path,"base_utility.pickle"),'rb') as f:
        a = pickle.load(f)

    alphas = fairness["alpha"]
    fairness = fairness["f"]
    b = utility["ba"]

    p = 0.2
    mask = b >=a-p*(a-0.5)
    idx = np.linspace(0,len(alphas)-1, len(alphas)).astype(int)
    i = np.argmin(fairness[mask])
    choosen = idx[mask][i]
    alpha_c = alphas[choosen]
    fairness_c = fairness[choosen]
    utility_c = b[choosen] 
    with open(Path(path,"alpha.pickle"), 'wb') as f:
        pickle.dump(alpha_c,f)
    return alpha_c, fairness_c, utility_c, a-p*(a-0.5)


