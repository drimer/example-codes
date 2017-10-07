import React from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';

import UserTokenStorage from './authentication/modules/UserTokenStorage.js';
import LoginPage from './authentication/pages/LoginPage.js';
import LogoutPage from './authentication/pages/LogoutPage.js';
import ReminderListPage from './reminders/pages/ReminderListPage.js';


const Router = (
    <BrowserRouter>
        <Switch>
            <Route exact path="/" render={() => {
                return (
                    UserTokenStorage.isUserAuthenticated()
                        ? <ReminderListPage/>
                        : <LoginPage/>
                );
            }} />
push
            <Route exact path="/login" render={() => {
                return (
                    UserTokenStorage.isUserAuthenticated()
                        ? <ReminderListPage/>
                        : <LoginPage/>
                );
            }} />

            <Route exact path="/logout" component={LogoutPage} />

            <Route exact path="/reminders" render={() => {
                return (
                    UserTokenStorage.isUserAuthenticated()
                        ? <ReminderListPage/>
                        : <LoginPage/>
                );
            }} />
        </Switch>
    </BrowserRouter>
);



export default Router;