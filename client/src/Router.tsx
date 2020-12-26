import React from 'react';
import {
  BrowserRouter,
  Switch,
  Route,
} from 'react-router-dom';
import { AbilityRetriever } from './components/Ability/AbilityRetriever/AbilityRetriever';
import { AbilityList } from './components/Ability/AbilityList/AbilityList';
import { LoginPage } from './pages/LoginPage/LoginPage';
import GameSessionPage from './pages/GameSessionPage/GameSessionPage';

export default () => {
  return (
    <BrowserRouter>
      <Switch>
      <Route exact path='/'>
          <LoginPage />
        </Route>
        <Route path='/login'>
          <LoginPage />
        </Route>
        <Route path='/sessions'>
          <GameSessionPage />
        </Route>
        <Route path='/abilityRetriever'>
          <AbilityRetriever
            classes={[1, 2]}
            render={(abilities => <AbilityList abilities={abilities}/>)}
          />
        </Route>
      </Switch>
    </BrowserRouter>
  );
}