def getRequiredInformation(df):
  df = df[['created_at', 'full_text', 'source', 'retweet_count', 'favorite_count',
      'user.name', 'user.followers_count', 'user.created_at', 'user.lang']]
  df['source'] = df['source'].str.split("\"").str[1]
  return df