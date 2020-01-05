# coding: utf8
# jmdictp.py
# 4/27/2015 jichi
from unitraits import cyrilchars
from unitraits.uniconv import wide2thin

def parsedef(t, language=None):
  """Get short definition out of translation
  @param  t  unicode
  @param* language  str  de(wadoku) and nl are in edict2 format, while fr/ru in edict1 format.
  @return  unicode
  """
  edict1 = language in ('ru', 'fr')
  DELIM = '<br/>'
  i = t.find(DELIM)
  if i != -1:
    t = t[i+len(DELIM):]
  i = t.find(DELIM)
  if i != -1:
    t = t[:i]
  if edict1:
    if language == 'ru':
      i = cyrilchars.findcyril(t)
      if i != -1:
        t = t[i:]
    else:
      for role in '１　', 'ｎｏｕｎ　', 'ａｄｊｅｃｔｉｖｅ　', 'ｖｅｒｂ　':
        i = t.find(role)
        if i != -1:
          t = t[i+len(role):]
  if t.startswith('<span'):
    STOP = '</span>'
    i = t.find(STOP)
    if i != -1:
      t = t[i+len(STOP):]
  while t.startswith('（'):
    i = t.find('）')
    if i != -1:
      t = t[i+1:].lstrip()
    else:
      break
  for c in '，．；（':
    i = t.find(c)
    if i != -1:
      t = t[:i]
  i = t.find('｜｜')
  if i != -1:
    t = t[i+3:] # '|| '
  t = t.strip()
  for s in '［］', '（）':
    if t and t[0] == s[0]:
      i = t.find(s[1])
      if i != -1:
        t = t[i+1:].lstrip()
    if t and t[-1] == s[0]:
      i = t.find(s[1])
      if i != -1:
        t = t[:i].rstrip()
  if t and t[-1] == '…':
    t = t[:-1].rstrip()
  if t:
    for c in '｛｝<>［］｜−·１２３４５６７８９０‘’':
      if c in t:
        return ''
    if edict1:
      if language == 'ru':
        t = t.replace('？', '') # only needed by Russian though
      for role in 'ｃｏｎｊｕｎｃｔｉｏｎ', 'ｐｒｏｎｏｕｎ', 'ｖｅｒｂ':
        if role in t:
          return ''
    t = wide2thin(t)
  return t

# EOF
