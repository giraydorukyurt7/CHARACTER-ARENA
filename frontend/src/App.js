import React, { useEffect, useState } from 'react';
import StartScreen from './components/StartScreen';
import SQLScreen from './components/SQLScreen';
import GameScreen from './components/GameScreen';
import WinnerScreen from './components/WinnerScreen';

function App() {
  const [gameStage, setGameStage] = useState(1); // 1=start, 2=sql, 3=game, 4=winner
  const [characters, setCharacters] = useState([]);
  const [loading, setLoading] = useState(true);
  const [roundInfo, setRoundInfo] = useState({ round: 1, match: 1 });
  const [remainingCount, setRemainingCount] = useState(null);
  const [roundTotalPlayers, setRoundTotalPlayers] = useState(null);
  const [winner, setWinner] = useState(null);

  useEffect(() => {
    document.body.style.background = "url('/background.jpg') no-repeat center center fixed";
    document.body.style.backgroundSize = "cover";    
    if (gameStage === 3) {
      fetch("http://127.0.0.1:5000/api/start_game", { method: "POST" })
        .then(res => res.json())
        .then(data => {
          if (data.round_total_players) {
            setRoundTotalPlayers(data.round_total_players);
          }
          fetchNextMatch();
        });
    }
  }, [gameStage]);

  const fetchNextMatch = () => {
    fetch("http://127.0.0.1:5000/api/next_match")
      .then(res => res.json())
      .then(data => {
        if (data.status === "game_over") {
          setWinner({
            name: data.winner[0],
            series: data.winner[1],
            age: data.winner[2],
            gender: data.winner[3],
            picture: data.winner[4]
          });
          setCharacters([]);
          setGameStage(4);
        } else if (data.status === "round_over") {
          alert("Round over. Advancing...");
          fetchNextMatch();
        } else {
          setCharacters(data);
          setLoading(false);
        }
      });
  };

  const handleSelect = (side) => {
    fetch("http://127.0.0.1:5000/api/selection", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ selected_character: side })
    })
      .then(res => res.json())
      .then(data => {
        if (data.status === "success") {
          setRoundInfo({ round: data.round, match: data.match });
          setRemainingCount(data.remaining);
          setRoundTotalPlayers(data.round_total_players);
        }
        fetchNextMatch();
      });
  };

  const handleRestart = () => {
    setWinner(null);
    setCharacters([]);
    setRoundInfo({ round: 1, match: 1 });
    setRemainingCount(null);
    setRoundTotalPlayers(null);
    setGameStage(1);
  };

  const renderStageLabel = () => {
    if (winner) return <h3>🏆 WINNER!</h3>;
    if (remainingCount === 8) return <h3>QUARTER FINALS</h3>;
    if (remainingCount === 4) return <h3>SEMI FINALS</h3>;
    if (remainingCount === 2) return <h3>FINALS</h3>;
    return null;
  };

  if (gameStage === 1) return <StartScreen onStart={() => setGameStage(2)} />;
  if (gameStage === 2) return <SQLScreen onApply={() => setGameStage(3)} />;
  if (gameStage === 3)
    return (
      <GameScreen
        characters={characters}
        roundInfo={roundInfo}
        remainingCount={remainingCount}
        roundTotalPlayers={roundTotalPlayers}
        onSelect={handleSelect}
        renderStageLabel={renderStageLabel}
      />
    );
  if (gameStage === 4 && winner)
    return <WinnerScreen winner={winner} onRestart={handleRestart} renderStageLabel={renderStageLabel} />;

  return null;
}

export default App;
