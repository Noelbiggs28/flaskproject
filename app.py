# flask --app app.py --debug run
# sqlite3 database.db
from flask import Flask, render_template, request
import sqlite3

db = sqlite3.connect('database.db')
db.close()
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

@app.route("/keke")
def keke():
    return render_template('keke.html')