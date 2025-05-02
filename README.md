# 🎮 Character Arena

A dynamic tournament-style character battle game built with **React**, **Flask**, and **MySQL**.

![Character Arena Preview](preview.png) 

---

## ⚙️ Technologies Used

- 🔹 **Frontend**: React
- 🔹 **Backend**: Python (Flask)
- 🔹 **Database**: MySQL
- 🔹 **Image Search**: DuckDuckGo (script to download image data)

---

## 🚀 Getting Started

### 📁 1-Clone the Repository

```bash
git clone https://github.com/giraydorukyurt7/character-arena.git
cd character-arena
```

### 🔌 2-Start the Flask Backend

```bash
cd backend
python app.py
```

### 🌐 3-Start the React Frontend

```bash
cd frontend
npm install     # First time only
npm start
```

### 4-Visit:

http://localhost:3000


## 🧠 How It Works
* Start Screen: Read how to play and begin the game.

* SQL Screen: Select one or more series from the database.

* Game Screen: Vote on matchups, one by one.

* Winner Screen: See the final champion and restart.

Characters are pulled dynamically from a MySQL database and displayed in random pairings. The tournament continues until only one winner remains.


## 🖼️ Folder Structure
```bash
character-arena/
├── backend/            # Flask API (Python) - handles game logic and database interaction
│   └── app.py          # Main backend server
│
├── frontend/           # React app (user interface)
│   ├── public/         # Static assets served directly (HTML, favicon, images)
│   │   ├── background.jpg / no_photo.png / logo.png  # UI assets
│   │   └── images/     # Character images organized by series (e.g. /naruto, /cars, ...)
│   │
│   └── src/            # React source files
│       ├── App.js      # Main app logic and game state management
│       ├── App.css     # Global styles
│       ├── index.js    # Entry point
│       └── components/ # Modular React components for each screen
│           ├── CharacterPair.js / .css
│           ├── GameScreen.js / .css
│           ├── SQLScreen.js / .css
│           ├── StartScreen.js / .css
│           └── WinnerScreen.js / .css
│
├── database/           # MySQL scripts (you can store init.sql here)
│   └── init.sql        # Schema + character data (used to populate MySQL)
│
└── README.md           # Project overview and setup instructions

```

# 📌 Notes
* Ensure MySQL is running and credentials match your local setup.

* Tested in modern Google Chrome.

* Images are optional — a fallback (no_photo.png) is used if missing.

## 📫 Contact  
Built with 💻 by [Giray Doruk Yurtseven](https://www.linkedin.com/in/giraydorukyurt7/)  
🔗 [GitHub](https://github.com/giraydorukyurt7)  
🔗 [LinkedIn](https://www.linkedin.com/in/giraydorukyurt7/)
