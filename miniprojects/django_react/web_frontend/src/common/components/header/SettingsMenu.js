import React from 'react';

import Authenticator from '../../../authentication/modules/Authenticator';
import SettingsMenuTemplate from './SettingsMenu.jsx';


export default class SettingsMenu extends React.Component {
    render() {
        return (
            <SettingsMenuTemplate
                showLogin={Authenticator.isUserAuthenticated() ? false : true}
                showLogout={Authenticator.isUserAuthenticated() ? true : false}
            />
        );
    }
}