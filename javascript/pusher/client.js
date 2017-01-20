var APP_KEY = '';  // Replace this with your APP_KEY
// By default, the app cluster is set to us-east-1. If you selected a
// different one for your app, change it in the following line.
var APP_CLUSTER = 'eu';  

var CHANNEL_NAME = 'example_channel';


function build_new_message_element(data) {
    return $('<li><div class="username">' + data.username + '</div> said: ' + data.message + '</li>');
}


function keep_chat_at_bottom() {
    var chat = $('.chat-container');
    chat.scrollTop = chat.scrollHeight;
}


function new_user_message(data) {
    console.log('User', data.username, 'wrote', data.message);

    $('.chat-container').append(build_new_message_element(data));

    keep_chat_at_bottom();
}


$(document).ready(function() {
    var pusher = new Pusher(APP_KEY, {
	cluster: 'eu',
    });  
    var channel = pusher.subscribe('example_channel');

    channel.bind('user_message', new_user_message);

    $('.new-message-form').on('submit', function(event) {
	event.preventDefault();
	channel.trigger('user_message', {username: 'Anonymous', message: 'something'});
    });
});
