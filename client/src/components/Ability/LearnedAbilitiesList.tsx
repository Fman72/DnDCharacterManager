import { ApolloRetriever } from '../Core/ApolloRetriever'
import { loader } from 'graphql.macro';
import { AbilityList } from './AbilityList';
import { Ability } from '../../types/api';

const GET_LEARNED_ABILTIIES = loader('./queries/getLearnedAbilities.gql');

interface GetLearnedAbilitiesData {
  learnedAbilities: Ability[];
}

export const ConnectedLearnedAbilitiesList = () => {
  return <ApolloRetriever
    query={GET_LEARNED_ABILTIIES}
    render={(data: GetLearnedAbilitiesData) => <AbilityList abilities={data.learnedAbilities}/>}
  />;
}
