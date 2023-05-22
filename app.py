from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template('index.html')

@app.route("/stores")
def stores():
    return render_template('stores.html')

@app.route("/keke")
def keke():
    return render_template('keke.html')