import React, { useState } from 'react';
import { Ability } from '../../types/api';
import { ApolloRetriever } from '../Core/ApolloRetriever';
import { loader } from 'graphql.macro';
import { useAbilitySearch } from '../../hooks/Ability/useAbilitySearch';

const GET_ALL_ABILTIIES = loader('./queries/getAllAbilities.gql');

interface ConnectedAbilitySearcherProps {
  refetch?: () => void;
}

interface AbilitySearcherProps extends ConnectedAbilitySearcherProps {
  abilities: Ability[];
}

export interface GetAllAbilitiesData {
  allAbilities: Ability[];
}

export const ConnectedAbilitySearcher = (props: ConnectedAbilitySearcherProps) => {
  return <ApolloRetriever 
    query={GET_ALL_ABILTIIES}
    render={((data: GetAllAbilitiesData) => <AbilitySearcher abilities={data.allAbilities} {...props}/>)}
  />
}

export const AbilitySearcher = (props: AbilitySearcherProps) => {
  const { abilities, refetch } = props;
  const [results, setResults] = useState<Ability[]>([]);
  const search = useAbilitySearch(abilities, {
    keys: ['name'],
    minMatchCharLength: 2,
  });


  const onChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    const searchTerm = event.target.value;
    const results = search(searchTerm);
    setResults(results);
  }

  return (
    <>
      <input onChange={onChange} />
      <div>{JSON.stringify(results)}</div>
    </>
  );
}