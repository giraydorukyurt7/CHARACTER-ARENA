import React from 'react';
import './SQLScreen.css';

function SQLScreen({ onApply }) {
  return (
    <div className="App">
      <div className="content-wrapper">
        <h1>Character Arena - SQL Setup</h1>
        <button onClick={onApply}>APPLY</button>
      </div>
    </div>
  );
}

export default SQLScreen;
