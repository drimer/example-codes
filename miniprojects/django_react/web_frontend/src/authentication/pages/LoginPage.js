import React from 'react';
import { Redirect } from 'react-router-dom';

import LoginPageTemplate from './LoginPage.jsx';
import Authenticator from '../modules/Authenticator.js';


export default class LoginPage extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            username: '',
            password: '',
            errors: [],
            loginSuccessful: false,
        };

        this.handleLoginSubmit = this.handleLoginSubmit.bind(this);
        this.handleUsernameChange = this.handleUsernameChange.bind(this);
        this.handlePasswordChange = this.handlePasswordChange.bind(this);
    }

    render() {
        if (this.state.loginSuccessful) {
            return <Redirect to="/" />
        }

        return (
            <LoginPageTemplate
                handleLoginSubmit={this.handleLoginSubmit}
                handleUsernameChange={this.handleUsernameChange}
                handlePasswordChange={this.handlePasswordChange}
                errors={this.state.errors}
            />
        );
    }

    handleUsernameChange(e) {
        this.setState({username: e.target.value});
    }

    handlePasswordChange(e) {
        this.setState({password: e.target.value});
    }

    handleLoginSubmit(e) {
        e.preventDefault();

        Authenticator.login(this.state.username, this.state.password)
            .then((token) => {
                this.setState({
                    errors: [],
                    loginSuccessful: true,
                });
            })
            .catch((errors) => {
                this.setState({errors: errors});
            });
    }
}