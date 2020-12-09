import react from "react";
import { loader } from 'graphql.macro';
import { useMutation } from '@apollo/client';
import { GameSession } from '../../../types/api';

const CREATE_GAME_SESSION_QUERY = loader('../queries/createGameSession.gql');

interface CreateGameSessionData {
  gameSession: GameSession;
}

interface CreateGameSessionButtonProps {
  onCompleted: (data: CreateGameSessionData) => void;
}


const CreateGameSessionButton = (props: CreateGameSessionButtonProps) => {
  
  const [ createGameSession, { data } ] = useMutation<
    { createGameSession: () => CreateGameSessionData },
    { gameSession: GameSession }
  >(CREATE_GAME_SESSION_QUERY);

  return (<button onClick={createGameSession}>Create Game Session</button>);
}