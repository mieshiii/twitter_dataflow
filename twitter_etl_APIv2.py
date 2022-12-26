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

#user id lookup
user_id_lookup = api.get_user(username = "BillGates", user_auth = True)
user_id = user_id_lookup[0]['id']

#API object
tweets = api.get_users_tweets(id = user_id, max_results = 100, user_auth = True)


tweet_list = []

#Iterating over the API response
for tweet in range(len(tweets[0])):
  
  refined_tweet = {
    "user": user_id,
    "tweet_id": tweets[0][tweet]['id'],
    "text": tweets[0][tweet]['text'],
  }
  tweet_list.append(refined_tweet)


#Creating the CSV file    
df = pd.DataFrame(tweet_list)
df.to_csv("billgates_tweeter_data.csv")
