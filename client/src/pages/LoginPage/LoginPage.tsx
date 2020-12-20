import React from 'react';
import { LoginForm } from '../../components/Auth/LoginForm/LoginForm';

export default () => {
    return <div>
        <LoginForm afterLogin={() => window.location.pathname = '/sessions'}/>
    </div>;
}