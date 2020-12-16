import React, {useState} from 'react';

interface LoginFormProps {

}

//Not going to set up redux/sagas as I think this is the only non graphql call I will make.
export const loginForm = (props: LoginFormProps) => {

    const [ isLoggingIn , setLoggingIn ] = useState<boolean>(false);
    
    return <div>
        Login Form
        <form>
          Username: <input type='text'></input>
          Password: <input type='password'></input>
        </form>
    </div>
}