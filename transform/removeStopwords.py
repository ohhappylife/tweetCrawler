def stopwords(text):
  return " ".join([word for word in str(text).split() if word not in stop_words])