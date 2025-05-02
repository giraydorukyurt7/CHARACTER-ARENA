import React from 'react';
import './WinnerScreen.css';

function WinnerScreen({ winner, onRestart, renderStageLabel }) {
  return (
    <div className="App">
      <div className="overlay-container">
        <h1>Character Arena</h1>
        {renderStageLabel()}
        <div className="winner-card">
          <div className="winner-card-content">
            <h2>{winner.name}</h2>
            <p>Series: {winner.series}</p>
            <p>Age: {winner.age}</p>
            <p>Gender: {winner.gender}</p>
            <img
              src={winner.picture}
              alt={winner.name}
              width="200"
              onError={(e) => (e.target.src = "/no_photo.png")}
            />
          </div>
        </div>
        <button onClick={onRestart} style={{ marginTop: '1rem' }}>
          Play Again
        </button>
      </div>
    </div>
  );
}

export default WinnerScreen;
