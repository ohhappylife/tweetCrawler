# Tweets Crawler

## Usage
1. Collects Tweets from Twitter based on keyword and location and time range.
   - Crawled data:
      - created_at
      - full_text
      - source
      - retweet_count
      - favorite_count
      - user.name
      - user.followers_count
      - user.created_at
      - user.lang
      - keyword
2. Transform collected tweets by removing stopwords/emoji/emoticons.
3. Extract keywords from tweets.

## Source
- Twitter (Twitter API - Tweepy)
  - User need to create and get API key from https://developer.twitter.com/

## How to use
- Please install required library (refer Requirements.txt)
- Please fill API keys and AWS S3 information into the config_example.py file and change that file name into config.py
- Result (collected data, N-gram result) will be stored on either S3 Bucket or cwd (based con configuration of the user).

## Requirements
- Users need to request and get API key from Twitter.