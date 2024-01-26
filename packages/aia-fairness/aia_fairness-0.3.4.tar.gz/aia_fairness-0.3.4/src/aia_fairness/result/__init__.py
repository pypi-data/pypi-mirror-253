import numpy as np
import pickle
import matplotlib.pyplot as plt
from pathlib import Path
import os


def boxplot(dset, attrib, evaltype, metric):

    targets  = os.listdir(Path("result"))
    m = []
    l = []
    for target in targets:
        try:
            with open(Path("result",target,evaltype,dset,attrib,f"{metric}.pickle"), 'rb') as f:
                m += [pickle.load(f)]
                l += [target]
        except:
            pass

    try:
        plt.boxplot(m,labels=l)
    except:
        print(f"{dset} {attrib} {evaltype} {metric}")
        quit()
    if metric=="rct_dp_lvl":
        plt.ylabel("0.5(1+demPar_level)")
    else:
        plt.ylabel(metric)
    plt.xticks(rotation=30, ha="right")
    path = Path("plot",dset,attrib,evaltype)
    os.makedirs(path,exist_ok=True)
    plt.savefig(Path(path,f"{metric}.pdf"), bbox_inches="tight")
    plt.clf()

def histogram(dset, attrib):

    targets  = os.listdir(Path("result"))
    for target in targets:
        with open(Path("result",target,"fairness",dset,attrib,"distinguishability.pickle"), 'rb') as f:
            d = pickle.load(f)

        x = np.linspace(0,1,10)
        hist0 = []
        hist1 = []
        for i in range(9):
            mask0 = (d["p0"]<=x[i+1])&(d["p0"]>=x[i])
            mask1 = (d["p1"]<=x[i+1])&(d["p1"]>=x[i])
            hist0 += [np.mean(mask0)]
            hist1 += [np.mean(mask1)]
        hist0 = np.concatenate([[hist0[0]], hist0])
        hist1 = np.concatenate([[hist1[0]], hist1])
        #plt.step(x,hist0,label="z=0")
        #plt.step(x,hist1,label="z=1")
        plt.hist(d["p0"], density=True, histtype="stepfilled", fc=(1,0,0,0.3), label="z=0")
        plt.hist(d["p1"], density=True, histtype="stepfilled", fc=(0,1,0,0.3), label="z=1")
        plt.legend()
        plt.xlim([0,1])
        plt.xlabel("Soft label")
        plt.ylabel("Density")
        path = Path("plot",dset,attrib,"distinguishability")
        os.makedirs(path, exist_ok=True)
        plt.title(target)
        plt.savefig(Path(path,f"{target}.pdf"),bbox_inches="tight")
        plt.clf()

def latex():
    size = 0.49
    tex = """\\documentclass{article}
\\usepackage{graphicx}
\\begin{document}
"""
    dsets = os.listdir(Path("plot"))
    for dset in dsets:
        tex += f"\\section{{ {dset} }}\n"
        attribs = os.listdir(Path("plot",dset))
        for attrib in attribs:
            tex += f"\\subsection{{ {attrib} }}\n"
            evaltypes = os.listdir(Path("plot",dset,attrib))
            for evaltype in evaltypes:
                tex += f"\\subsubsection{{ {evaltype} }}\n"
                if evaltype=="attack":
                    atypes = os.listdir(Path("plot",dset,attrib,evaltype,))
                    tex += "\\begin{tabular}{c}\n"
                    for atype in atypes:
                        tex += f"{atype}\\\\ \n"
                        metrics = os.listdir(Path("plot",dset,attrib,evaltype,atype))
                        for metric in metrics:
                            tex += f"\\includegraphics[width={size}\\linewidth]{{ plot/{dset}/{attrib}/{evaltype}/{atype}/{metric} }}\n"
                        tex += "\\\\"
                    tex += "\\end{tabular}\n"

                else:
                    metrics = os.listdir(Path("plot",dset,attrib,evaltype))
                    count = 0
                    for metric in metrics:
                        if (count%2==0)&(count!=0):
                            tex += "\\newline"
                        tex += f"\\includegraphics[width={size}\\linewidth]{{ plot/{dset}/{attrib}/{evaltype}/{metric} }}\n"
                        count += 1

    tex += "\\end{document}\n"

    with open("main.tex", 'w') as f:
        f.write(tex)






