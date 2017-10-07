import React from 'react';
import Request from 'es6-request';

import './ReminderListPage.css';
import ReminderListPageTemplate from './ReminderListPage.jsx';
import UserTokenStorage from "../../authentication/modules/UserTokenStorage";


const BACKEND_URL = 'http://localhost:8990'

export default class ReminderListPage extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            reminders: [],
            error: null
        };
    }

    componentDidMount() {
        const token = UserTokenStorage.getToken();

        Request.get(BACKEND_URL + "/reminders/")
            .header('Authorization', 'Token ' + token)
            .then(([body, result]) => {
                const result_parsed = JSON.parse(body);
                const reminders = Array.from(result_parsed, reminder => {
                    return {id: reminder.id, title: reminder.title, text: reminder.text};
                });

                this.setState({reminders: reminders});
            })
            .catch(error => {
                const error_msg = (
                    'Something went wrong. Please contact support if this error '
                    + ' persists.'
                );
                this.setState({error: error_msg})
            });
    }

    render() {
        return (
            <ReminderListPageTemplate
                reminders={this.state.reminders}
                error={this.state.error} />
        );
    }
}