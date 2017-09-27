import React from 'react';

import ReminderTemplate from './ReminderSummaryBox.jsx';


export default class ReminderSummaryBox extends React.Component {
    render() {
        return <ReminderTemplate reminder={this.props.reminder} />;
    }
}