import React, {useState, useCallback, useEffect} from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { startLogin } from '../../../redux/actions/login';
import { RootState } from '../../../redux/reducers';
import { useGetGameData } from '../../GameData/helpers/useGetGameData';


interface LoginFormProps {
  afterLogin?: () => void;
}

export const LoginForm = (props: LoginFormProps) => {
    const { afterLogin } = props;
    const [username, setUsername] = useState<string>('');
    const [password, setPassword] = useState<string>('');
    const dispatch = useDispatch();
    const onClick = useCallback(() => dispatch(startLogin(username, password, afterLogin)), [username, password, afterLogin]);
    const loggedIn = useSelector((state: RootState) => state.login.loggedIn);
    const [getGameData, { data, error, loading }] = useGetGameData({
      onCompleted: () => window.location.pathname = '/sessions'
    });

    useEffect(() => {
      if (loggedIn && !loading && !data) {
        getGameData();
      }
    }, [loggedIn]);

    return <div>
        Login Form
        Username: <input type='text' value={username} onChange={(e => setUsername(e.target.value))}></input>
        Password: <input type='password' value={password} onChange={(e => setPassword(e.target.value))}></input>
        <button onClick={onClick}>Login</button>
    </div>
}