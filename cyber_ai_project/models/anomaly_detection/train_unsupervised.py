import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
import joblib

df = pd.read_csv("../../data/processed/network_features.csv")
X = StandardScaler().fit_transform(df.drop(columns=["label"]))

model = IsolationForest(n_estimators=100, contamination=0.01)
model.fit(X)
joblib.dump(model, "unsupervised_iforest_model.pkl")


# from transformers import pipeline

# generator = pipeline("text-generation", model="gpt2")
# prompt = "Generate a cybersecurity insurance claim report:"

# result = generator(prompt, max_length=100)[0]['generated_text']
# print(result)
