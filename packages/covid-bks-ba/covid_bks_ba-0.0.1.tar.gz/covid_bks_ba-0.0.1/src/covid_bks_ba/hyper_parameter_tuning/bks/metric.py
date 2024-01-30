import numpy as np
import pickle
import os
from pathlib import Path

class Missed:
    def __init__(self,n_mods,number_of_folds=5):
        self.number_of_folds=number_of_folds
        self.n_mods = n_mods
        self.missed = np.zeros([len(n_mods),number_of_folds]).astype(float)

    def add_result(self, missed,n_mod, k):
        j = np.argwhere(self.n_mods==n_mod)
        self.missed[j,k] = missed

    def save(self, nom):
        path = Path("tuning","bks","n_mod",nom)
        os.makedirs(path,exist_ok=True)
        with open(Path(path,"missed.pickle"), 'wb') as f:
            pickle.dump(self.missed,f)



class Utility:
    def __init__(self, n_mods, number_of_folds=5):
        #For each n_mod, there is an array of metrics (accuracy, balanced accuracy, ...) 
        #coresponding to cross validation steps.
        self.number_of_folds=number_of_folds
        self.n_mods = n_mods
        self.accuracy = np.zeros([len(n_mods),number_of_folds]).astype(float)
        self.balanced_accuracy = np.zeros([len(n_mods),number_of_folds]).astype(float)

    def add_result(self,y,yhat,n_mod,k):
        a = np.mean(y==yhat)

        a0 = np.mean(yhat[y==0]==0)
        a1 = np.mean(yhat[y==1]==1)
        ba = 0.5*(a0+a1)

        j = np.argwhere(self.n_mods==n_mod)
        self.accuracy[j,k] = a
        self.balanced_accuracy[j,k] = ba
    
    def save(self, nom):
        path = Path("tuning","bks","n_mod",nom)
        os.makedirs(path,exist_ok=True)
        with open(Path(path,"accuracy.pickle"), 'wb') as f:
            pickle.dump(self.accuracy,f)
        with open(Path(path,"balanced_accuracy.pickle"), 'wb') as f:
            pickle.dump(self.balanced_accuracy,f)
        with open(Path(path,"n_mods.pickle"), 'wb') as f:
            pickle.dump(self.n_mods,f)
