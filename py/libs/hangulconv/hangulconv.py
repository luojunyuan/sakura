# coding: utf8
# hangulconv.py
# 5/2/2015 jichi
# http://en.wikipedia.org/wiki/Hangul_Syllables
from korean import hangul

BINARY_CONSONANTS = {
  'ㄶ': ('ㄴ', 'ㅎ'),
  'ㄵ': ('ㄴ', 'ㅈ'),

  'ㄺ': ('ㄹ', 'ㄱ'),
  'ㄼ': ('ㄹ', 'ㅂ'),
  'ㄻ': ('ㄹ', 'ㅁ'),
  'ㄽ': ('ㄹ', 'ㅅ'),
  'ㄾ': ('ㄹ', 'ㅌ'),
  'ㄿ': ('ㄹ', 'ㅍ'),
  'ㅀ': ('ㄹ', 'ㅎ'),

  'ㄲ': ('ㄱ', 'ㄱ'),
  'ㄳ': ('ㄱ', 'ㅅ'),

  'ㅆ': ('ㅅ', 'ㅅ'),

  'ㅃ': ('ㅂ', 'ㅂ'),
  'ㅄ': ('ㅂ', 'ㅅ'),
}

def split_consonant(ch):
  """
  @param  ch  unicode
  @return  (unicode x, unicode y) or None
  """
  return BINARY_CONSONANTS.get(ch)

def join_consonant(l):
  """
  @param  l  (unicode x, or unicode y) or None
  @return  unicode or None
  """
  if len(l) == 1:
    return l[0]
  if len(l) == 2:
    for k,v in BINARY_CONSONANTS.items():
      if v[0] == l[0] and v[1] == l[1] or v[1] == l[0] and v[0] == l[1]:
        return k

def split_char(ch):
  """
  @param  ch  unicode
  @return  [unicode] or None
  """
  try: return list(filter(bool,  hangul.split_char(ch)))
  except: pass

def join_char(l):
  """
  @param  l  [unicode]
  @return  unicode or None
  """
  try:
    if len(l) == 2:
      l = l[0], l[1], ''
    return hangul.join_char(l)
  except: pass

if __name__ == '__main__':
  t = '옶'
  t = '갟'
  l = split_char(t)
  print(l[-2], l[-1])
  print(join_char(l))

  t = 'ㅄ'
  l = split_consonant(t)
  print(l[-1])
  print(join_consonant(l))

# EOF
