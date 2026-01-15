from flask import Flask, request, render_template
import mysql.connector

app = Flask(__name__)

@app.route('/')
def form():
    return render_template("form.html")

@app.route('/save', methods=['POST'])
def save():
    name = request.form['name']
    email = request.form['email']

    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database=""
    )

    cursor = db.cursor()
    cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
    db.commit()

    return render_template("success.html", name=name, email=email)

app.run(debug=True)
