import React from 'react';
import {
  BrowserRouter,
  Switch,
  Route,
} from 'react-router-dom';
import { AbilityRetriever } from './components/Ability/AbilityRetriever';
import { AbilityList } from './components/Ability/AbilityList';
import { LoginPage } from './pages/LoginPage/LoginPage';
import { GameSessionPage } from './pages/GameSessionPage/GameSessionPage';
import { SessionLoader } from './components/Auth/SessionLoader';
import { Logouter } from './components/Auth/Logouter';
import { CharacterSelectPage } from './pages/CharacterSelectPage/CharacterSelectPage';

export enum Paths {
  LOGIN_PAGE = '/login',
  SESSIONS_PAGE = '/sessions',
  CHARACTER_SELECT_PAGE = '/characterSelect',
  GAME = '/game',
} 

export default () => {
  return (
    <>
      <SessionLoader />
      <Logouter />
      <BrowserRouter>
        <Switch>
        <Route exact path='/'>
            <LoginPage />
          </Route>
          <Route path={Paths.LOGIN_PAGE}>
            <LoginPage />
          </Route>
          <Route path={Paths.SESSIONS_PAGE}>
            <GameSessionPage />
          </Route>
          <Route path={Paths.CHARACTER_SELECT_PAGE}>
            <CharacterSelectPage />
          </Route>
          <Route path='/abilityRetriever'>
            <AbilityRetriever
              classes={[1, 2]}
              render={(abilities => <AbilityList abilities={abilities}/>)}
            />
          </Route>
        </Switch>
      </BrowserRouter>
    </>
  );
}