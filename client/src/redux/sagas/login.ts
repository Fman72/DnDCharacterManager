import { takeLatest, put, call } from 'redux-saga/effects';
import { LoginStart, LoginActions } from '../types/login';
import { retrieveToken, setToken } from '../../api/token';

function* loginStartWorker(action: LoginStart) {
  const { username, password, callback } = action;
  try {
    yield put({type: LoginActions.LoginProcessing});
    const response: Response = yield call(retrieveToken, username, password);
    if (response.status === 200) {
      const responseBody = yield response.json();
      yield setToken(responseBody.token);
      yield put({type: LoginActions.LoginSuccess});
      // This should kick off another saga but want to wait to abstract saga code first.
      if (callback) {
        callback();
      }
    }
  } catch (ex) {
    yield put({type: LoginActions.LoginFailed, error: ex});
  }
}

function* loginStartWatcher() {
  yield takeLatest(LoginActions.LoginStart, loginStartWorker);
}

export {
  loginStartWatcher
}