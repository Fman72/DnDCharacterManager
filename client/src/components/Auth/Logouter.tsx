import { useReactiveVar } from '@apollo/client';
import { isLoggedInVar } from '../../apollo/cache';
import { useHistory } from 'react-router-dom';
import React, { useEffect } from 'react';

const PUBLIC_PATHS = ['/', ''];

export const Logouter = () => {

  const isLoggedIn = useReactiveVar(isLoggedInVar);
  const history = useHistory();

  useEffect(() => {
    if (!isLoggedIn && !PUBLIC_PATHS.includes(window.location.pathname)) {
      history.push('/');
    }
  }, [isLoggedIn]);

  return <></>;
}