import React from 'react';
import { useQuery } from '@apollo/client';
import { loader } from 'graphql.macro';
import { Ability } from '../../../types/api'; 


interface SpellSearcherProps {
    classes: number[],
    render: (abilities: Ability[]) => React.ReactNode,
}

const getAbilitiesForClasses = loader('../../../apollo/queries/ability/getAbilitiesForClasses.gql');

export const AbilityRetriever = (props: SpellSearcherProps) => {
    const { classes, render } = props;
    const { data, error, loading } = useQuery(getAbilitiesForClasses, {
        variables: {
            classes
        },
        pollInterval: 0,
    });

    if (loading) {
        return <>'Loading'</>;
    }

    if (data) {
        const { allAbilitiesForClasses } = data;
        return (
            <>
                {render(allAbilitiesForClasses)}
            </>
        );
    }

    if (error) {
        console.log(error);
    }
    
    return <>Spell Searcher</>;
}
