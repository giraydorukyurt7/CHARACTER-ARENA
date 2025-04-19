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

random_characters = [
    {"name": "Optimus Prime", "series": "Transformers", "age": "adult", "gender": "male", "picture": "path/to/optimus.jpg"},
    {"name": "Naruto", "series": "Naruto", "age": "teen", "gender": "male", "picture": "path/to/naruto.jpg"},
    {"name": "Heisenberg", "series": "Breaking Bad", "age": "adult", "gender": "male", "picture": "path/to/heisenberg.jpg"},
    {"name": "John Wick", "series": "John Wick", "age": "adult", "gender": "male", "picture": "path/to/johnwick.jpg"},
    {"name": "Wall-E", "series": "Wall-E", "age": "other", "gender": "other", "picture": "path/to/walle.jpg"},
    {"name": "Lightning McQueen", "series": "Cars", "age": "adult", "gender": "male", "picture": "path/to/mcqueen.jpg"},
    {"name": "Hatsune Miku", "series": "Vocaloid", "age": "teen", "gender": "female", "picture": "path/to/miku.jpg"},
    {"name": "Gon", "series": "Hunter x Hunter", "age": "kid", "gender": "male", "picture": "path/to/gon.jpg"}
]

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

    #TODO
    #add if else block to save it into next round if character quantity is not power of 2


    i = 1
    print("====================")
    print("ROUND %d" %i)
    print("====================")
    for index in range(0,len(random_characters),2):
        print("\nSelect the best character:")
        print(f"        {random_characters[index]["name"]} or {random_characters[index+1]["name"]}")
        print(f"Series: {random_characters[index]["series"]} | {random_characters[index+1]["series"]}")
        print(f"Age:    {random_characters[index]["age"]} | {random_characters[index+1]["age"]}")
        print(f"Gender: {random_characters[index]["gender"]} | {random_characters[index+1]["gender"]}")
        print(f"Picture:{random_characters[index]["picture"]} | {random_characters[index+1]["picture"]}")
        choice = input("\nEnter left or right: ")
        while not (choice=="left" or choice=="right"):
            print("Invalid Input")
            choice = input("Enter left or right: ")
        if choice == "left":
            new_character_list.append(random_characters[index])
        else:
            new_character_list.append(random_characters[index+1])
        #print("index:%d, list:%s" % (index, new_character_list))
        print("---------------------------------------")
    random_characters = new_character_list
    
    
print("==========The WINNER!!!==========")

print(f"        {random_characters[index]["name"]}")
print(f"Series: {random_characters[index]["series"]}")
print(f"Age:    {random_characters[index]["age"]}")
print(f"Gender: {random_characters[index]["gender"]}") 
print(f"Picture:{random_characters[index]["picture"]}")