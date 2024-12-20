from flask import Flask, render_template, request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

import time

from model import *

app = Flask(__name__)
limiter = Limiter(app=app, key_func=get_remote_address)


@app.route("/api")
def api():
    return get_remote_address()


@app.route("/api/predict", methods=["POST"])
@limiter.limit("60 per minute")
def predict():
    try:
        data = request.form
        ra = data.get("ra")
        dec = data.get("dec")
        u = data.get("u")
        g = data.get("g")
        r = data.get("r")
        i = data.get("i")
        z = data.get("z")
        pred, conf = run_model(ra, dec, u, g, r, i, z)
        output = {"prediction": pred, "confidence": conf}
    except ValueError as e:
        output = {"error": "Please enter valid values."}
    except Exception as e:
        output = {"error": str(e)}
    print(output, time.strftime("%H:%M:%S"), get_remote_address())
    return output, 500 if "error" in output else 200


@app.route("/")
@limiter.limit("60 per minute")
def index():
    return render_template(
        "index.html",
        ra="180",
        dec="0",
        u="15",
        g="15",
        r="15",
        i="15",
        z="15",
        output="Press submit to get a prediction.",
    )


@app.route("/", methods=["POST"])
@limiter.limit("30 per minute")
def submit():
    try:
        data = request.form
        ra = data.get("ra")
        dec = data.get("dec")
        u = data.get("u")
        g = data.get("g")
        r = data.get("r")
        i = data.get("i")
        z = data.get("z")
        print(ra, dec, u, g, r, i, z)
        pred, conf = run_model(ra, dec, u, g, r, i, z)
        output = f"{pred} with {conf}% confidence."
    except ValueError as e:
        output = "Please enter valid values."
    except Exception as e:
        output = f"Error: {e}"
    return render_template(
        "index.html",
        ra=ra,
        dec=dec,
        u=u,
        g=g,
        r=r,
        i=i,
        z=z,
        output=output,
    )


@app.errorhandler(429)
def ratelimit_handler(e):
    return "Rate limit has been exceeded. Please try again later.", 429


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
