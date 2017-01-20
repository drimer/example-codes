import logging
import random
import time

import names
from pusher import Pusher


APP_ID = ''  # Fill in with your app id
APP_KEY = ''  # Fill in with your app key
APP_SECRET = ''  # Fill in with your app secret
# By defult, the app cluster is set to us-east-1. If you selected a different
# one for your app, change it in the following line.
APP_CLUSTER = 'us-east-1'

CHANNEL_NAME = 'example_channel'

DELAY_SECS_MIN = 1
DELAY_SECS_MAX = 3

SENTENCES = (
    'Pusher is so awesome!',
    'Hey, Python is super great.',
    'Wait guys, have you heard of Marshmallow?',
    'This is quite a cool chat, isnt it?',
    'Yep... I quite like this website.',
)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def main():
    if any(not value for value in (APP_KEY, APP_ID, APP_SECRET)):
        print('Please, configure the credentials for your PushJS app.')
        return

    pusher = Pusher(
        app_id=APP_ID,
        key=APP_KEY,
        secret=APP_SECRET,
        cluster=APP_CLUSTER,
    )

    while True:
        delay_secs = random.randint(DELAY_SECS_MIN, DELAY_SECS_MAX)
        time.sleep(delay_secs)

        user_message = {
            'message': random.choice(SENTENCES),
            'username': names.get_first_name(),
        }
        logger.info('Sending message: {}'.format(user_message))
        pusher.trigger(CHANNEL_NAME, 'user_message', user_message)


if __name__ == '__main__':
    main()
