import React from 'react';
import { Link } from 'react-router-dom';


export default function SubheaderTemplate(props) {
    return (
        <div id="subheader-menu-bar">
            {props.isUserAuthenticated === true &&
                <Link to="/logout" className="subheader-item" href="#">Log out</Link>
            }

            {props.isUserAuhenticated === false &&
                <Link to="/login" className="subheader-item">Log in</Link>
            }
        </div>
    );
}
