import React from 'react';
import { CreateGameSessionButton } from '../../components/GameSession/CreateGameSessionButton/CreateGameSessionButton';


export default () => {
    return <div>
        Game Session Page
        <CreateGameSessionButton onCompleted={(data) => null}/>
    </div>;
}