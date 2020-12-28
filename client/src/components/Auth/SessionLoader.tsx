import { getToken } from '../../api/token';
import { isLoggedInVar, gameDataVar } from '../../apollo/cache';
import { useGetGameData } from '../GameData/helpers/useGetGameData';
import { useReactiveVar } from '@apollo/client';
import React, { useEffect } from 'react';

export const SessionLoader = () => {

  const [getGameData, meta] = useGetGameData();
  const gameData = useReactiveVar(gameDataVar);
  const isLoggedIn = useReactiveVar(isLoggedInVar);

  useEffect(() => {
    const token = getToken();

    if (!token && isLoggedIn) {
      isLoggedInVar(false);
    } else if (!gameData) {
      getGameData();
    }
  }, [gameData, isLoggedIn]);

  return <></>;
}