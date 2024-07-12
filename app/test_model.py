from matplotlib import pyplot as plt
from tabulate import tabulate
import numpy as np
import os
import pandas as pd
import pickle
from sklearn.metrics import classification_report
import seaborn as sns

features = ["ra", "dec", "u", "g", "r", "i", "z", "redshift"]
fi_cols = ["u", "g", "r", "redshift", "g-r", "i-z", "u-r", "i-r", "z-r"]


def preprocess(df, features):
    scale = "scaling.pkl"
    with open(file=scale, mode="rb") as pre_pkl:
        scaling = pickle.load(file=pre_pkl)
    df = scaling.transform(X=df)
    df = pd.DataFrame(data=df, columns=features)
    return df


def featurize(df):
    df["g-r"] = df["g"] - df["r"]
    df["i-z"] = df["i"] - df["z"]
    df["u-r"] = df["u"] - df["r"]
    df["i-r"] = df["i"] - df["r"]
    df["z-r"] = df["z"] - df["r"]
    df = df[fi_cols]
    return df


def prediction(X):
    model = "model_stacking_classifier.pkl"
    with open(file=model, mode="rb") as m_pkl:
        clf = pickle.load(file=m_pkl)
    pred_proba = clf.predict_proba(X=X)
    confidence = np.round(a=np.max(pred_proba) * 100, decimals=2)
    pred_class = clf.predict(X=X)[0]
    if pred_class == "QSO":
        pred_class = "Quasar"
    else:
        pred_class = "Star"
    print(f"The predicted class is '{pred_class}' with a confidence of {confidence}%.")


df = pd.DataFrame(
    data=[["12", "12", "12", "12", "12", "12", "12", "1"]], columns=features
)
df = preprocess(df=df, features=features)
df = featurize(df=df)
prediction(df)
