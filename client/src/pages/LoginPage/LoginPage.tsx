import React, { useEffect } from 'react';
import { LoginForm } from '../../components/Auth/LoginForm';
import { useGetGameData } from '../../hooks/GameData/useGetGameData';
import { useReactiveVar } from '@apollo/client';
import { isLoggedInVar } from '../../apollo/cache';

export const LoginPage = () => {

    const isLoggedIn = useReactiveVar(isLoggedInVar);

    return <div>
        <LoginForm isLoggedIn={isLoggedIn} />
    </div>;
}