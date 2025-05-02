import React from "react";
import './CharacterPair.css';

const CharacterCard = ({character, side, onSelect}) => (
    <div style={{textAlign:"center"}}>
        <h2>{character.name}</h2>
        <p>Series: {character.series}</p>
        <p>Age: {character.age}</p>
        <p>Gender: {character.gender}</p>
        <img src={character.picture} alt={character.name} width="150"/>
        <br/>
        <button onClick={() =>onSelect(side)}>Select {side}</button>
    </div>
);


const CharacterPair = ({ characters, onSelect }) => {
    if (!characters || characters.length < 2 || !characters[0] || !characters[1]) {
      return <div>Loading match...</div>;
    }
  
    return (
      <div className="character-pair-container">
        <CharacterCard character={characters[0]} side="left" onSelect={onSelect} />
        <CharacterCard character={characters[1]} side="right" onSelect={onSelect} />
      </div>
    );
  };
  

export default CharacterPair;