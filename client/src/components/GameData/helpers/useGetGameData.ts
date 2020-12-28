import { useLazyQuery, QueryTuple, QueryHookOptions } from '@apollo/client';
import { loader } from 'graphql.macro';
import { GameData } from '../../../types/userAuth'
import { gameDataVar } from '../../../apollo/cache';

const GET_GAME_DATA_QUERY = loader('../queries/getGameData.gql');

export const useGetGameData = (options?: QueryHookOptions<GameData>): QueryTuple<GameData, {}> => {
  
  const onCompleted = (data: any) => {
    if (data) {
      const { gameData } = data;
      gameDataVar(gameData);
    }
    if (options?.onCompleted) {
      options?.onCompleted(data);
    }
  }

  const [getGameData, result] = useLazyQuery<GameData>(GET_GAME_DATA_QUERY, {
    ...options,
    onCompleted
  });

  return [getGameData, result];
};