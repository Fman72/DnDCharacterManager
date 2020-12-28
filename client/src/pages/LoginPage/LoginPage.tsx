import React, { useEffect } from 'react';
import { LoginForm } from '../../components/Auth/LoginForm';
import { useGetGameData } from '../../components/GameData/helpers/useGetGameData';

export const LoginPage = () => {

    return <div>
        <LoginForm />
    </div>;
}