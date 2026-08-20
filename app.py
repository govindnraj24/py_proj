from os import name

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""

    if request.method == "POST":
        name = request.form["name"]
        age = request.form["age"]

        result = f"Welcome {name}! You are {age} years old."

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

#connect to MSSSQL server
'''
import pyodbc

connection = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=192.168.1.4;'
    'DATABASE=MSSQL;'
    'UID=sa;'
    'PWD=Success@2026'
)
# not configured yet to check
'''


