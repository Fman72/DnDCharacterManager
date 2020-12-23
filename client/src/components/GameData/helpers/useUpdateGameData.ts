import { useMutation, MutationHookOptions } from '@apollo/client';
import { loader } from 'graphql.macro';
import { GameData } from '../../../types/userAuth'
import { client } from '../../../apollo/client';

const UPDATE_GAME_DATA_QUERY = loader('../queries/updateGameData.gql');
const GET_GAME_DATA_QUERY = loader('../queries/getGameData.gql');

interface UpdateGameDataVariables {
  currentCharacter?: number;
  currentGameSession?: number;
}

export const useUpdateGameData = (options?: MutationHookOptions<GameData, UpdateGameDataVariables>) => {
  const gameData = client.readQuery<GameData, GameData>({query: GET_GAME_DATA_QUERY});
  const [updateGameDataRaw, { data }] = useMutation<GameData, UpdateGameDataVariables>(UPDATE_GAME_DATA_QUERY, options);
  const updateGameData = (currentGameSession?: number, currentCharacter?: number) => {
    
    const variables: UpdateGameDataVariables = {
      currentGameSession,
      currentCharacter
    };
    if (variables.currentCharacter === undefined) {
      variables.currentCharacter = gameData?.currentCharacter.id;
    }
    if (variables.currentGameSession === undefined) {
      variables.currentGameSession = gameData?.currentGameSession.id;
    }

    updateGameDataRaw({ variables })
    
  }

  return { updateGameData };
};