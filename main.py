from typing import re
from extract import extractTweets
import sys
from temp import savetoBucket
from transform import dropColumns, removeStopwords, removeHashTagMention, removeEmoji, removeURL
from datetime import date, timedelta
from transform.removeRT import removeRT

try:
    keyword = sys.argv[1]
except IndexError:
    exit(-1)

try:
    if re.match(r'\d{4}-\d{2}-\d{2}', sys.argv[2]): since = sys.argv[2]
    if re.match(r'\d{4}-\d{2}-\d{2}', sys.argv[3]): to = sys.argv[3]
    if (sys.argv[4].isnumeric()): number = sys.argv[4]
    df = extractTweets(keyword, since, to, number)
except:
    df = extractTweets(keyword)

df = dropColumns(df)

cleaned = df['full_text'].apply(removeStopwords.stopwords)
cleaned = cleaned['full_text'].apply(removeEmoji.removeemoji)
cleaned = cleaned['full_text'].apply(removeHashTagMention.removeHashtagMention)
cleaned = cleaned['full_text'].apply(removeRT.removeRT)
cleaned = cleaned['full_text'].apply(removeURL.removeURL)

savetoBucket(df, 'raw_tweets_)', str(date.today()) + '_' + keyword)
savetoBucket(cleaned, 'cleaned_tweets_', str(date.today()) + '_' + keyword)

cleaned.create_Ngram(df, str(date.today()), 'full_text')

