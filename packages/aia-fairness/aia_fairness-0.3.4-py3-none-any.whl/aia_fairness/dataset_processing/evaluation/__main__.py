import pickle

from .. import metric
from .. import config

dp_lvl = {}

for dset in config.config.dsets:
    dp_lvl[dset] = {}
    for attrib in config.config.attribs:
        dp_lvl[dset][attrib] = metric.dp_lvl(dset, attrib)

with open("data_eval.pickle", "wb") as f:
    pickle.dump(dp_lvl,f)

tex = """
\\documentclass{article}
\\begin{document}
\\begin{tabular}"""
length = len(dp_lvl.keys())
col = "{c|"
for i in range(length):
    col += "c"
col += "}\n"
tex += col
tex += "&"
for dset in dp_lvl.keys():
    tex += f"{dset}&"
tex = tex[:-1]
tex += "\\\\"
tex += "\n"
tex += "\\hline\n"

for attrib in config.config.attribs:
    tex += f"{attrib}&"
    for dset in config.config.dsets:
        tex += f"{round(dp_lvl[dset][attrib],3)}&"
    tex = tex[:-1]
    tex += "\\\\"
    tex += "\n"

tex +="""
\\end{tabular}\n
"""
with open("data_eval.tex", 'w') as f:
    f.write(tex)


#Counting number of points 

tex = "\\begin{tabular}{cccccc}\n"
tex += "dataset&features&\\multicolumn{2}{c}{target}&\\multicolumn{2}{c}{auxiliary}\n"
tex += "&&train&test&train&test\n"
for dset in config.config.dsets:
    count = metric.counting(dset)
    tex += f"{dset}&{count['features']}&{count['target']['train']}&{count['target']['test']}&{count['aux']['train']}&{count['aux']['test']}\\\\\n"
tex += "\\end{tabular}\n"
tex += "\\end{document}\n"

with open("data_eval.tex", 'a') as f:
    f.write(tex)
