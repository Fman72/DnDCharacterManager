import { HOST } from './constants';
import { getToken } from './token';

export const retrieveCurrentUser = async (username: string, password: string): Promise<Response> => {
  return await fetch(HOST + '/currentUser/', {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer: ${getToken()}`
    }
  });
}
