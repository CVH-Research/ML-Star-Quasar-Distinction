import numpy as np
import pandas as pd

import pickle
import warnings

warnings.filterwarnings("ignore")

features = ["ra", "dec", "u", "g", "r", "i", "z"]
fi_cols = ["u", "g", "r", "g-r", "i-z", "u-r", "i-r", "z-r"]


def preprocess(df, features):
    with open(file="scaling.pkl", mode="rb") as pre_pkl:
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
    with open(file="model_random_forest_classifier.pkl", mode="rb") as m_pkl:
        clf_tuple = pickle.load(file=m_pkl)
    clf = clf_tuple[1]  # CalibratedClassifierCV
    pred_proba = clf.predict_proba(X=X)
    confidence = np.round(a=np.max(pred_proba) * 100, decimals=1)
    pred_class = clf.predict(X=X)[0]
    if pred_class == "QSO":
        pred_class = "Quasar"
    if pred_class == "STAR":
        pred_class = "Star"
    return pred_class, confidence


def run_model(ra, dec, u, g, r, i, z):
    df = pd.DataFrame(
        data=[
            [
                ra,
                dec,
                u,
                g,
                r,
                i,
                z,
            ]
        ],
        columns=features,
    )
    df = preprocess(df=df, features=features)
    df = featurize(df=df)
    return prediction(df)
