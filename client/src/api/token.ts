const TOKEN_KEY = 'TOKENY_TOKEN';

const HOST = 'http://localhost:8000';

export const retrieveToken = async (username: string, password: string): Promise<Response> => {
  return await fetch(HOST + '/getToken/', {
    method: 'POST',
    body: JSON.stringify({
      username,
      password,
    }),
    headers: {
      'Content-Type': 'application/json'
    }
  });
}

export const getToken = (): string|null => {
  return localStorage.getItem(TOKEN_KEY);
}

export const setToken = (token: string) => {
  localStorage.setItem(TOKEN_KEY, token);
}