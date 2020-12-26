import { LoginSuccess, LoginStart, LoginFailed, LoginActions } from "../types/login";

type LoginActionTypes = LoginSuccess | LoginStart | LoginFailed;

export interface LoginState {
  loggingIn: boolean;
  loggedIn: boolean;
}

const initialState = {
  loggingIn: false,
  loggedIn: false,
}

export default (state = initialState, action: LoginActionTypes) => {
  switch(action.type) {
    case LoginActions.LoginStart:
      return {
        ...state,
        loggingIn: true,
      }
    case LoginActions.LoginSuccess:
      return {
        ...state,
        loggingIn: false,
        loggedIn: true,
      }
    case LoginActions.LoginFailed:
      return {
        ...state,
        loggingIn: false,
      }
    default:
      return initialState;
  }
}