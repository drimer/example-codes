import React from 'react';

import './LoginPage.css';
import Header from '../../common/components/header/Header.js';
import SettingsMenu from "../../common/components/header/SettingsMenu.js";


function LoginPageTemplate(props) {
    return (
        <div>
            <div id="main-container">
                <Header/>

                {props.errors.length > 0 &&
                    <p>{props.errors}</p>
                }

                <div id="login-form-container">
                    <form id="login-form" onSubmit={props.handleLoginSubmit}>
                        <label htmlFor="username">Username</label>
                        <input id="username" name="username" onChange={props.handleUsernameChange} />

                        <label htmlFor="password">Password</label>
                        <input id="password" name="password" type="password" onChange={props.handlePasswordChange}/>

                        <input className="action-btn" type="submit" value="Log in" />
                    </form>
                </div>
            </div>

            <SettingsMenu/>
        </div>
    );
}


export default LoginPageTemplate;