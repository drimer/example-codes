import React from 'react';

import HeaderTemplate from './Header.jsx';


export default class Header extends React.Component {
    render() {
        return (
            <HeaderTemplate
                onSettingsIconClick={this.props.onSettingsIconClick}
            />
        );
    }
}
