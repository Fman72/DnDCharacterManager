import { ReactiveVar, makeVar, InMemoryCache } from '@apollo/client';
import { GameData } from '../types/userAuth';
import { getToken } from '../api/token';

export const cache =  new InMemoryCache();

export const gameDataVar: ReactiveVar<GameData | null> = makeVar<GameData | null>(null);
export const isLoggedInVar: ReactiveVar<boolean> = makeVar<boolean>(!!getToken());