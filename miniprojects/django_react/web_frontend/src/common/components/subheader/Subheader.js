import React from 'react';

import './Subheader.css';
import SubheaderTemplate from './Subheader.jsx';


function Subheader(props) {
    return <SubheaderTemplate
        isUserAuthenticated={props.isUserAuthenticated}
    />;
}


export default Subheader;