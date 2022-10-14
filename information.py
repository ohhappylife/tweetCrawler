def getck(): # please put ck
  return ''

def getcs(): # please put cs
  return ''

def getat(): # please put at
  return '-'

def getats(): # please put ats
  return ''

def savetoBucket(df, bn, fn): # dataframe to be saved, bucket name, file name
  path = "s3://" + bn + "/" + fn
  df.to_csv(path,
              storage_options={'key': '',
                             'secret': ''})