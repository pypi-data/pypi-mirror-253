import numpy as np
import concurrent.futures as fu

from aia_fairness import evaluation

from .. import dataset_processing as dp
from .. import config as config

models = config.models

def loop(model):
    data = dp.load_format()
    utility = evaluation.utility()
    for k in range(config.NN):
        T = dp.split(data,k)
        clf = model()
        clf.fit(T["train"]["x"],T["train"]["y"])
        yhat = clf.predict(T["test"]["x"])
        utility.add_result(T["test"]["y"],yhat)
    utility.save(type(clf).__name__,"covid","_")
        
for model in models:
    if config.para:
        ex = fu.ThreadPoolExecutor()
        ex.submit(loop, model)
    else:
        loop(model)
