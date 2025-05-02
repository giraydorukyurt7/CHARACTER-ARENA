import React from 'react';
import './SQLScreen.css';

function SQLScreen({ onApply }) {
  return (
    <div className="App">
      <h1>Character Arena - SQL Setup</h1>
      <button onClick={onApply}>APPLY</button>
    </div>
  );
}

export default SQLScreen;
