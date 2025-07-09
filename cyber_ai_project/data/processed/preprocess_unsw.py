# preprocess_unsw.py
import pandas as pd

df = pd.read_csv("../raw/UNSW-NB15.csv")
df.dropna(inplace=True)
df.to_csv("../processed/network_features.csv", index=False)
