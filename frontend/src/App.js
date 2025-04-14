import React, { useEffect, useState } from 'react';

function App() {
  const [characters, setCharacters] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch('http://127.0.0.1:5000/characters') // Flask endpoint'ine istek gönder
      .then((response) => {
        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }
        return response.json();
      })
      .then((data) => setCharacters(data))
      .catch((err) => {
        console.error('Error fetching characters:', err);
        setError(err.message);
      });
  }, []);

  return (
    <div style={{ backgroundColor: 'pink', fontFamily: 'Arial, sans-serif', padding: '20px' }}>
      <h1>Character List</h1>
      {error ? (
        <p style={{ color: 'red' }}>Failed to fetch data: {error}</p>
      ) : characters.length > 0 ? (
        <ul>
          {characters.map((character) => (
            <li key={character.id}>
              <h3>{character.name}</h3>
              <p>Series: {character.series}</p>
              {character.image_url && (
                <img
                  src={character.image_url}
                  alt={`${character.name}`}
                  style={{ maxWidth: '200px', borderRadius: '5px' }}
                />
              )}
            </li>
          ))}
        </ul>
      ) : (
        <p>No characters available or still loading...</p>
      )}
    </div>
  );
}

export default App;
