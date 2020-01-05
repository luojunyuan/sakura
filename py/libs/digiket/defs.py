# coding: utf8
# defs.py
# 6/18/2014 jichi

def toitemkey(id):
  """
  @param  id  int or str
  @return  str
  """
  try: return 'ITM%07d' % int(id)
  except: return ''

def fromitemkey(key):
  """
  @param  key  str
  @return  int
  """
  if isinstance(key, int):
    return key
  elif isinstance(key, str):
    if key.startswith('ITM'):
      key = key[3:]
    key = key.lstrip('0')
  try: return int(key)
  except: return 0

# EOF
