from datetime import date, timedelta, datetime

from extract import extractTweets
from transform import dropColumns, removeStopwords, removeHashTagMention, removeEmoji, removeURL
from transform.removeRT import removeRT
from analyze import extract_keywords
from config import keywords, since, until, number, bool_date_absolute, bool_date_relative, timediff, \
    s3_tweets_uncleaned, s3_tweets_cleaned, bool_get_keyword, bool_store_rawdata_cwd, bool_store_cleaneddata_cwd,  bool_store_rawdata_s3, bool_store_cleaneddata_s3
import store_to_s3
for keyword in keywords:

    if bool_date_absolute == True:
        since = since
        until = until
    if bool_date_relative == True:
        since = datetime.strptime(until, '%Y-%M-%d') - timedelta(days=timediff)
        until = until
    if ((bool_date_absolute == False) & (bool_date_absolute == False))== True | \
            ((bool_date_absolute == True) & (bool_date_absolute == True)) == True:
        exit(-1)

    df = extractTweets.getTweet(keyword, since, until, number)
    today = date.today()
    if bool_store_rawdata_cwd == True:
        df.to_csv(str(today) + '_' + str(keyword) + '_crawled_data.csv')
    if bool_store_rawdata_s3 == True:
        store_to_s3.savetoBucket_csv(df, s3_tweets_uncleaned, str(date.today()) + '_' + keyword + '_crawled_data.csv')

    df = dropColumns.getRequiredInformation(df)
    df['full_text'] = df['full_text'].apply(removeStopwords.stopwords)
    df['full_text'] = df['full_text'].apply(removeEmoji.removeemoji)
    df['full_text'] = df['full_text'].apply(removeHashTagMention.removeHashtagMention)
    df['full_text'] = df['full_text'].apply(removeRT)
    df['full_text'] = df['full_text'].apply(removeURL.removeURL)

    if bool_get_keyword == True:
        df = extract_keywords.get_keywords(df, 'full_text')
    if bool_store_cleaneddata_cwd == True:
        df.to_csv(str(today) + '_' + str(keyword) + '_cleaned_data.csv')
    if bool_store_cleaneddata_s3 == True:
        store_to_s3.savetoBucket_csv(df, s3_tweets_cleaned, str(date.today()) + '_' + keyword + '_cleaned_data.csv')