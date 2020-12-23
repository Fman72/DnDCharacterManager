import React from 'react';
import { Character } from "../../../types/api";

interface CharacterPaneProps {
  character: Character;
}

export const CharacterPane = (props: CharacterPaneProps) => {
  const { character } = props;
  return (
    <div>
      Character: {character.name}
    </div>
  );
}