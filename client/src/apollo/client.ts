import { ApolloClient, InMemoryCache } from '@apollo/client';
import { split, HttpLink } from '@apollo/client';
import { WebSocketLink } from '@apollo/client/link/ws';
import { loader } from 'graphql.macro';

const typeDefs = loader('./schema.gql');

const httpLink = new HttpLink({
    uri: 'http://127.0.0.1:8000/graphql/'
});

export const client = new ApolloClient({
    link: httpLink,
    cache: new InMemoryCache(),
    typeDefs,
});