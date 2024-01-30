import sys

if len(sys.argv)>1:
    if sys.argv[1]=="plot":
        print("plot mode")
        from ..result import *
        from ..import config
        dsets = ["covid"]
        evaltypes = ["utility"]
        metrics={"utility":["accuracy", "balanced_accuracy"]}

        for dset in dsets:
            for evaltype in evaltypes:
                for metric in metrics[evaltype]:
                    boxplot(dset, evaltype, metric)

        quit()

print("run mode")
