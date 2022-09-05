import string

def removeHashtagMention(text):
  entity_prefixes = ['@', '#']
  for separator in string.punctuation:
    if separator not in entity_prefixes:
      text = text.replace(separator, ' ')
  words = []
  for word in text.split():
    word = word.strip()
    if word:
      if word[0] not in entity_prefixes:
        words.append(word)
  return ' '.join(words)
