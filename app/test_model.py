import numpy as np
import pandas as pd
import pickle

features = ["ra", "dec", "u", "g", "r", "i", "z", "redshift"]
fi_cols = ["u", "g", "r", "redshift", "g-r", "i-z", "u-r", "i-r", "z-r"]


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
    with open(file="model_stacking_classifier.pkl", mode="rb") as m_pkl:
        clf = pickle.load(file=m_pkl)
    pred_proba = clf.predict_proba(X=X)
    confidence = np.round(a=np.max(pred_proba) * 100, decimals=1)
    pred_class = clf.predict(X=X)[0]
    if pred_class == "QSO":
        pred_class = "Quasar"
    if pred_class == "STAR":
        pred_class = "Star"
    return f"The predicted class is '{pred_class}' with a confidence of {confidence}%."


def test_model(ra, dec, u, g, r, i, z, redshift):
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
                redshift,
            ]
        ],
        columns=features,
    )
    df = preprocess(df=df, features=features)
    df = featurize(df=df)
    return prediction(df)


print(
    test_model(
        ra=99.7741238427793,
        dec=-1.10633761268037,
        u=16.55442,
        g=14.60306,
        r=13.89092,
        i=13.64049,
        z=13.52043,
        redshift=-3.229735e-05,
    )
)  # Star

print(
    test_model(
        ra=195.953918788569,
        dec=0.336255783379351,
        u=23.45055,
        g=20.91976,
        r=18.93975,
        i=18.71329,
        z=18.23316,
        redshift=3.648712,
    )
)  # Quasar
