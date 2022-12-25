import tweepy
import pandas as pd
import json
from datetime import datetime
import s3fs

keys_file = open("keys.txt")
lines = keys_file.readlines()

#Twitter keys
access_key = lines[0].rstrip()
access_secret = lines[1].rstrip()
consumer_key = lines[2].rstrip()
consumer_secret = lines[3].rstrip()

#Twitter Authentication
api = tweepy.Client(consumer_key=consumer_key, consumer_secret=consumer_secret, access_token=access_key, access_token_secret=access_secret)

#API object

user_id_lookup = api.get_user(username = "BillGates", user_auth = True)
user_id = user_id_lookup[0]['id']

tweets = api.get_users_tweets(id = user_id, max_results = 100, user_auth = True)

tweet_list = []
# for tweet in tweets:
#   text = tweet._json["full_text"]
  
#   refined_tweet = {
#     "user"
#   }
  
  
print(tweets)
