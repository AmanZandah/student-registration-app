import os
import mysql.connector
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for

load_dotenv()  # load DB credentials from the .env file

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

@app.route("/")
def home():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id, name, email, phone, course FROM students ORDER BY id DESC")
    students = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template("index.html", students=students)

@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    phone = request.form.get("phone", "").strip()
    course = request.form.get("course", "").strip()

    if not name or not email or not phone or not course:
        return "All fields are required. Go back and complete the form.", 400

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO students (name, email, phone, course) VALUES (%s, %s, %s, %s)",
        (name, email, phone, course)
    )
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)