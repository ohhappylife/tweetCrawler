import pandas as pd
import temp
import re
import unicodedata
import nltk

def basic_clean(text):
  wnl = nltk.stem.WordNetLemmatizer()
  text = (unicodedata.normalize('NFKD', text)
    .encode('ascii', 'ignore')
    .decode('utf-8', 'ignore')
    .lower())
  words = re.sub(r'[^\w\s]', '', text).split()
  return [wnl.lemmatize(word) for word in words]

def Ngram(df, name, columns):
  title = basic_clean(''.join(str(df[columns].tolist())))

  for i in range(1,4):
    ftitle = name + "_" +columns + '_' + str(i) + '.csv'

    ngram_title = (pd.Series(nltk.ngrams(title, i)).value_counts()).reset_index()

    temp.savetoBucket(ngram_title, 'ngram', ftitle)


