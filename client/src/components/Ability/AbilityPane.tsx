import React from 'react';
import { Ability } from '../../types/api'; 

interface AbilityPaneProps {
    ability: Ability,
}

export const AbilityPane = (props: AbilityPaneProps) => {
    const { ability } = props;
    const { name } = ability;
    return (
        <div>
            { name }
        </div>
    );
}