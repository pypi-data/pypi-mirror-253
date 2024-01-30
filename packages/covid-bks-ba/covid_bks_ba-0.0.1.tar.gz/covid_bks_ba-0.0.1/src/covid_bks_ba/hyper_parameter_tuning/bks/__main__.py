import numpy as np
import concurrent.futures as fu

from .metric import *
from .. import dp
from .. import config
from .. import models

models_lst = [models.AdaBoost, models.AdaBoost_Bks, models.AdaBoost_Bks_Ba]

def loop(model):
    data = dp.load_format()
    n_mods = np.arange(1,51)
    utility = Utility(n_mods,number_of_folds=config.NN)
    if model.__name__ != "AdaBoost":
        missed = Missed(n_mods,number_of_folds=config.NN)
    for n_mod in n_mods:
        for k in range(config.NN):
            T = dp.split(data,k)
            clf = model(n_mod=n_mod)
            clf.fit(T["train"]["x"],T["train"]["y"])
            if model.__name__=="AdaBoost":
                yhat= clf.predict(T["test"]["x"])
            else:
                yhat,missed_tmp = clf.predict(T["test"]["x"],return_missed=True)
                missed.add_result(missed_tmp, n_mod,k)
            utility.add_result(T["test"]["y"],yhat,n_mod,k)
    utility.save(type(clf).__name__)
    if model.__name__ != "AdaBoost":
        missed.save(type(clf).__name__)
            
for model in models_lst:
    if config.para:
        ex = fu.ThreadPoolExecutor()
        ex.submit(loop, model)
    else:
        loop(model)


