import matplotlib.pyplot as plt
import os
import pickle
import numpy as np
from pathlib import Path

def boxplot(model):
    #Load results for studied model
    path = Path("tuning", "bks", "n_mod",model)
    with open(Path(path, "accuracy.pickle"), 'rb') as f:
        accuracy = pickle.load(f)
    with open(Path(path, "balanced_accuracy.pickle"), 'rb') as f:
        balanced_accuracy = pickle.load(f)
    with open(Path(path, "missed.pickle"), 'rb') as f:
        missed = pickle.load(f)
    with open(Path(path, "n_mods.pickle"), 'rb') as f:
        n_mods = pickle.load(f)

    #Load results for baseline model
    path = Path("tuning", "bks", "n_mod","AdaBoost")
    with open(Path(path, "accuracy.pickle"), 'rb') as f:
        base_accuracy = pickle.load(f)
    with open(Path(path, "balanced_accuracy.pickle"), 'rb') as f:
        base_balanced_accuracy = pickle.load(f)

    plt.plot(n_mods,np.mean(accuracy,axis=1),label=model)
    plt.plot(n_mods,np.mean(base_accuracy,axis=1),label="AdaBoost")
    ax = plt.gca()
    ax.set_xticks(n_mods)
    ax.set_xticklabels(n_mods)
    plt.legend()
    plt.ylabel("Accuracy")
    plt.xlabel("Number of weak classifiers")
    save_path = Path("plot",path,model)
    os.makedirs(save_path,exist_ok=True)
    plt.savefig(Path(save_path,"accuracy.pdf"),bbox_inches='tight')
    plt.clf()

    plt.plot(n_mods,np.mean(balanced_accuracy,axis=1),label=model)
    plt.plot(n_mods,np.mean(base_balanced_accuracy,axis=1),label="AdaBoost")
    ax = plt.gca()
    ax.set_xticks(n_mods)
    ax.set_xticklabels(n_mods)
    plt.legend()
    plt.ylabel("Balanced accuracy")
    plt.xlabel("Number of weak classifiers")
    plt.savefig(Path(save_path,"balanced_accuracy.pdf"),bbox_inches='tight')
    plt.clf()

    plt.plot(n_mods,np.mean(missed,axis=1),label=model)
    ax = plt.gca()
    ax.set_xticks(n_mods)
    ax.set_xticklabels(n_mods)
    plt.ylabel("Number of missed points")
    plt.xlabel("Number of weak classifiers")
    plt.savefig(Path(save_path,"missed.pdf"),bbox_inches='tight')
    plt.clf()

def latex():
    models = ["AdaBoost_Bks", "AdaBoost_Bks_Ba"]
    evaltypes = ["accuracy","balanced_accuracy","missed"]
    tex = """
\\documentclass{article}
\\usepackage{graphicx}
\\begin{document}
"""
    for model in models:
        tex += f"\\section{{ {model.replace('_',' ')} }}\n"
        for evaltype in evaltypes:
            tex += f"\\subsection{{ {evaltype.replace('_',' ')} }}\n"
            tex += f"\\includegraphics[width=0.9\\linewidth]{{ plot/tuning/bks/n_mod/AdaBoost/{model}/{evaltype}.pdf }}\n"

    tex += "\\end{document}"
    with open("bks_tuning.tex", 'w') as f:
        f.write(tex)

