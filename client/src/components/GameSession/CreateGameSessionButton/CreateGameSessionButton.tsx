import React from "react";
import { loader } from 'graphql.macro';
import { useMutation } from '@apollo/client';
import { GameSession } from '../../../types/api';

const CREATE_GAME_SESSION_QUERY = loader('../queries/createGameSession.gql');

interface CreateGameSessionButtonProps {
  onCompleted: (data: GameSession) => void;
}


export const CreateGameSessionButton = (props: CreateGameSessionButtonProps) => {
  
  const { onCompleted } = props;

  const [ createGameSession, { data } ] = useMutation<
    { gameSession: GameSession }
  >(CREATE_GAME_SESSION_QUERY, {
    onCompleted({ gameSession }) {
      onCompleted(gameSession);
    }
  });

  const onClick = (e: React.MouseEvent<HTMLButtonElement>) => createGameSession();

  return (<button onClick={onClick}>Create Game Session</button>);
}