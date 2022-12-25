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
auth = tweepy.OAuth2AppHandler(consumer_key, consumer_secret)

#API object
api = tweepy.API(auth)

#Fetching the tweets
tweets = api.user_timeline( screen_name='@BillGates', count=200, include_rts=False, tweet_mode='extended')  

#iterating on the response  
tweet_list = []
for tweet in tweets:
  text = tweet._json["full_text"]
  
  refined_tweet = {
                       "user": tweet.user.screen_name,
                       "text": text,
                       "favorite_count": tweet.favorite_count,
                       "retweet_count": tweet.retweet_count,
                       "created_at": tweet.created_at     
                    }
  tweet_list.append(refined_tweet)
  
df = pd.DataFrame(tweet_list)
df.to_csv("billgates_tweeter_data.csv")