import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier

from .. import config
from .. import seed
from .bks import *

def get_n_mod():
    return 5

class BaseClassifier:
    """Base classifier to be used as a model for all target and attack.
    In our usecase all prediction and sensitive attributes are binary"""
    def __init__(self, dset = None,attrib=None):
        seed.setseed()

    def fit(self, x, y):
        pass

    def predict_proba(self, x):
        unif = np.random.uniform(0,1,np.shape(x)[0])
        return unif

    def predict(self, x):
        p = self.predict_proba(x)
        return p<0.5

class RandomForest(BaseClassifier):
    def __init__(self, dset=None,attrib=None):
        super().__init__(dset)
        self.model = RandomForestClassifier(random_state=config.random_state,n_estimators=100,criterion='gini',max_depth=2)

    def fit(self,x,y):
        self.model.fit(x,y)

    def predict_proba(self,x):
        return self.model.predict_proba(x)[:,0]

    def predict(self,x):
        return self.model.predict(x)

class AdaBoost(BaseClassifier):
    def __init__(self,n_mod=None):
        super().__init__()
        if n_mod==None:
            self.n_mod = get_n_mod()
        else:
            self.n_mod=n_mod

    def fit(self, x,y):
        self.model = AdaBoostClassifier(algorithm="SAMME.R",n_estimators=self.n_mod)
        self.model.fit(x,y)

    def predict_proba(self,x):
        return self.model.predict_proba(x)[:,0]

    def predict(self,x):
        return self.model.predict(x)
    
class AdaBoost_Bks(AdaBoost):
    def __init__(self,n_mod=None):
        super().__init__(n_mod)

    def fit(self, x,y):
        self.model = AdaBoostBksClassifier(n_mod=self.n_mod)
        self.model.fit(x,y)

    def predict_proba(self,x):
        return self.model.predict_proba(x)[:,0]

    def predict(self,x,return_missed=False):
        mask = self.model.is_seen(x)
        p = np.zeros(np.shape(x)[0])
        missed = np.mean(~mask)
        if missed != 1:
            p[mask] = self.model.predict(x[mask])
        #if x hasn't been seen, fall back to adaboost
        if missed != 0:
            p[~mask] = self.model.model.predict(x[~mask])
        if return_missed:
            missed = np.mean(~mask)
            return p,missed
        else:
            return p

class AdaBoost_Bks_Ba(AdaBoost):
    def __init__(self,n_mod=None):
        super().__init__(n_mod)

    def fit(self, x,y):
        self.model = AdaBoostBksBaClassifier(n_mod=self.n_mod)
        self.model.fit(x,y)

    def predict_proba(self,x):
        return self.model.predict_proba(x)[:,0]

    def predict(self,x,return_missed=False):
        mask = self.model.is_seen(x)
        p = np.zeros(np.shape(x)[0])
        missed = np.mean(~mask)
        if missed != 1:
            p[mask] = self.model.predict(x[mask])
        #if x hasn't been seen, fall back to adaboost
        if missed != 0:
            p[~mask] = self.model.model.predict(x[~mask])
        if return_missed:
            missed = np.mean(~mask)
            return p,missed
        else:
            return p
