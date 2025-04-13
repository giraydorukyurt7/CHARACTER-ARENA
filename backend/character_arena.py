from flask import Flask, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

# Veritabanı bağlantısı
db = mysql.connector.connect(
    host="localhost",
    user="root",           
    password="",           
    database="fandom_game"
)

@app.route('/characters')
def get_characters():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM characters")
    results = cursor.fetchall()
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
