# coding: utf8
# jpmacros.py
# 1/15/2015 jichi
if __name__ == '__main__':
  import sys
  sys.path.append('..')

import re
from sakurakit.skdebug import dwarn

# Dump from Shared Dictionary at 1/15/2014
MACROS = {
  ':bos:': r'。？！…~～〜♪❤【】＜《（『「“',
  ':eos:': r'。？！…~～〜♪❤【】＞》）』」”',

  ':boc:': r'{{:bos:}}、，―─',
  ':eoc:': r'{{:eos:}}、，―─',

  'boc': r'(?:^|(?<=[{{:boc:}}]))',
  'eoc': r'(?:^|(?<=[{{:eoc:}}]))',

  'bos': r'(?:^|(?<=[{{:bos:}}]))',
  'eos': r'(?:^|(?<=[{{:eos:}}]))',

  ':digit:': r'0-9',
  ':alpha:': r'a-zA-Z',
  ':alnum:': r'{{:alpha:}}{{:digit:}}',
  ':kanji:': r'一-龯',
  ':hira:': r'ぁ-ゖ',
  ':kata:': r'ァ-ヺ',
  ':kana:': r'{{:hira:}}{{:kata:}}',

  'digit': r'[{{:digit:}}]',
  'alpha': r'[{{:alpha:}}]',
  'alnum': r'[{{:alpha:}}]',
  'kanji': r'[{{:kanji:}}]',
  'hira': r'[{{:hira:}}]',
  'kata': r'[{{:kata:}}]',
  'kana': r'[{{:kana:}}]',

  '!digit': r'[^{{:digit:}}]',
  '?!digit': r'(?!{{digit}})',
  '?<!digit': r'(?<!{{digit}})',
  '?=digit': r'(?={{digit}})',
  '?<=digit': r'(?<={{digit}})',

  '!alpha': r'[^{{:alpha:}}]',
  '?!alpha': r'(?!{{alpha}})',
  '?<!alpha': r'(?<!{{alpha}})',
  '?=alpha': r'(?={{alpha}})',
  '?<=alpha': r'(?<={{alpha}})',

  '!alnum': r'[^{{:alnum:}}]',
  '?!alnum': r'(?!{{alnum}})',
  '?<!alnum': r'(?<!{{alnum}})',
  '?=alnum': r'(?={{alnum}})',
  '?<=alnum': r'(?<={{alnum}})',

  '!kanji': r'[^{{:kanji:}}]',
  '?!kanji': r'(?!{{kanji}})',
  '?<!kanji': r'(?<!{{kanji}})',
  '?=kanji': r'(?={{kanji}})',
  '?<=kanji': r'(?<={{kanji}})',

  '!hira': r'[^{{:hira:}}]',
  '?!hira': r'(?!{{hira}})',
  '?<!hira': r'(?<!{{hira}})',
  '?=hira': r'(?={{hira}})',
  '?<=hira': r'(?<={{hira}})',

  '!kata': r'[^{{:kata:}}]',
  '?!kata': r'(?!{{kata}})',
  '?<!kata': r'(?<!{{kata}})',
  '?=kata': r'(?={{kata}})',
  '?<=kata': r'(?<={{kata}})',

  '!kana': r'[^{{:kana:}}]',
  '?!kana': r'(?!{{kana}})',
  '?<!kana': r'(?<!{{kana}})',
  '?=kana': r'(?={{kana}})',
  '?<=kana': r'(?<={{kana}})',
}

_RE_MACRO = re.compile(r'{{(.+?)}}')

def evalmacros(macros, limit=1000):
  """
  @param  macros  {unicode name:unicode value}
  @param* limit  int  maximum iteration count
  @return  unicode
  """
  for count in range(1, limit):
    dirty = False
    for pattern,text in macros.items(): # not iteritems as I will modify ret
      if text and '{{' in text:
        dirty = True
        ok = False
        for m in _RE_MACRO.finditer(text):
          macro = m.group(1)
          repl = macros.get(macro)
          if repl:
            text = text.replace("{{%s}}" % macro, repl)
            ok = True
          else:
            dwarn("missing macro", macro, text)
            ok = False
            break
        if ok:
          macros[pattern] = text
        else:
          macros[pattern] = None # delete this pattern
    if not dirty:
      break
  if count == limit - 1:
    dwarn("recursive macro definition")
evalmacros(MACROS)

def getmacro(name, macros=MACROS):
  """
  @param  name  unicode
  @param* macros  {unicode name:unicode value}
  @return  unicode
  """
  return macros.get(name)

def applymacros(text, macros=MACROS):
  """
  @param  text  unicode
  @param* macros  {unicode name:unicode value}
  @return  unicode
  """
  if text and '{{' in text:
    for m in _RE_MACRO.finditer(text):
      macro = m.group(1)
      repl = macros.get(macro)
      if repl is None:
        dwarn("missing macro:", macro, text)
      else:
        text = text.replace("{{%s}}" % macro, repl)
  return text

if __name__ == '__main__':
  import re

  t = 'す、す、すみません'
  boc = getmacro('boc')
  _re_jitter = re.compile(boc + r'([あ-んア-ヴ])(?=[、…]\1)')
  t = _re_jitter.sub('xxx', t)
  print(t)

# EOF
