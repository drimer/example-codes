import React from 'react';

import './Header.css';
import LogoImg from './logo.png';


export default function HeaderTemplate(props) {
    return (
        <div id="header">
            <div id="header-logo-container">
                <img id="logo-img" alt="logo" src={LogoImg}/>
            </div>

            <div id="header-settings-icon-container">
                <label id="burger-icon" onClick={props.onSettingsIconClick}>
                    &#9776;
                </label>
            </div>
        </div>
    );
}
