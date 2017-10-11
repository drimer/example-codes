import React from 'react';
import $ from 'jquery/dist/jquery.js';

import Authenticator from '../../../authentication/modules/Authenticator';
import SettingsMenuTemplate from './SettingsMenu.jsx';


export default class SettingsMenu extends React.Component {
    render() {
        return (
            <SettingsMenuTemplate
                showLogin={Authenticator.isUserAuthenticated() ? false : true}
                showLogout={Authenticator.isUserAuthenticated() ? true : false}
                onLoginClick={this.onLoginClick}
            />
        );
    }

    onLoginClick() {
        $('#user-menu').hide();
    }
}