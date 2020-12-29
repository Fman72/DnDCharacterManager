import React from 'react';
import { ConnectedCharacterList } from '../../components/Character/CharacterList';
import { useUpdateGameData } from '../../hooks/GameData/useUpdateGameData';
import { useHistory } from 'react-router-dom';
import { Paths } from '../../Router';

interface CharacterSelectProps {
  
}
 
export const CharacterSelectPage = (props: CharacterSelectProps) => {

  const [updateGameData] = useUpdateGameData();
  const history = useHistory();

  const generateOnCharacterSelect = (characterId: number) => async () => {
    await updateGameData(undefined, characterId);
    history.push(Paths.GAME)
  };
  
  return (
    <div>
      <ConnectedCharacterList generateOnCharacterSelect={generateOnCharacterSelect}/>
    </div>
  );
}