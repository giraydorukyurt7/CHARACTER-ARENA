import numpy as np
import math
import mysql.connector
from flask import Flask, jsonify
from flask_cors import CORS
from flask import request

app = Flask(__name__)
CORS(app)

#Global variables
latest_selection = None
game_characters  = []
winners          = []
round_index      = 0
match_index      = 0
round_start_count = 0

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



#flask tests

@app.route("/api/start_game", methods=["POST"])
def start_game():
    global game_characters, round_index, match_index, round_start_count

    data = request.get_json()
    selected_series = data.get("series", [])

    conn = mysql.connector.connect(
        host="localhost", user="root", password="2002g", database="character_arena"
    )
    cursor = conn.cursor(dictionary=True)
    format_strings = ','.join(['%s'] * len(selected_series))
    cursor.execute(
        f"SELECT name, series, age, gender, picture FROM characters WHERE series IN ({format_strings})",
        tuple(selected_series)
    )
    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    dtype = np.dtype([
        ('name', 'U100'), ('series', 'U100'),
        ('age', 'U10'), ('gender', 'U10'), ('picture', 'U255')
    ])
    arr = np.zeros(len(rows), dtype=dtype)
    for i, row in enumerate(rows):
        arr[i] = (row['name'], row['series'], row['age'], row['gender'], row['picture'])

    characters = remove_until_power_of_two(arr)
    np.random.shuffle(characters)
    game_characters = list(characters)

    round_index = 1
    match_index = 0
    round_start_count = len(game_characters)  # <-- EKLENDİ

    return jsonify({
        "status": "game_started",
        "round_total_players": round_start_count
    })




@app.route("/api/next_match")
def next_match():
    global game_characters, match_index
    if len(game_characters)==1:
        return jsonify({"status":"game_over",
                        "winner":game_characters[0].tolist()})
    #send pairs

    if match_index >= len(game_characters)-1:
        return jsonify({"status":"round_over"})
    


    pair = game_characters[match_index:match_index + 2]

    return jsonify([
        {
            "name"    : pair[0]["name"],
            "series"  : pair[0]["series"],
            "age"     : pair[0]["age"],
            "gender"  : pair[0]["gender"],
            "picture" : pair[0]["picture"]
        },
        {
            "name"    : pair[1]["name"],
            "series"  : pair[1]["series"],
            "age"     : pair[1]["age"],
            "gender"  : pair[1]["gender"],
            "picture" : pair[1]["picture"]
        }
    ])

#Get the answer
@app.route("/api/selection", methods=["POST"])
def handle_selection():
    global game_characters, winners, match_index, round_index, round_start_count

    data = request.get_json()
    selected = data.get("selected_character")

    if selected not in ("left", "right"):
        return jsonify({"status": "error", "message": "Invalid selection"}), 400

    if match_index >= len(game_characters) - 1:
        return jsonify({"status": "error", "message": "No more matches in this round"}), 400

    pair = game_characters[match_index:match_index + 2]
    winner = pair[0] if selected == "left" else pair[1]
    winners.append(winner)

    match_index += 2

    # round over
    if match_index >= len(game_characters):
        game_characters = winners
        winners = []
        match_index = 0
        round_index += 1
        round_start_count = len(game_characters)

    return jsonify({
        "status": "success",
        "remaining": len(game_characters),
        "round": round_index,
        "match": match_index // 2 + 1,
        "round_total_players": round_start_count
    }), 200



#Send 2 character
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

@app.route("/api/series")
def get_series():
    conn = mysql.connector.connect(
        host="localhost", user="root", password="2002g", database="character_arena"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT series FROM characters")
    results = [row[0] for row in cursor.fetchall()]
    cursor.close()
    conn.close()
    return jsonify(results)



if __name__ == "__main__":
    app.run(debug=True)