import React from 'react';

import Header from '../components/header/Header.js';
import SettingsMenu from '../components/header/SettingsMenu.js';


export default function PageWithHeaderTemplate(props) {
    return (
        <div>
            <div id="main-container">
                <Header
                    onSettingsIconClick={props.onSettingsIconClick}
                />

                {props.children}
            </div>

            {props.settingsMenuVisible &&
                <SettingsMenu/>
            }
        </div>
    );
}