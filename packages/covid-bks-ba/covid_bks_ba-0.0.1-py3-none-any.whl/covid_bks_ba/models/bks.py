import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from .. import config
from .. import seed


class AdaBoostBksClassifier:
    def __init__(self,n_mod=6):
        self.n_mod=n_mod

    def fit(self, x,y):
        self.model = AdaBoostClassifier(algorithm="SAMME.R",n_estimators=self.n_mod)
        self.model.fit(x,y)
        bks = np.concatenate([(estimator.predict(x)).reshape(-1,1) for estimator in self.model.estimators_],axis=1)
        yphi = LabelEncoder()
        yphi.fit(y)
        ylab = yphi.transform(y)

        #Majority vote
        vote = {}
        classes = np.unique(bks,axis=0)
        for u in classes:
            vote[str(u)] = np.zeros(len(y))
        for i in range(len(y)):
            vote[str(bks[i])][ylab[i]] += 1

        decision = {}
        for u in classes:
            decision[str(u)] = yphi.inverse_transform([np.argmax(vote[str(u)])])[0]
        self.decision = decision
            
    #def predict_proba(self,x):
    #    return self.model.predict_proba(x)[:,0]

    def is_seen(self, x):
        n = np.shape(x)[0]
        bks = np.concatenate([(estimator.predict(x)).reshape(-1,1) for estimator in self.model.estimators_],axis=1)
        mask = np.zeros(n).astype(bool)
        for i in range(n):
            mask[i] = str(bks[i]) in self.decision.keys()
        return mask
        
    def predict(self,x):
        n = np.shape(x)[0]
        pred = np.zeros(n)
        bks = np.concatenate([(estimator.predict(x)).reshape(-1,1) for estimator in self.model.estimators_],axis=1)
        for i in range(n):
            pred[i] = self.decision[str(bks[i])]
        return pred

class AdaBoostBksBaClassifier(AdaBoostBksClassifier):
    def __init__(self,n_mod):
        super().__init__(n_mod)

    def fit(self, x,y):
        self.model = AdaBoostClassifier(algorithm="SAMME.R",n_estimators=self.n_mod)
        self.model.fit(x,y)
        bks = np.concatenate([(estimator.predict(x)).reshape(-1,1) for estimator in self.model.estimators_],axis=1)

        #Finit classification for balanced accuracy
        #UTILISER LE PACKAGE FINIT CLASSIFICATION 
        from finit_classifier import FinitClassifier
        self.finit = FinitClassifier()
        self.finit.fit(bks,y)

    def is_seen(self, x):
        n = np.shape(x)[0]
        bks = np.concatenate([(estimator.predict(x)).reshape(-1,1) for estimator in self.model.estimators_],axis=1)
        return self.finit.is_seen(bks)

    def predict(self,x):
        n = np.shape(x)[0]
        pred = np.zeros(n)
        bks = np.concatenate([(estimator.predict(x)).reshape(-1,1) for estimator in self.model.estimators_],axis=1)
        return self.finit.predict(bks)
        #for i in range(n):
        #    pred[i] = self.decision[str(bks[i])]
        #return pred
