import React, {useState, useCallback, useEffect, useRef} from 'react';
import { useHistory } from 'react-router-dom';
import { useReactiveVar } from '@apollo/client';
import { useDispatch } from 'react-redux';
import { startLogin } from '../../redux/actions/login';
import { isLoggedInVar } from '../../apollo/cache';
import { Paths } from '../../Router';


interface LoginFormProps {
  afterLogin?: () => void;
  isLoggedIn: boolean;
}

export const LoginForm = (props: LoginFormProps) => {
    const { afterLogin, isLoggedIn } = props;
    const [username, setUsername] = useState<string>('');
    const [password, setPassword] = useState<string>('');
    const dispatch = useDispatch();
    const onClick = useCallback(() => dispatch(startLogin(username, password, afterLogin)), [username, password, afterLogin]);
    const history = useHistory();
 
    useEffect(() => {
      if (isLoggedIn) {
        history.push(Paths.SESSIONS_PAGE);
      }
    }, [isLoggedIn]);

    return <div>
        Login Form
        Username: <input type='text' value={username} onChange={(e => setUsername(e.target.value))}></input>
        Password: <input type='password' value={password} onChange={(e => setPassword(e.target.value))}></input>
        <button onClick={onClick}>Login</button>
    </div>
}