import React from 'react';
import { Ability } from '../../../types/api'; 
import { AbilityPane } from '../AbilityPane/AbilityPane';

interface AbilityListProps {
    abilities: Ability[],
}

export const AbilityList = (props: AbilityListProps) => {
    const { abilities } = props;
    const abilityPanes = abilities.map(ability => <AbilityPane ability={ability}/>);
    return (
        <div>
            {abilityPanes}
        </div>
    );
}