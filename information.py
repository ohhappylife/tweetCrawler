def getck():
  return ''

def getcs():
  return ''

def getat():
  return '-'

def getats():
  return ''

def savetoBucket(df, bn, fn):
  path = "s3://" + bn + "/" + fn
  df.to_csv(path,
              storage_options={'key': '',
                             'secret': ''})