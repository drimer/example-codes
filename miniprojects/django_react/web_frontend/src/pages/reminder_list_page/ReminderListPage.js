import React from 'react';
import Request from 'es6-request';

import './ReminderListPage.css';
import ReminderListPageTemplate from './ReminderListPage.jsx';

const BACKEND_URL = 'http://localhost:8990'

export default class ReminderListPage extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            reminders: []
        };
    }

    componentDidMount() {
        console.log('yada');
        Request.get(BACKEND_URL + "/reminders")
        .then(([body, result]) => {
            const result_parsed = JSON.parse(body);
            const reminders = Array.from(result_parsed, reminder => {
                return {id: reminder.id, title: reminder.title, text: reminder.text};
            });

            this.setState({reminders: reminders});
        })
        .catch(error => {
            console.log('the fuck');
            console.log('error!', error);
        });
    }

    render() {
        return <ReminderListPageTemplate reminders={this.state.reminders} />;
    }
}