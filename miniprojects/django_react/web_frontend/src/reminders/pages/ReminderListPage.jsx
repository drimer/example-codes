import React from 'react';

import Header from '../../common/components/header/Header.js';
import ReminderSummaryBox from '../components/reminder_summary_box/ReminderSummaryBox.js';
import SettingsMenu from "../../common/components/header/SettingsMenu.js";


function ReminderListPageTemplate(props) {
    return (
        <div>
            <div id="main-container">
                <Header/>

                <div id="page-body">
                    {props.error &&
                        <div className="error">{props.error}</div>
                    }

                    {props.reminders.map((reminder) =>
                        <ReminderSummaryBox key={reminder.id} reminder={reminder} />
                    )}
                </div>
            </div>

            <SettingsMenu/>
        </div>
    );
}


export default ReminderListPageTemplate;
