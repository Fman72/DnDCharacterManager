import { useMutation, MutationHookOptions, useReactiveVar, useLazyQuery, useQuery, MutationTuple, MutationResult } from '@apollo/client';
import { loader } from 'graphql.macro';
import { GameData } from '../../../types/userAuth'
import { useImperativeQuery } from '../../../apollo/useImperativeQuery';
import { gameDataVar } from '../../../apollo/cache';

const UPDATE_GAME_DATA_QUERY = loader('../queries/updateGameData.gql');
const GET_LOCAL_GAME_DATA_QUERY = loader('../queries/getLocalGameData.gql');

interface UpdateGameDataVariables {
  currentCharacter?: number;
  currentGameSession?: number;
}

type UpdateGameDataMethod = (currentGameSession?: number, currentCharacter?: number) => void;
type UpdateGameDataTuple = [UpdateGameDataMethod, MutationResult<GameData>];

// Update this to use reactive var to store game data not the apollo cache,.
export const useUpdateGameData = (options?: MutationHookOptions<GameData, UpdateGameDataVariables>): UpdateGameDataTuple => {
  const [updateGameDataRaw, result] = useMutation<GameData, UpdateGameDataVariables>(UPDATE_GAME_DATA_QUERY, options);
  const gameData = useReactiveVar(gameDataVar);

  const updateGameData = async (currentGameSession?: number, currentCharacter?: number) => {
    const variables: UpdateGameDataVariables = {
      currentGameSession,
      currentCharacter
    };
    if (gameData) {
      if (variables.currentCharacter === undefined && gameData?.currentCharacter) {
        variables.currentCharacter = gameData?.currentCharacter.id;
      }
      if (variables.currentGameSession === undefined && gameData?.currentGameSession) {
        variables.currentGameSession = gameData?.currentGameSession.id;
      }
  
      updateGameDataRaw({ variables })
    }
  }

  return [updateGameData, result];
};