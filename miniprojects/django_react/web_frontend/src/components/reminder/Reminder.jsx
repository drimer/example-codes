import React from 'react';

import './Reminder.css';


export default function ReminderTemplate(props) {
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