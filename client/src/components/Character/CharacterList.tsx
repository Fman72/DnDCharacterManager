import React from 'react';
import { Character } from '../../types/api';
import { CharacterPane } from './CharacterPane';

interface CharacterListProps {
  characters: Character[];
}

const CharacterList = (props: CharacterListProps) => {
  const { characters } = props;

  return (
    <div>
      {characters.map((character) => <CharacterPane character={character}/>)}
    </div>
  );
}  