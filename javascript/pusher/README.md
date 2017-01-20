Example with Pusher
===================

Just a simple example of how I've been playing with PuserJS.


Setting up
----------

1. Create an account on www.pusher.com and create an app with new credentials.
2. Replace the app credentials (APP_ID, APP_KEY and APP_SECRET) with yours
in `server.py` and `client.js`. You can check these in Pusher's admin screen,
in the section "App Keys".
3. Make sure Python 3 is installed in your machine.
4. Run the commands:
> $ mkvirtualenv -p $(which python3) pusher-example
> $ pip install -r requirements.txt


Running the example
-------------------

This example is composed of two diffrent components:

- A server that will send events randomly through a Pusher channel.
  In order to run the server, run the command:
  > $ python server.py

  We'll want to have this running in the backgroun to see something happening
  in our browser n the next step.

- A client website that will listen to the events thrown by the server. In
  order to see the client working, open client.html in your favourite browser.
