import sys

if len(sys.argv)>1:
    if sys.argv[1]=="plot":
        print("plot mode")
        from ..result import *
        from ..import config
        from .. import result
        models = ["AdaBoost_Bks", "AdaBoost_Bks_Ba"]
        for model in models:
            boxplot(model)

        latex()

        quit()

print("run mode")
