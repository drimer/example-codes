import React from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';

import Authenticator from './authentication/modules/Authenticator.js';
import LoginPage from './authentication/pages/LoginPage.js';
import LogoutPage from './authentication/pages/LogoutPage.js';
import ReminderListPage from './reminders/pages/ReminderListPage.js';


const Router = (
    <BrowserRouter>
        <Switch>
            <Route exact path="/" render={() => {
                return (
                    Authenticator.isUserAuthenticated()
                        ? <ReminderListPage/>
                        : <LoginPage/>
                );
            }} />
push
            <Route exact path="/login" render={() => {
                return (
                    Authenticator.isUserAuthenticated()
                        ? <ReminderListPage/>
                        : <LoginPage/>
                );
            }} />

            <Route exact path="/logout" component={LogoutPage} />

            <Route exact path="/reminders" render={() => {
                return (
                    Authenticator.isUserAuthenticated()
                        ? <ReminderListPage/>
                        : <LoginPage/>
                );
            }} />
        </Switch>
    </BrowserRouter>
);



export default Router;