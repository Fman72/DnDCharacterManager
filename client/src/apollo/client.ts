import { ApolloClient, InMemoryCache } from '@apollo/client';
import { HttpLink } from '@apollo/client';
import { loader } from 'graphql.macro';
import { setContext } from '@apollo/client/link/context';
import { getToken } from '../api/token';
import { cache } from './cache'

const typeDefs = loader('./schema.gql');

const authLink = setContext((request, previousContext) => {
  const { headers } = previousContext;
  const token = getToken();
  return {
    headers: {
      ...headers,
      authorization: token ? `Token ${token}` : ''
    },
  }
});

const httpLink = new HttpLink({
    uri: 'http://127.0.0.1:8000/graphqlToken/'
});

export const client = new ApolloClient({
    link: authLink.concat(httpLink),
    cache,
    typeDefs,
});