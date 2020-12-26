import { ReactiveVar, makeVar, InMemoryCache } from '@apollo/client';
import { GameData } from '../types/userAuth';

export const gameDataVar: ReactiveVar<GameData | null> = makeVar<GameData | null>(null);

const typePolicies = {
  Query: {
    fields: {
      localGameData: {
        read() {
          return gameDataVar();
        }
      }
    }
  }
};

export const cache =  new InMemoryCache({
  typePolicies
}); 