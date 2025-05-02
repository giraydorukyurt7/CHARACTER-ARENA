import React, { useEffect, useState } from 'react';
import CharacterPair from './CharacterPair';

function App(){
  const [characters, setCharacters] = useState([]);
  const [loading, setLoading]       = useState(true);
  const [roundInfo, setRoundInfo]   = useState({ round: 1, match: 1 });
  const [remainingCount, setRemainingCount] = useState(null);
  const [roundTotalPlayers, setRoundTotalPlayers] = useState(null);

  const fetchNextMatch = () => {
    fetch("http://127.0.0.1:5000/api/next_match")
      .then((response) => response.json())
      .then((data) => {
        if (data.status === "game_over") {
          alert(`The winner is: ${data.winner[0]}`);
          setCharacters([]);
        } else if (data.status === "round_over") {
          alert("Round is over, new matches are loading...");
          fetchNextMatch();
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
      .then((response) => response.json())
      .then((data) => {
        if (data.round_total_players) {
          setRoundTotalPlayers(data.round_total_players);
        }
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
        if (data.status === "success") {
          setRoundInfo({ round: data.round, match: data.match });
          setRemainingCount(data.remaining);
          setRoundTotalPlayers(data.round_total_players);
        }
        fetchNextMatch();
      });
  };
  

  const renderStageLabel = () => {
    if (remainingCount === 8) return <h3>QUARTER FINALS</h3>;
    if (remainingCount === 4) return <h3>SEMI FINALS</h3>;
    if (remainingCount === 2) return <h3>FINALS</h3>;
    return null;
  };
  

  const renderVsInfo = () => {
    if (!roundTotalPlayers || roundTotalPlayers < 2) return null;
    const half = Math.floor(roundTotalPlayers / 2);
    return <h3>{half} vs {half}</h3>;
  };
  

  if (loading || characters.length < 2){
    return(
      <div className='App'>
        <h1>Character Arena</h1>
        <div>Loading...</div>
      </div>
    );
  }

  return(
    <div className='App'>
      <h1>Character Arena</h1>
      <h2>Round {roundInfo.round} - Match {roundInfo.match}</h2>
      {renderVsInfo()}
      {renderStageLabel()}
      <CharacterPair characters={characters} onSelect={handleSelect}/>
    </div>
  );
}

export default App;
