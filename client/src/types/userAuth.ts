import { Character, GameSession } from './api';

export interface GameData {
  currentCharacter: Character;
  currentGameSession: GameSession;
}