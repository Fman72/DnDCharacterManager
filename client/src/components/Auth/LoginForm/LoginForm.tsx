import React, {useState, useCallback} from 'react';
import { useDispatch } from 'react-redux';
import { startLogin } from '../../../redux/actions/login';


interface LoginFormProps {

}

export const LoginForm = (props: LoginFormProps) => {

    const [ isLoggingIn , setLoggingIn ] = useState<boolean>(false);
    const [ username, setUsername] = useState<string>('');
    const [ password, setPassword] = useState<string>('');
    const dispatch = useDispatch();
    const onClick = useCallback(() => dispatch(startLogin(username, password)), [username, password]);


    return <div>
        Login Form
        Username: <input type='text' value={username} onChange={(e => setUsername(e.target.value))}></input>
        Password: <input type='password' value={password} onChange={(e => setPassword(e.target.value))}></input>
        <button onClick={onClick}>Login</button>
    </div>
}