import React from 'react';
import { Redirect } from 'react-router-dom';

import Authenticator from "../modules/Authenticator";
import UserTokenStorage from "../modules/UserTokenStorage";

export default function LogoutPage() {
    if (UserTokenStorage.isUserAuthenticated()) {
        Authenticator.logout();
    }

    console.log('redirecting');
    return <Redirect to="/login"/>;
}