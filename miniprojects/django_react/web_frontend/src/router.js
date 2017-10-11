import React from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';

import LoginPage from './authentication/pages/LoginPage.js';
import ReminderListPage from './reminders/pages/ReminderListPage.js';


const Router = (
    <BrowserRouter>
        <Switch>
            <Route exact path="/" component={LoginPage} />
            <Route exact path="/login" component={LoginPage} />
            <Route exact path="/reminders" component={ReminderListPage} />
        </Switch>
    </BrowserRouter>
);



export default Router;