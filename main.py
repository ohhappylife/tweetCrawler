from extract import extractTweets
import sys
from temp import savetoBucket
from transform import dropColumns, removeStopwords, removeHashTagMention, removeEmoji, removeURL
from transform.removeRT import removeRT
import pandas as pd

try:
  keyword = sys.argv[1]
except IndexError:
  exit(-1)

try:
  since = sys.argv[2]
  to = sys.argv[3]
  number = sys.argv[4]
  df = extractTweets.getTweet(keyword, since, to, number)

except IndexError:
  df = extractTweets.getTweet(keyword)

df.to_csv('crawled_data.csv')

df = dropColumns.getRequiredInformation(df)

df.to_csv('raw_data.csv')

df['full_text'] = df['full_text'].apply(removeStopwords.stopwords)
df['full_text'] = df['full_text'].apply(removeEmoji.removeemoji)
df['full_text'] = df['full_text'].apply(removeHashTagMention.removeHashtagMention)
df['full_text'] = df['full_text'].apply(removeRT)
df['full_text'] = df['full_text'].apply(removeURL.removeURL)

df.to_csv('cleaned_data.csv')

savetoBucket(df, 'tweetcrawlerdata', str(date.today()) + '_' + keyword)
savetoBucket(df, 'tweetcrawlerdata', str(date.today()) + '_' + keyword)

df.create_Ngram(df, str(date.today()), 'full_text')
