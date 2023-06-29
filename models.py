
import pandas as pd
import json


df_train = pd.read_csv("../train.csv")
df_train.shape
df_train.head()

df_sup_data = pd.read_csv("../supplemental_metadata.csv")
df_sup_data.shape
df_sup_data.head()

with open("../character_to_prediction_index.json") as f:
    c2p = f.readlines()
c2p = c2p[0]
c2p_json = json.loads(c2p)

df_prq = pd.read_parquet("../train_landmarks/2072876091.parquet")
df_prq.index.nunique()