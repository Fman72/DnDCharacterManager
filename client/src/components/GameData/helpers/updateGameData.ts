import { useMutation, MutationHookOptions } from '@apollo/client';
import { loader } from 'graphql.macro';
import { GameData } from '../../../types/userAuth'
import { client } from '../../../apollo/client';

const UPDATE_GAME_DATA_QUERY = loader('../queries/updateGameData.gql');
const GET_GAME_DATA_QUERY = loader('../queries/getGameData.gql');

interface UpdateGameDataVariables {
  currentCharacter: number;
  currentGameSession: number;
}

const updateGameData = (currentGameSession: number, currentCharacter: number, options?: MutationHookOptions<UpdateGameDataVariables, GameData>) => {
  const gameData = client.readQuery<GameData, GameData>({query: GET_GAME_DATA_QUERY});
  
  const [updateGameData, { data }] = useMutation<UpdateGameDataVariables, GameData>(UPDATE_GAME_DATA_QUERY, options);
  return [updateGameData, data];
};