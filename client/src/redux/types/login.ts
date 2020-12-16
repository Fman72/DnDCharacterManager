export enum LoginActions {
  LoginStart = 'LOGIN_START',
  LoginSuccess = 'LOGIN_SUCCESS',
  LoginFailed = 'LOGIN_FAILED',
  LoginProcessing = 'LOGIN_PROCESSING',
}

export interface LoginStart {
  type: LoginActions.LoginStart,
  password: string,
  username: string,
}

export interface LoginSuccess {
  type: LoginActions.LoginSuccess  
}

export interface LoginFailed {
  type: LoginActions.LoginFailed,
  error: string,
}

export interface LoginProcessing {
  type: LoginActions.LoginProcessing
}