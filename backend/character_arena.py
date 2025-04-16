#from flask import Flask, jsonify, send_from_directory
#from flask_cors import CORS
#import mysql.connector
#import os
#
#app = Flask(__name__, static_folder="../frontend/build", static_url_path="/")
#CORS(app)
#
## Veritabanı bağlantısı
#db = mysql.connector.connect(
#    host="localhost",
#    user="root",
#    password="2002",
#    database="fandom_game"
#)
#
#@app.route('/characters')
#def get_characters():
#    cursor = db.cursor(dictionary=True)
#    cursor.execute("SELECT * FROM characters")
#    results = cursor.fetchall()
#    return jsonify(results)
#
## React'in ana dosyasını servis etme
#@app.route('/')
#def serve_react_app():
#    return send_from_directory(app.static_folder, 'index.html')
#
## Flask'ın diğer React dosyalarını servis etmesi için
#@app.route('/<path:path>')
#def serve_static_files(path):
#    return send_from_directory(app.static_folder, path)
#
#if __name__ == '__main__':
#    app.run(debug=True)


# Testing character randomizer:

import numpy as np

#random_characters = np.arange(0,128)

random_characters = np.array([f"character{i}" for i in range(128)])

print("Original List:")
print(random_characters)

np.random.shuffle(random_characters)

print("Random Suffle:")

print(random_characters)

random_index = np.random.randint(0,128)

print(random_index)


random_numbers = np.random.choice(np.arange(0, 128), size=2, replace=False)
print(random_numbers)



a = input("Enter left or right: ")
while not (a=="left" or a=="right"):
    print("Invalid Input")
    a = input("Enter left or right: ")
    
print(a)