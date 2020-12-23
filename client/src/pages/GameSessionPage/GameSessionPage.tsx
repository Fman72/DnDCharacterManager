import React from 'react';
import { CreateGameSessionButton } from '../../components/GameSession/CreateGameSessionButton/CreateGameSessionButton';
import { useUpdateGameData } from '../../components/GameData/helpers/useUpdateGameData';
import { GameSession } from '../../types/api';


export default () => {
    const { updateGameData } = useUpdateGameData();
    return <div>
        Game Session Page
        <CreateGameSessionButton onCompleted={(data: GameSession) => updateGameData(data.id)}/>
    </div>;
}