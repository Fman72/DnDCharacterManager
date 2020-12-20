import { ApolloProvider } from '@apollo/client';
import React from 'react';
import { Provider } from 'react-redux';
import './App.css';
import Router from './Router';
import { client } from './apollo/client';
import { store } from './redux/store';

function App() {
  return (
    <Provider store={store}>
      <ApolloProvider client={client}>
        <Router />
      </ApolloProvider>
    </Provider>
  );
}

export default App;
