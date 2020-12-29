import React from 'react';
import { Character } from '../../types/api';
import { CharacterPane } from './CharacterPane';
import { ApolloRetriever } from '../Core/ApolloRetriever';
import { loader } from 'graphql.macro';

const GET_CHARACTERS_QUERY = loader('./queries/getCharacters.gql');

interface ConnectedCharacterListProps {
  generateOnCharacterSelect: (characterId: number) => () => void; 
}

interface CharacterListProps extends ConnectedCharacterListProps {
  characters: Character[];
}

export const CharacterList = (props: CharacterListProps) => {
  const { characters, generateOnCharacterSelect } = props;

  return (
    <div>
      {characters.map((character) => <CharacterPane onCharacterSelect={(generateOnCharacterSelect(character.id))} character={character}/>)}
    </div>
  );
}

interface CharacterListData {
  usersCharacters: Character[];
}

export const ConnectedCharacterList = (props: ConnectedCharacterListProps) => {
  return <ApolloRetriever<CharacterListData, undefined>
    query={GET_CHARACTERS_QUERY}
    render={(data: CharacterListData) => <CharacterList characters={data.usersCharacters} {...props}/>}
  />
}