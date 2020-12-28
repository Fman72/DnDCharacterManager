import React, {useState, useCallback, useEffect} from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { startLogin } from '../../../redux/actions/login';
import { RootState } from '../../../redux/reducers';
import { useGetGameData } from '../../GameData/helpers/useGetGameData';
import { gameDataVar, isLoggedInVar } from '../../../apollo/cache';
import { useHistory } from 'react-router-dom';
import { useReactiveVar } from '@apollo/client';


interface LoginFormProps {
  afterLogin?: () => void;
}

export const LoginForm = (props: LoginFormProps) => {
    const { afterLogin } = props;
    const [username, setUsername] = useState<string>('');
    const [password, setPassword] = useState<string>('');
    const dispatch = useDispatch();
    const onClick = useCallback(() => dispatch(startLogin(username, password, afterLogin)), [username, password, afterLogin]);
    const history = useHistory();
    const isloggedIn = useReactiveVar(isLoggedInVar);

    useEffect(() => {
      if (isloggedIn) {
        history.push('/sessions');
      }
    }, [isloggedIn]);

    return <div>
        Login Form
        Username: <input type='text' value={username} onChange={(e => setUsername(e.target.value))}></input>
        Password: <input type='password' value={password} onChange={(e => setPassword(e.target.value))}></input>
        <button onClick={onClick}>Login</button>
    </div>
}