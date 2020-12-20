import { LoginActions } from "../types/login"

export const startLogin = (username: string, password: string, callback?: () => void) => ({
  type: LoginActions.LoginStart,
  username,
  password,
  callback,
});