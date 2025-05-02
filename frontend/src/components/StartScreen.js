import React from 'react';
import './StartScreen.css';

function StartScreen({ onStart }) {
  return (
    <div className="App">
      <h1>Character Arena</h1>
      <div className="instructions-box">
        <h3>How to Play:</h3>
        <p>
          You'll be shown 2 characters each round. Pick your favorite. Winner advances.
        </p>
        <button onClick={onStart}>Start</button>
      </div>
    </div>
  );
}

export default StartScreen;
