from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))

def stopwords(text):
  return " ".join([word for word in str(text).split() if word not in stop_words])