import { LoginActions } from "../types/login"

export const startLogin = (username: string, password: string) => ({
  type: LoginActions.LoginStart,
  username,
  password,
});