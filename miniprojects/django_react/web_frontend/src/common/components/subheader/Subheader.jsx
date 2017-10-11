import React from 'react';
import { Link } from 'react-router-dom';


export default function SubheaderTemplate() {
    return (
        <div id="subheader-menu-bar">
            <Link to="/login" className="subheader-item">Log in</Link>
        </div>
    );
}
