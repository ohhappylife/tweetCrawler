"""
  tokenize_words.py
  tokenize Title_without_stopwords and Text_without_stopwords columns
    requirements : Title_without_stopwords and Text_without_stopwords columns shall be existed.
    input : dataframe
    output : dataframe
"""

from nltk.tokenize import word_tokenize

def tokenize_words(df, original):

  df['tokenized_' + original] = df[original].apply(word_tokenize)
  return df