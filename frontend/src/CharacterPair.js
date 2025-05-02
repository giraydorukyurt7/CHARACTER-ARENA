import React from "react";
import './CharacterPair.css';

function CharacterPair({characters}){
    if(characters.length<2)
        return <div>Unsufficient amount of characters</div>

    const [left, right] = characters;

    return( 
    <div className="character-pair-container">
        <div className="character-card">
            <h2>{left.name}</h2>
            <p>Series: {left.series}</p>
            <p>Age: {left.age}</p>
            <p>Gender: {left.gender}</p>
            <img src={left.picture} alt={left.name} width="100"/>
        </div>
        <div className="character-card">
            <h2>{right.name}</h2>
            <p>Series: {right.series}</p>
            <p>Age: {right.age}</p>
            <p>Gender: {right.gender}</p>
            <img src={right.picture} alt={right.name} width="100"/>
        </div>        
    </div>
    );
}

export default CharacterPair;