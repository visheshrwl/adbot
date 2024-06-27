import os
import tweepy
from config import TWITTER_API_KEY, TWITTER_API_SECRET_KEY, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET
from bot_logic import process_message, log_interaction, rate_limited

auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET_KEY)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        user = status.user.screen_name
        user_message = status.text
        
        if rate_limited(user):
            return
        
        response = process_message(user_message)
        log_interaction('Twitter', user, user_message, response)
        api.update_status(f"@{user} {response}", in_reply_to_status_id=status.id)

def start_twitter_bot():
    myStreamListener = MyStreamListener()
    myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)
    myStream.filter(track=['@YourTwitterBotHandle'])
