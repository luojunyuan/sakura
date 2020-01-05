# coding: utf8
# 4/3/2015 jichi
if __name__ == '__main__':
  import sys
  sys.path.append('..')

from unitraits import jpchars, jpmacros
import re

_J2C_NAME = {
  'の': '之',
  'ノ': '之',
  'ケ': '', # example: 芹ケ野
  'ヶ': '',
  'し': '', # example: 串刺し公
  'つ': '', # example: 一つ目小僧
  'ツ': '',
  'っ': '',
  'ッ': '',
}
_rx_name_repeat = re.compile(
  jpmacros.applymacros(
    r"({{kanji}})々"
  )
)
def ja2zh_name(text): # unicode -> unicode
  for k,v in _J2C_NAME.items():
    text = text.replace(k, v)
  if '々' in text:
    text = _rx_name_repeat.sub(r'\1\1', text)
  return text

_rx_name_sep = re.compile(
  jpmacros.applymacros(
    r"{{?<=kanji}}[%s]{{?=kanji}}" % (
      ' 　・＝ー' + ''.join(iter(_J2C_NAME.keys()))
    )
  )
)

def ja2zh_name_test(text): # unicode -> bool
  text = _rx_name_sep.sub('', text).replace('々', '')
  return bool(text) and jpchars.allkanji(text)

def ja2zht_name_fix(text): # unicode -> unicode
  return text.replace('裡', '里').replace('裏', '里')

if __name__ == '__main__':
  #s = u'乃々華'
  #s = u'串刺し公'
  s = '一つ目小僧'
  print(ja2zh_name_test(s))
  print(ja2zh_name(s))

# EOF
