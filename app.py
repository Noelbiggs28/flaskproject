# flask --app app.py --debug run
# sqlite3 database.db
from flask import Flask, render_template, request
import sqlite3


app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template('index.html')

@app.route("/stores")
def stores():
    return render_template('stores.html')

@app.route('/activities')
def activities():
    return render_template('activities.html')

@app.route('/suggestions', methods=["GET", "POST"])
def suggestions():
    if request.method == "GET":
        return render_template('suggestions.html')
    else:
        name = request.form.get('name')
        description = request.form.get('description')
        with sqlite3.connect("database.db") as con:
            con.execute("INSERT INTO suggestions (name, description) VALUES(?, ?)", (name, description))
        return render_template('index.html')

@app.route("/keke")
def keke():
    return render_template('keke.html')

@app.route("/aqua")
def aquarium():
    return render_template('aqua.html')