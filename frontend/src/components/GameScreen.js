import React from 'react';
import CharacterPair from './CharacterPair';
import './GameScreen.css';

function GameScreen({ characters, roundInfo, remainingCount, roundTotalPlayers, onSelect, renderStageLabel }) {
  const renderVsInfo = () => {
    if (!roundTotalPlayers || roundTotalPlayers < 2) return null;
    const half = Math.floor(roundTotalPlayers / 2);
    return <h3>{half} vs {half}</h3>;
  };

  return (
    <div className="App">
      <div className="content-wrapper">
        <h1>Character Arena</h1>
        <h2>Round {roundInfo.round} - Match {roundInfo.match}</h2>
        {renderVsInfo()}
        {renderStageLabel()}
        <CharacterPair characters={characters} onSelect={onSelect} />
      </div>
    </div>
  );
}

export default GameScreen;