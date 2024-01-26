import pickle 
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
import os

from .alpha_optimization import rule

def plot(dset,attrib):
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

    alpha, fair, util, lim = rule(dset,attrib)



    plt.rcParams.update({
        "text.usetex": True,
        "font.family": "Helvetica"
    })
    plt.plot(alphas,fairness,label="dempar_lvl")
    plt.plot([0,1],[a,a],label="BA without debiasing")
    plt.fill([0,1,1,0],[lim,lim,1,1],color=(0,1,0,0.3),label="Accepted loss in BA")
    plt.plot(alphas,b,label="BA with debiasing")
    plt.plot([alpha,alpha],[fair,util],'ro',label="chosen $\\alpha$")
    plt.legend()
    plt.xlabel("$\\alpha$")
    path = Path("tuning","debiasing","alpha","plot")
    path = Path(path,dset,attrib)
    os.makedirs(path,exist_ok=True)
    plt.savefig(Path(path,"a_fb.pdf"),bbox_inches="tight")
    plt.clf()
    fm = np.min(fairness)
    fM = np.max(fairness)
    plt.plot(b,fairness,'bo')
    plt.plot([a,a],[fm,fM],label="BA without debiasing")
    plt.fill([lim,lim,1,1],[fm,fM,fM,fm],color=(0,1,0,0.3),label="Accepted loss in BA")
    plt.plot(util,fair,'ro',label="chosen $\\alpha$")
    plt.xlabel("Balanced accuracy (BA)")
    plt.ylabel("dmpar_lvl")
    plt.legend()
    plt.savefig(Path(path,"b_f.pdf"),bbox_inches="tight")
    plt.clf()

def latex():
    size = 0.49
    tex = """\\documentclass{article}
\\usepackage{graphicx}
\\begin{document}
"""
    path = Path("tuning","debiasing","alpha","plot")
    dsets = os.listdir(path)
    for dset in dsets:
        tex += f"\\section{{ {dset} }}\n"
        attribs = os.listdir(Path(path,dset))
        for attrib in attribs:
            tex += f"\\subsection{{ {attrib} }}\n"
            tex += f"\\includegraphics[width={size}\\linewidth]{{ tuning/debiasing/alpha/plot/{dset}/{attrib}/a_fb.pdf }}\n"
            tex += f"\\includegraphics[width={size}\\linewidth]{{ tuning/debiasing/alpha/plot/{dset}/{attrib}/b_f.pdf }}\n"

    tex += "\\end{document}\n"
    with open("alpha_tuning.tex", 'w') as f:
        f.write(tex)
