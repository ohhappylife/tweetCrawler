import re
def removeURL(text):
  link_regex = re.compile('((https?):((//)|(\\\\))+([\w\d:#@%/;$()~_?\+-=\\\.&](#!)?)*)', re.DOTALL)
  links = re.findall(link_regex, text)
  for link in links:
    text = text.replace(link[0], ', ')
  return text