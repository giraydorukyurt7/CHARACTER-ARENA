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

#########################################################################################################
import numpy as np

#random_characters = np.arange(0,128)

#random_characters = np.array([f"character{i}" for i in range(8)])
random_characters = ["Optimus Prime", "Naruto", "Heisenberg", "John Wick",
                     "Wall-E", "Lightning MCQuenn","Hatsune Miku", "Gon"]
#name,series, age(baby,kid,teen,adult,elder,other), Gender(female,male,other), Picture

#print("Original List:")
#print(random_characters)



#random_index = np.random.randint(0,128)
#
#print(random_index)


#random_numbers = np.random.choice(np.arange(0, 128), size=2, replace=False)
#print(random_numbers)

print("Number of Characters is: %d\n" % len(random_characters))

while not len(random_characters)==1:
    np.random.shuffle(random_characters)
    print("Random Suffle:")
    print(random_characters)
    
    new_character_list = []
    for index in range(0,len(random_characters),2):
        print(f"{random_characters[index]} or {random_characters[index+1]}")
        choice = input("Enter left or right: ")
        while not (choice=="left" or choice=="right"):
            print("Invalid Input")
            choice = input("Enter left or right: ")
        if choice == "left":
            new_character_list.append(random_characters[index])
        else:
            new_character_list.append(random_characters[index+1])
        #print("index:%d, list:%s" % (index, new_character_list))
    random_characters = new_character_list
    
    
print("The winner is:")
print(random_characters)