# flask --app app.py --debug run
# sqlite3 database.db
from flask import Flask, render_template, request, jsonify
import sqlite3


app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET" or request.method == "POST":
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        cursor.execute("SELECT COUNT(*) FROM suggestions")
        result = cursor.fetchone()
        row_count = result[0]

        cursor.close()
        conn.close()

        jsonify(row_count)
        return render_template('index.html', row_count=row_count)

@app.route("/stores")
def stores():
    return render_template('stores.html')

@app.route('/activities')
def activities():
    return render_template('activities.html')

@app.route('/suggestions', methods=["GET"])
def suggestions():
    if request.method == "GET":
        return render_template('suggestions.html')

@app.route("/keke")
def keke():
    return render_template('keke.html')

@app.route("/aqua")
def aquarium():
    return render_template('aqua.html')

@app.route("/hopscotch")
def hopscotch():
    return render_template('hopscotch.html')

@app.route("/lighthouse")
def lighthouse():
    return render_template('lighthouse.html')

@app.route("/makers_market")
def makers_market():
    return render_template('makers_market.html')

@app.route("/thanks", methods=["POST"])
def thanks():
    name = request.form.get('name')
    description = request.form.get('description')
    with sqlite3.connect("database.db") as con:
        con.execute("INSERT INTO suggestions (name, description) VALUES(?, ?)", (name, description))
    return render_template('thanks.html')