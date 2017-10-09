import React from 'react';

import PageWithHeader from '../../common/pages/PageWithHeader.js';
import ReminderSummaryBox from '../components/reminder_summary_box/ReminderSummaryBox.js';


function ReminderListPageTemplate(props) {
    return (
        <PageWithHeader>
            <div id="page-body">
                {props.error &&
                    <div className="error">{props.error}</div>
                }

                {props.reminders.map((reminder) =>
                    <ReminderSummaryBox key={reminder.id} reminder={reminder} />
                )}
            </div>
        </PageWithHeader>
    );
}


export default ReminderListPageTemplate;
