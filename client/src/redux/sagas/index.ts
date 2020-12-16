import { all } from 'redux-saga/effects';
import { loginStartWatcher } from './login';

export default function* rootSaga() {
  yield all([
    loginStartWatcher(),
  ]);
}