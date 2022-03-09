from flask import Flask, jsonify


app = Flask(__name__)


@app.route("/")
def home():
    r = jsonify({"message": "Hello World!"})
    return r
