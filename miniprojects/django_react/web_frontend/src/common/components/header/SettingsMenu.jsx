import React from 'react';
import { Link } from 'react-router-dom';

import './SettingsMenu.css';


export default function SettingsMenuTemplate(props) {
    return (
        <div id="user-menu">
            <ul>
                <li className="user-menu-title">
                    Settings
                </li>
                <hr/>

                {props.showLogout &&
                <li className="user-menu-item">
                    <Link to="/logout">Log out</Link>
                </li>
                }

                {props.showLogin &&
                <li className="user-menu-item">
                    <Link to="/login" onClick={props.onLoginClick}>Log in</Link>
                </li>
                }
            </ul>
        </div>
    );
}