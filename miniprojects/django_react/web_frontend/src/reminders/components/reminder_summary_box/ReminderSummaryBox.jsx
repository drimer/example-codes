import React from 'react';

import './ReminderSummaryBox.css';


export default function ReminderSummaryBoxTemplate(props) {
    return (
        <div className="reminder">
            <div className="reminder-title">
                {props.reminder.title}
            </div>
            <div className="reminder-description">
                {props.reminder.text}
            </div>
        </div>
    );
}