from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/test", methods=["GET"])
def test():
    if request.method == "GET":
        return render_template("test.html")