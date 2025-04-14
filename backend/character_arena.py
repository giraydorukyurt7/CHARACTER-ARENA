from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import mysql.connector
import os

app = Flask(__name__, static_folder="../frontend/build", static_url_path="/")
CORS(app)

# Veritabanı bağlantısı
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="2002",
    database="fandom_game"
)

@app.route('/characters')
def get_characters():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM characters")
    results = cursor.fetchall()
    return jsonify(results)

# React'in ana dosyasını servis etme
@app.route('/')
def serve_react_app():
    return send_from_directory(app.static_folder, 'index.html')

# Flask'ın diğer React dosyalarını servis etmesi için
@app.route('/<path:path>')
def serve_static_files(path):
    return send_from_directory(app.static_folder, path)

if __name__ == '__main__':
    app.run(debug=True)
