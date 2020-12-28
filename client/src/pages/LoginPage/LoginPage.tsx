import React, { useEffect } from 'react';
import { LoginForm } from '../../components/Auth/LoginForm';
import { useGetGameData } from '../../hooks/GameData/useGetGameData';

export const LoginPage = () => {

    return <div>
        <LoginForm />
    </div>;
}