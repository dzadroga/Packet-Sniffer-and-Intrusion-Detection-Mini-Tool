import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

df = pd.read_csv("traffic_log.csv")

#if no label exists 
if "label" not in df.columns:
    df["label"] = df["syn_count"].apply(lambda x: 1 if x > 20 else 0)

X = df[["protol", "length", "syn_flag", "syn_count"]]
y = df["label"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2)

model = RandomForestClassifier()
model.fit(X_train, y_train)

joblib.dump(model, "traffic_model.pkl")

print("Model has been trained and saved.")

