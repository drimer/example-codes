import React from 'react';

import PageWithHeaderTemplate from './PageWithHeader.jsx';


export default class PageWithHeader extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            settingsMenuVisible: false,
        };

        this.onSettingsIconClick = this.onSettingsIconClick.bind(this);
    }

    render() {
        return (
            <PageWithHeaderTemplate
                onSettingsIconClick={this.onSettingsIconClick}
                children={this.props.children}
                settingsMenuVisible={this.state.settingsMenuVisible}
            />
        );
    }

    onSettingsIconClick() {
        const newState = this.state.settingsMenuVisible ? false : true;
        this.setState({
            settingsMenuVisible: newState
        });
    }
}