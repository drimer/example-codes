import React from 'react';
import $ from 'jquery/dist/jquery.js';

import HeaderTemplate from './Header.jsx';


export default class Header extends React.Component {
    render() {
        return (
            <HeaderTemplate
                onSettingsIconClick={this.onSettingsIconClick}
            />
        );
    }

    onSettingsIconClick() {
        $('#user-menu').toggle();
    }
}
