import React, { useEffect, useState } from 'react';
import CharacterPair from './CharacterPair';

function App(){
  const [characters, setCharacters] = useState([]);
  const [loading, setLoading]       = useState(true);

  const fetchNextMatch = () => {
    fetch("http://127.0.0.1:5000/api/next_match")
      .then((response) => response.json())
      .then((data) => {
        if (data.status === "game_over") {
          alert(`Kazanan: ${data.winner[0]}`);
          setCharacters([]);
        } else if (data.status === "round_over") {
          alert("Round bitti, yeni eşleşmeler geliyor...");
          fetchNextMatch(); // hemen yeni eşleşmeye geç
        } else {
          setCharacters(data);
          setLoading(false);
        }
      })
      .catch((error) => console.error("API Error: ", error));
  };
  

  useEffect(() => {
    fetch("http://127.0.0.1:5000/api/start_game", {
      method: "POST",
    })
      .then(() => {
        fetchNextMatch();
      });
  }, []);
  

  const handleSelect = (side) => {
    fetch("http://127.0.0.1:5000/api/selection", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ selected_character: side }),
    })
      .then((response) => response.json())
      .then((data) => {
        console.log("Server response:", data);
        fetchNextMatch(); // get new pair
      });
  };
  

  if (loading || characters.length < 2){
    return(
      <div className='App'>
        <h1>Character Arena</h1>
        <div>Loading...</div>
      </div>
    )
  }

  return(
    <div className='App'>
      <h1>Character Arena</h1>
      <CharacterPair characters={characters} onSelect={handleSelect}/>
    </div>
  );
}

export default App;
