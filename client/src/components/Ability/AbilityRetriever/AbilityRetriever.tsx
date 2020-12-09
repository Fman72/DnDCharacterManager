import React from 'react';
import { useQuery } from '@apollo/client';
import { loader } from 'graphql.macro';
import { Ability } from '../../../types/api'; 


interface AllAbilitiesForClassesData {
  allAbilitiesForClasses: Ability[];
}

interface AllAbilitiesForClassesVars {
  classes: number[];
}

interface SpellSearcherProps {
    classes: number[],
    render: (abilities: Ability[]) => React.ReactNode,
}

const GET_ABILITIES_FOR_CLASSES_QUERY = loader('../queries/getAbilitiesForClasses.gql');

export const AbilityRetriever = (props: SpellSearcherProps) => {
    const { classes, render } = props;
    const { data, error, loading } = useQuery<AllAbilitiesForClassesData, AllAbilitiesForClassesVars>(GET_ABILITIES_FOR_CLASSES_QUERY, {
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
