import React from 'react';

import Header from '../../components/header/Header.js';
import Subheader from '../../components/subheader/Subheader.js';
import Reminder from '../../components/reminder/Reminder.js';


function ReminderListPageTemplate(props) {
    return (
        <div id="main-container">
            <Header/>
            <Subheader/>

            <div id="page-body">
                {props.reminders.map((reminder) =>
                    <Reminder id={reminder.id} reminder={reminder} />
                )}
            </div>
        </div>
    );
}


export default ReminderListPageTemplate;
