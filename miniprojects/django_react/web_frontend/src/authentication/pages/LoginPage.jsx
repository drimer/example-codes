import React from 'react';

import Header from '../../common/components/header/Header.js';
import Subheader from '../../common/components/subheader/Subheader.js';



function LoginPageTemplate(props) {
    return (
        <div id="main-container">
            <Header/>
            <Subheader/>
            <p>Login page</p>

            {props.errors.length > 0 &&
                <p>{props.errors}</p>
            }

            <form onSubmit={props.handleLoginSubmit}>
                <p>Username: <input name="username" onChange={props.handleUsernameChange} /></p>
                <p>Password: <input name="password" type="password" onChange={props.handlePasswordChange}/></p>

                <input type="submit" text="Submit" />
            </form>
        </div>
    );
}


export default LoginPageTemplate;