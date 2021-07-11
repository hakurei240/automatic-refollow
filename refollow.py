from requests_oauthlib import OAuth1Session
import json
import os
import datetime
import tweepy

def ref():
    consumer_key = os.environ["CONSUMER_KEY"]
    consumer_secret = os.environ["CONSUMER_SECRET"]
    access_token_key = os.environ["ACCESS_TOKEN_KEY"]
    access_token_secret = os.environ["ACCESS_TOKEN_SECRET"]
    
    auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token_key,access_token_secret)
    api = tweepy.API(auth)
    
    followers = api.followers_ids(id)   
    friend = api.friends_ids(id)
    
    for f in followers:
        if f not in friend:
            api.create_friendship(f)
            api.create_mute(f)


def bot_tweet():
    time = datetime.datetime.now()
    day = str(time.day)+"日"+str(time.hour)+"時"+str(time.minute)+"分"
    consumer_key = os.environ["CONSUMER_KEY"]
    consumer_secret = os.environ["CONSUMER_SECRET"]
    access_token_key = os.environ["ACCESS_TOKEN_KEY"]
    access_token_secret = os.environ["ACCESS_TOKEN_SECRET"]
    
    auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token_key,access_token_secret)
    api = tweepy.API(auth)

    tweeter = "@tos \n#フォロバ100 \n#相互フォロー\n#相互フォロー100 \n#相互支援 \n#フォローした人全員フォロー \n#らむくんは神絵師だぁぁぁぁぁぁぁぁぁ"+day
    api.update_status(tweeter)
    
            


            
