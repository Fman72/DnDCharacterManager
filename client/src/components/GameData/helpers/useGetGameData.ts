import { useLazyQuery, QueryTuple, QueryHookOptions } from '@apollo/client';
import { loader } from 'graphql.macro';
import { GameData } from '../../../types/userAuth'
import { gameDataVar } from '../../../apollo/cache';

const GET_GAME_DATA_QUERY = loader('../queries/getGameData.gql');

export const useGetGameData = (options?: QueryHookOptions<GameData>): QueryTuple<GameData, {}> => {
  
  const onCompleted = (data: GameData) => {
    if (data) {
      localStorage.setItem('GAMEDATA', JSON.stringify(data));
      // This doesn't work so I'm using localStorage.
      gameDataVar(data);
    }
    if (options?.onCompleted) {
      options?.onCompleted(data);
    }
  }

  const [getGameData, meta] = useLazyQuery<GameData>(GET_GAME_DATA_QUERY, {
    ...options,
    onCompleted
  });

  return [getGameData, meta];
};