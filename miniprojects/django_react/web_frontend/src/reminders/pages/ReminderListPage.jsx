import React from 'react';

import Header from '../../common/components/header/Header.js';
import Subheader from '../../common/components/subheader/Subheader.js';
import ReminderSummaryBox from '../components/reminder_summary_box/ReminderSummaryBox.js';


function ReminderListPageTemplate(props) {
    return (
        <div id="main-container">
            <Header/>
            <Subheader isUserAuthenticated={props.isUserAuthenticated}/>

            <div id="page-body">
                {props.error &&
                    <div class="error">{props.error}</div>
                }

                {props.reminders.map((reminder) =>
                    <ReminderSummaryBox key={reminder.id} reminder={reminder} />
                )}
            </div>
        </div>
    );
}


export default ReminderListPageTemplate;
