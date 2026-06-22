from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root"
)

cursor = db.cursor()

with open("schema.sql", "r") as file:
    sql_script = file.read()

for statement in sql_script.split(";"):
    if statement.strip():
        cursor.execute(statement)

db.commit()

cursor.execute("USE flowershop")


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=['POST'])
def register():

    username = request.form.get('username')
    phone = request.form.get('phone')

    sql = "INSERT INTO users (username, phone) VALUES (%s, %s)"
    values = (username, phone)

    cursor.execute(sql, values)

    return render_template("Success_register.html")


if __name__ == '__main__':
    app.run(debug=True)