import { createStore, applyMiddleware } from 'redux'
import createSagaMiddleware from 'redux-saga';
import reducer from './reducers/index'
import saga from './sagas/index'

const sagaMiddleware = createSagaMiddleware()
export default createStore(
  reducer,
  applyMiddleware(sagaMiddleware)
);