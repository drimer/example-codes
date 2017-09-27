import React from 'react';

import ReminderTemplate from './Reminder.jsx';


export default class Reminder extends React.Component {
    render() {
        return <ReminderTemplate reminder={this.props.reminder} />;
    }
}