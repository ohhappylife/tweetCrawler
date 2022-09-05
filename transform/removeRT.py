import re
def removeRT(text):
    modified = lambda x: re.compile('\#').sub('', re.compile('rt @').sub('@', x, count=1).strip())
    return modified(text)