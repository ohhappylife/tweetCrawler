import tweepy as tweepy
import pandas as pd
from datetime import date, timedelta
from config import tweepy_api_key, tweepy_key_secret,tweepy_access_token_secret,tweepy_access_token
import information

weekago = str(date.today() - timedelta(days=7))
today = str(date.today())

location = "%s,%s,%s" % ("37.09024", "-95.712891", "2000mi") # USA

def getTweet(keyword, startDate = weekago, until = today, number = 5):
  auth = tweepy.OAuthHandler(tweepy_api_key, tweepy_key_secret)
  auth.set_access_token(tweepy_access_token, tweepy_access_token_secret)

  api = tweepy.API(auth)

  cursor = tweepy.Cursor(api.search_tweets,
                         q=keyword,
                         since=startDate,
                         until=until,
                         tweet_mode='extended',
                         count=number,
                         lang='en',
                         geocode=location,
                         include_entities=True)

  json_data = [r._json for r in cursor.items(number)]
  df = pd.json_normalize(json_data)

  return df