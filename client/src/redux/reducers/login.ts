import { LoginSuccess, LoginStart, LoginFailed, LoginActions } from "../types/login";

type LoginActionTypes = LoginSuccess | LoginStart | LoginFailed;

interface LoginState {
  loggingIn: boolean;
}

const initialState = {
  loggingIn: false,
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
      }
    case LoginActions.LoginFailed:
      return {
        ...state,
        loggingIn: false,
      }
  }
}