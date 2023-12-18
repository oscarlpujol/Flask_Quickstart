from flask import Flask, render_template, request, redirect, url_for
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
        print(parameters)
        return render_template("test.html", parameters=parameters)
    
@app.route("/test", methods=["POST"])
def change_parameter():
    if request.method == "POST":
        print(request.form)
        with open("./data/parameters.json", 'w') as file:
            param = { "test" : request.form["test"]}
            file.write(json.dumps(param, ensure_ascii=False))

        return redirect(url_for("render_test"))