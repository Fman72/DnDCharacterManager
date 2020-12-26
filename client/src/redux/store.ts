import { createStore, applyMiddleware } from 'redux'
import createSagaMiddleware from 'redux-saga';
import { rootReducer } from './reducers/index'
import saga from './sagas/index'

const sagaMiddleware = createSagaMiddleware()
export const store = createStore(
  rootReducer,
  applyMiddleware(sagaMiddleware)
);

sagaMiddleware.run(saga);