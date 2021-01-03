import React from 'react';
import { ConnectedAbilitySearcher } from '../../components/Ability/AbilitySearcher';
import { ConnectedLearnedAbilitiesList } from '../../components/Ability/LearnedAbilitiesList';


export const GamePage = () => {

    return <div>
        Game Page
        <ConnectedAbilitySearcher />
        <ConnectedLearnedAbilitiesList />
    </div>;
}