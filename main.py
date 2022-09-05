from typing import re
from extract import extractTweets
import sys
from transform import dropColumns, removeStopwords
from datetime import date, timedelta

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

    df.create_Ngram(df, str(date.today()), 'full_text')