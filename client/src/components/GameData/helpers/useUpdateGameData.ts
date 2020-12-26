import { useMutation, MutationHookOptions, useReactiveVar, useLazyQuery, useQuery } from '@apollo/client';
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

// Update this to use reactive var to store game data not the apollo cache,.
export const useUpdateGameData = (options?: MutationHookOptions<GameData, UpdateGameDataVariables>) => {
  const [updateGameDataRaw] = useMutation<GameData, UpdateGameDataVariables>(UPDATE_GAME_DATA_QUERY, options);
  const getLocalGameData = useImperativeQuery(GET_LOCAL_GAME_DATA_QUERY);
  const dataString = localStorage.getItem('GAMEDATA');
  let data: GameData | null = null;
  if (dataString) {
    data = JSON.parse(dataString).gameData;
  }

  const updateGameData = async (currentGameSession?: number, currentCharacter?: number) => {
    const variables: UpdateGameDataVariables = {
      currentGameSession,
      currentCharacter
    };
    if (data) {
      if (variables.currentCharacter === undefined && data?.currentCharacter) {
        variables.currentCharacter = data?.currentCharacter.id;
      }
      if (variables.currentGameSession === undefined && data?.currentGameSession) {
        variables.currentGameSession = data?.currentGameSession.id;
      }
  
      updateGameDataRaw({ variables })
    }
  }

  return { updateGameData };
};