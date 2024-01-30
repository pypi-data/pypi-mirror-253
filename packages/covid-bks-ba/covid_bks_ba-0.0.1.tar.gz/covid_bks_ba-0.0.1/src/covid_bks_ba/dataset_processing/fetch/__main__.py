import numpy as np
import os
from pathlib import Path
import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder

from .. import seed

seed.setseed()

df = pd.read_csv("data.csv").drop("id",axis=1)
#Symptom encoding
le_symp = LabelEncoder()
le_symp.fit(np.concatenate([df["symptom1"].to_numpy(),
df["symptom2"].to_numpy(),
df["symptom3"].to_numpy(),
df["symptom4"].to_numpy(),
df["symptom5"].to_numpy(),
df["symptom6"].to_numpy()]))

n = len(df.keys())-2
m = len(df)
x = np.zeros([m,n])
y = np.zeros(m)

le = {}
for key in df.keys():
    if key[:7]=="symptom":
        le[key]=le_symp
        le_symp.transform(df[key].to_numpy())
    else:
        le[key] = LabelEncoder()
        le[key].fit(df[key])

#Feature to use
feat_keys = ["location", "country", "gender", "age", "sym_on", "hosp_vis", "vis_wuhan", "from_wuhan", "symptom1", "symptom2", "symptom3", "symptom4", "symptom5", "symptom6"]

#Prediction task
lab_key = "death"

for i,feat_key in enumerate(feat_keys):
    x[:,i] = le[feat_key].transform(df[feat_key].to_numpy())
y[:] = le[lab_key].transform(df[lab_key].to_numpy())
idx = np.linspace(0,len(y)-1,len(y)).astype(int)
np.random.shuffle(idx)
np.random.shuffle(idx)
np.random.shuffle(idx)

data = {"x":x[idx], "y":y[idx]}

path = Path("data_format")
os.makedirs(path,exist_ok=True)
with open(Path(path,"covid.pickle"), 'wb') as f:
    pickle.dump(data,f)

