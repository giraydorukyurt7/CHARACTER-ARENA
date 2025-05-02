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
import math
import mysql.connector
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


#random_characters = [
#    {"name": "Optimus Prime", "series": "Transformers", "age": "adult", "gender": "male", "picture": "path/to/optimus.jpg"},
#    {"name": "Naruto", "series": "Naruto", "age": "teen", "gender": "male", "picture": "path/to/naruto.jpg"},
#    {"name": "Heisenberg", "series": "Breaking Bad", "age": "adult", "gender": "male", "picture": "path/to/heisenberg.jpg"},
#    {"name": "John Wick", "series": "John Wick", "age": "adult", "gender": "male", "picture": "path/to/johnwick.jpg"},
#    {"name": "Wall-E", "series": "Wall-E", "age": "other", "gender": "other", "picture": "path/to/walle.jpg"},
#    {"name": "Lightning McQueen", "series": "Cars", "age": "adult", "gender": "male", "picture": "path/to/mcqueen.jpg"},
#    {"name": "Hatsune Miku", "series": "Vocaloid", "age": "teen", "gender": "female", "picture": "path/to/miku.jpg"},
#    {"name": "Gon", "series": "Hunter x Hunter", "age": "kid", "gender": "male", "picture": "path/to/gon.jpg"}
#]



#SQL Connection
def get_characters_array():
    #Connection:
    conn = mysql.connector.connect(host = "localhost",
                                   user="root",
                                   password="2002g",
                                   database="character_arena")
    cursor = conn.cursor(dictionary=True)

    #Select all characters
    cursor.execute("SELECT name, series, age, gender, picture FROM characters")
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    #Define dtype for Numpy
    dtype = np.dtype([('name',    'U100'),
                      ('series',  'U100'),
                      ('age',     'U10'),
                      ('gender',  'U10'),
                      ('picture', 'U255')])

    #Create structured array
    arr = np.zeros(len(rows), dtype=dtype)
    for i, row in enumerate(rows):
        arr[i] = (row['name'],
                  row['series'],
                  row['age'],
                  row['gender'],
                  row['picture'])
    return arr



def print_list(listname):
    for i in range(len(listname)):
        print("index:%d, list:%s" % (i, listname[i]))

def is_power_of_two(n):
    if n<=0:
        print("Number of characters are not power of two")
        return False
    log_value=math.log2(n)
    if log_value.is_integer():
        print("Number of characters are power of two")
        return True
    else:
        print("Number of characters are not power of two")
        return False

def remove_until_power_of_two(listname):
    np.random.shuffle(listname)
    number_of_elements_to_remove = 0
    if not is_power_of_two(len(listname)):
        number_of_elements_to_remove = len(listname) - 2**math.floor(math.log2(len(listname)))
        print("Length of the list is %d, Removing %d elements to make it power of two" % (len(listname),number_of_elements_to_remove))
        listname = listname[:-number_of_elements_to_remove]
    return listname

#
#random_characters = get_characters_array()
#print_list(random_characters)
#
#print("Number of Characters is: %d\n" % len(random_characters))
#
#random_characters = remove_until_power_of_two(random_characters)
#    
#round_ = 0
#while not len(random_characters)==1:
#    np.random.shuffle(random_characters)
#
#    print("The Character List:\n")
#    print_list(random_characters)
#    new_character_list = []
#
#    round_+=1
#    match_=0
#    for index in range(0,len(random_characters),2):
#        match_+=1
#        print("====================")
#        print("ROUND %d - Match %d" %(round_, match_))
#        print("====================")
#    
#        print("\nSelect the best character:")
#        print(f"        {random_characters[index]["name"]} or {random_characters[index+1]["name"]}")
#        print(f"Series: {random_characters[index]["series"]} | {random_characters[index+1]["series"]}")
#        print(f"Age:    {random_characters[index]["age"]} | {random_characters[index+1]["age"]}")
#        print(f"Gender: {random_characters[index]["gender"]} | {random_characters[index+1]["gender"]}")
#        print(f"Picture:{random_characters[index]["picture"]} | {random_characters[index+1]["picture"]}")
#        choice = input("\nEnter left or right: ")
#        while not (choice=="left" or choice=="right"):
#            print("Invalid Input")
#            choice = input("Enter left or right: ")
#        if choice == "left":
#            new_character_list.append(random_characters[index])
#        else:
#            new_character_list.append(random_characters[index+1])
#        print("---------------------------------------")
#    random_characters = new_character_list
#    
#    
#print("==========The WINNER!!!==========")
#
#print(f"        {random_characters[0]["name"]}")
#print(f"Series: {random_characters[0]["series"]}")
#print(f"Age:    {random_characters[0]["age"]}")
#print(f"Gender: {random_characters[0]["gender"]}") 
#print(f"Picture:{random_characters[0]["picture"]}")


#flask tests

@app.route("/api/characters")
def characters_api():
    characters_array = get_characters_array()
    
    characters_list = []
    for row in characters_array[:2]:
        character_dict = {
            "name"    : row["name"],
            "series"  : row["series"],
            "age"     : row["age"],
            "gender"  : row["gender"],
            "picture" : row["picture"]
        }
        characters_list.append(character_dict)
    return jsonify(characters_list)

if __name__ == "__main__":
    app.run(debug=True)