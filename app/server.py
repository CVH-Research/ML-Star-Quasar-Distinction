#!/usr/bin/env python

# flask --app server run -p 5001

from flask import Flask, render_template, request, jsonify
from model import *

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route(r"/", methods=["POST"])
def submit():
    data = request.form
    ra = data.get("ra")
    dec = data.get("dec")
    u = data.get("u")
    g = data.get("g")
    r = data.get("r")
    i = data.get("i")
    z = data.get("z")
    redshift = data.get("redshift")
    pred, conf = run_model(ra, dec, u, g, r, i, z, redshift)
    return render_template("index.html", output=f"{pred} with {conf}% confidece.")


if __name__ == "__main__":
    app.run(debug=True)
