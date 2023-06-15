from flask import Flask, jsonify, request

import mysql.connector as mysql
  
dataBase = mysql.connect(
  host ="localhost",
  user ="root",
  passwd ="",
  database="address"
)
cursor= dataBase.cursor()

 
app = Flask(__name__)

@app.route("/")
def home():
    return "Go to /place<id>"

@app.route("/place/<id>")
def get_place(id):
    cursor.execute("select * from data where id=%s",[id])
    data = cursor.fetchone()
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)

