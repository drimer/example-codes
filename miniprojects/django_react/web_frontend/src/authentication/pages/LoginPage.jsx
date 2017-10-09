import React from 'react';

import './LoginPage.css';
import PageWithHeader from '../../common/pages/PageWithHeader.js';


function LoginPageTemplate(props) {
    return (
        <PageWithHeader>
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
         </PageWithHeader>
    );
}


export default LoginPageTemplate;