import tweepy as tweepy
import pandas as pd
import temp
from datetime import date, timedelta

weekago = str(date.today() - timedelta(days=7))
today = str(date.today())

location = "%s,%s,%s" % ("37.09024", "-95.712891", "2000mi") # USA

def getTweet(keyword, startDate = weekago, until = today, number = 5):
  auth = tweepy.OAuthHandler(temp.getck(), temp.getcs())
  auth.set_access_token(temp.getat(), temp.getats())

  api = tweepy.API(auth)

  cursor = tweepy.Cursor(api.search_tweets,
                         q=keyword,
                         until=until,
                         tweet_mode='extended',
                         count=number,
                         lang='en',
                         geocode=location,
                         include_entities=True)

  json_data = [r._json for r in cursor.items(number)]
  df = pd.json_normalize(json_data)

  return df