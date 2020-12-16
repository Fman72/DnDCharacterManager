const TOKEN_KEY = 'TOKENY_TOKEN';

export const retrieveToken = async (username: string, password: string) => {
  const result: Response = await fetch('/getToken', {
    method: 'POST',
    body: JSON.stringify({
      username,
      password,
    })
  });
}

export const getToken = (): string|null => {
  return localStorage.getItem(TOKEN_KEY);
}

export const setToken = (token: string) => {
  localStorage.setItem(TOKEN_KEY, token);
}