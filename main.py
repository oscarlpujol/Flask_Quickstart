from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/test", methods=["GET"])
def render_test():
    if request.method == "GET":
        with open("./data/parameters.json") as file:
            parameters = json.load(file)
        return render_template("test.html", parameters=parameters)
