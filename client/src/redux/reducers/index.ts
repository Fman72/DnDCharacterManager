import { combineReducers } from 'redux';
import login, { LoginState } from './login';

export const rootReducer = combineReducers({
  login,
});

export type RootState = ReturnType<typeof rootReducer>