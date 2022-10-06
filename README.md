# Tweets Crawler

## Usage
1. Collects Tweets from Twitter based on keyword and location and time range.
2. Transform collected tweets by removing stopwords/emoji/emoticons, tokenize words.
3. Create N-Grams models for collected tweets.

## Source
- Twitter (Twitter API - Tweepy)

## How to use
- Please install required library (refer Requirements.txt)
- Please fill API keys and AWS S3 information into the information.py file and change that file name into temp.py
- Please configure main.py before used (please refer to the comment on python file).; 
- Run the main.py with through the command line.
- Result (collected data, N-gram result) will be stored on S3 Bucket.

## Issues (To-be fixed)
- The pipeline is not a fault-tolerant
- The pipeline does not have function to validate the data (Partially Fixed as of Oct 5 2022).
- The pipeline does not store logs (Partially Fixed  as of Sept 8 2022 : ONLY critical issues and errors are stored into log files).
- As it utilizes default list of stopwords from NLTK, not all stopwords might be removed during the process.
- Stores login credentials into codes can increase chance of data breach.

## Requirements
- Users need to request and get API key from Twitter.
- Users need to have AWS Account, and set S3 storage and s3 bucket for storing dataset.
- Users need to have writing privilege on CWD to store log data.