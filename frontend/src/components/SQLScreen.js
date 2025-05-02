import React, { useState, useEffect } from 'react';
import './SQLScreen.css';

function SQLScreen({ onApply }) {
  const [seriesList, setSeriesList] = useState([]);
  const [selectedSeries, setSelectedSeries] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:5000/api/series")
      .then(res => res.json())
      .then(data => setSeriesList(data));
  }, []);

  const toggleSeries = (series) => {
    setSelectedSeries(prev =>
      prev.includes(series)
        ? prev.filter(s => s !== series)
        : [...prev, series]
    );
  };

  const handleApply = () => {
    if (selectedSeries.length > 0) {
      onApply(selectedSeries);
    } else {
      alert("Please select at least one series.");
    }
  };

  return (
    <div className="App">
      <div className="content-wrapper">
        <h1>Character Arena - SQL Setup</h1>
        <h3>Select Series:</h3>
        {seriesList.map((series, i) => (
          <div key={i}>
            <label>
              <input
                type="checkbox"
                checked={selectedSeries.includes(series)}
                onChange={() => toggleSeries(series)}
              />
              {series}
            </label>
          </div>
        ))}
        <br />
        <button onClick={handleApply}>APPLY</button>
      </div>
    </div>
  );
}

export default SQLScreen;
