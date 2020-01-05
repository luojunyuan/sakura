# coding: utf8
# kochars.py
# 4/25/2015 jichi
from functools import partial
from . import unichars

def ishangul(ch):
  """
  @param  ch  str
  @return  bool
  """
  if len(ch) != 1:
    return False
  ch = ord(ch[0])
  return ch > 127 and (
    0xac00 <= ch and ch <= 0xd7a3    # Hangul Syllables (AC00-D7A3) which corresponds to (가-힣)
    or 0x1100 <= ch and ch <= 0x11ff # Hangul Jamo (1100–11FF)
    or 0x3130 <= ch and ch <= 0x318f # Hangul Compatibility Jamo (3130-318F)
    or 0xa960 <= ch and ch <= 0xa97f # Hangul Jamo Extended-A (A960-A97F)
    or 0xd7b0 <= ch and ch <= 0xd7ff # Hangul Jamo Extended-B (D7B0-D7FF)
  )

def anyhangul(text):
  """
  @param  text  unicode
  @return  bool
  """
  for c in text:
    if ishangul(c):
      return True
  return False

def allhangul(text):
  """
  @param  text  unicode
  @return  bool
  """
  if not text:
    return False
  for c in text:
    #if ord(c) >= 128 and not ishangul(c):
    if c != ' ' and not ishangul(c):
      return False
  return True

# http://en.wikipedia.org/wiki/Template:Unicode_chart_Hangul_Syllables
# http://en.wikipedia.org/wiki/Hangul_consonant_and_vowel_tables
ORD_SYLLABLE_FIRST = 0xac00
ORD_SYLLABLE_LAST = 0xd7a3
issyllable = partial(unichars.charinrange, start=ORD_SYLLABLE_FIRST, stop=ORD_SYLLABLE_LAST)

HANGUL_FINALS = (
  '',   # 0
  'ᆨ', # 1
  'ᆩ', # 2
  'ᆪ', # 3
  'ᆫ', # 4
  'ᆬ', # 5
  'ᆭ', # 6
  'ᆮ', # 7
  'ᆯ', # 8
  'ᆰ', # 9
  'ᆱ', # 10
  'ᆲ', # 11
  'ᆳ', # 12
  'ᆴ', # 13
  'ᆵ', # 14
  'ᆶ', # 15
  'ᆷ', # 16
  'ᆸ', # 17
  'ᆹ', # 18
  'ᆺ', # 19
  'ᆻ', # 20
  'ᆼ', # 21
  'ᆽ', # 22
  'ᆾ', # 23
  'ᆿ', # 24
  'ᇀ', # 25
  'ᇁ', # 26
  'ᇂ', # 27
)
# http://www.verbix.com/languages/korean.php?verb=%EB%AA%A8%EB%A5%B4%EB%8B%A4
HANGUL_FINALS_ROMAJA = (
  '',  # 0
  'g', # 1 'ᆨ'
  'gg', # 2 'ᆩ'
  'gs', # 3 'ᆪ'
  'n', # 4 'ᆫ'
  'nj', # 5 'ᆬ'
  'nh', # 6 'ᆭ'
  'd', # 7 'ᆮ'
  'l', # 8 'ᆯ'
  'lg', # 9 'ᆰ'
  'lm', # 10 'ᆱ'
  'lb', # 11 'ᆲ'
  'ls', # 12 'ᆳ'
  'lt', # 13 'ᆴ'
  'lp', # 14 'ᆵ'
  'lh', # 15 'ᆶ'
  'm', # 16 'ᆷ'
  'b', # 17 'ᆸ'
  'bs', # 18 'ᆹ'
  's', # 19 'ᆺ'
  'ss', # 20 'ᆻ'
  'ng', # 21 'ᆼ'
  'j', # 22 'ᆽ'
  'c', # 23 'ᆾ'
  'k', # 24 'ᆿ'
  't', # 25 'ᇀ'
  'p', # 26 'ᇁ'
  'h', # 27 'ᇂ'
)
HANGUL_FINAL_COUNT = 28
def gethangulfinal(ch):
  """Get the final character of the 2~3 characters
  @param  ch
  @return  str or None
  """
  if ch and len(ch) == 1:
    ch = ord(ch)
    if ch >= ORD_SYLLABLE_FIRST and ch <= ORD_SYLLABLE_LAST:
      return HANGUL_FINALS[(ch - ORD_SYLLABLE_FIRST) % HANGUL_FINAL_COUNT]

HANGUL_FINAL_COUNT = 28
def gethangulfinal_en(ch):
  """Get the final character of the 2~3 characters
  @param  ch
  @return  str or None
  """
  if ch and len(ch) == 1:
    ch = ord(ch)
    if ch >= ORD_SYLLABLE_FIRST and ch <= ORD_SYLLABLE_LAST:
      return HANGUL_FINALS_ROMAJA[(ch - ORD_SYLLABLE_FIRST) % HANGUL_FINAL_COUNT]

# EOF
