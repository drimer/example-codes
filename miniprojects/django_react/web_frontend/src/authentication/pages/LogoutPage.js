import React from 'react';
import { Redirect } from 'react-router-dom';

import Authenticator from "../modules/Authenticator";


export default function LogoutPage() {
    if (Authenticator.isUserAuthenticated()) {
        Authenticator.logout();
    }

    return <Redirect to="/login"/>;
}