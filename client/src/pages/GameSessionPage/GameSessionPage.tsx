import React from 'react';
import { useHistory } from 'react-router-dom';
import { CreateGameSessionButton } from '../../components/GameSession/CreateGameSessionButton';
import { useUpdateGameData } from '../../components/GameData/helpers/useUpdateGameData';
import { GameSession } from '../../types/api';
import { Paths } from '../../Router';


export const GameSessionPage = () => {
    const history = useHistory();
    const [updateGameData] = useUpdateGameData();

    const onCompleted = async (gameSession: GameSession) => {
      await updateGameData(gameSession.id);
      history.push(Paths.CHARACTER_SELECT_PAGE);
    }

    return <div>
        Game Session Page
        <CreateGameSessionButton onCompleted={(data: GameSession) => onCompleted(data)}/>
    </div>;
}