import React, { memo } from 'react';
import { Character } from "../../types/api";

interface CharacterPaneProps {
  character: Character;
  onCharacterSelect: () => void;
}

export const CharacterPane = memo((props: CharacterPaneProps) => {
  const { character, onCharacterSelect } = props;
  return (
    <div onClick={onCharacterSelect}>
      Character: {character.name}
    </div>
  );
}, (nextProps, prevProps) => nextProps.character.id === prevProps.character.id);