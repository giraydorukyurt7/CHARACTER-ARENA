import React, { useEffect, useState } from 'react';
import CharacterPair from './CharacterPair';

function App(){
  const [characters, setCharacters] = useState([])

  useEffect(()=>{
    fetch('http://127.0.0.1:5000/api/characters')
      .then((response)=>response.json())
      .then((data)=>setCharacters(data))
      .catch((error)=> console.error('API Error: ', error));
  }, []);

  return(
    <div className='App'>
      <h1>Character Arena</h1>
      <CharacterPair characters={characters}/>
    </div>
  );

}
export default App;
