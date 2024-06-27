import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from config import SLACK_BOT_TOKEN, SLACK_APP_TOKEN
from bot_logic import process_message, log_interaction, rate_limited

app = App(token=SLACK_BOT_TOKEN)

@app.message("")
def handle_message_events(message, say):
    user = message['user']
    user_message = message['text']
    
    if rate_limited(user):
        say("You are sending messages too quickly. Please wait a while before trying again.")
        return
    
    response = process_message(user_message)
    log_interaction('Slack', user, user_message, response)
    say(response)

def start_slack_bot():
    handler = SocketModeHandler(app, SLACK_APP_TOKEN)
    handler.start()
