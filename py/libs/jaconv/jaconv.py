# coding: utf8
# jaconv.py
# 12/30/2012 jichi

if __name__ == '__main__':
  import sys
  sys.path.append("..")

import re
from sakurakit.skdebug import dprint
from sakurakit.skstr import multireplacer
from unitraits.uniconv import hira2kata
from . import kanadef

# Global settings

OPT_NAME_MACRON = True # enable macron for English

def setopt(**kwargs):
  dprint(kwargs)
  v = kwargs.get('macron')
  if v is not None:
    global OPT_NAME_MACRON
    OPT_NAME_MACRON = v

def _lang_has_capital(lang): # str -> bool
  return lang not in ('ar', 'ko', 'th')
def _lang_is_latin(lang): # str -> bool
  return lang not in ('ko', 'th', 'ar', 'ru', 'uk', 'el')

# Cached converters

def _makeconverter(fr, to):
  """
  @param  fr  int
  @param  to  int
  @return  function or None
  """
  s = kanadef.TABLES[to]
  if fr == 'kata':
    s = hira2kata(s)
  elif fr == 'kana':
    s += '\n' + hira2kata(s)

  t = kanadef.parse(s)
  return multireplacer(t)

_CONVERTERS = {}
def _convert(text, fr, to):
  """
  @param  text  unicode
  @param  fr  int
  @param  to  int
  @return  unicode
  """
  conv = _CONVERTERS.get(fr + to)
  if not conv:
    conv = _CONVERTERS[fr + to] = _makeconverter(fr, to)
  text = conv(text)
  text = text.replace('ッ', 'っ')
  return text

# unicode -> unicode

def hira2en(text): return _repair_reading(_repair_en(_convert(text, 'hira', 'en')))
def kata2en(text): return _repair_reading(_repair_en(_convert(text, 'kata', 'en')))
def kana2en(text): return _repair_reading(_repair_en(_convert(text, 'kana', 'en')))

def hira2ru(text): return _repair_reading(_repair_ru(_convert(text, 'hira', 'ru')))
def kata2ru(text): return _repair_reading(_repair_ru(_convert(text, 'kata', 'ru')))
def kana2ru(text): return _repair_reading(_repair_ru(_convert(text, 'kana', 'ru')))

def hira2uk(text): return _repair_reading(_repair_uk(_convert(text, 'hira', 'uk')))
def kata2uk(text): return _repair_reading(_repair_uk(_convert(text, 'kata', 'uk')))
def kana2uk(text): return _repair_reading(_repair_uk(_convert(text, 'kana', 'uk')))

def hira2el(text): return _repair_reading(_repair_el(_convert(text, 'hira', 'el')))
def kata2el(text): return _repair_reading(_repair_el(_convert(text, 'kata', 'el')))
def kana2el(text): return _repair_reading(_repair_el(_convert(text, 'kana', 'el')))

def hira2th(text): return _repair_reading(_repair_th(_convert(text, 'hira', 'th')))
def kata2th(text): return _repair_reading(_repair_th(_convert(text, 'kata', 'th')))
def kana2th(text): return _repair_reading(_repair_th(_convert(text, 'kana', 'th')))

def hira2ko(text): return _repair_reading(_repair_ko(_convert(text, 'hira', 'ko')))
def kata2ko(text): return _repair_reading(_repair_ko(_convert(text, 'kata', 'ko')))
def kana2ko(text): return _repair_reading(_repair_ko(_convert(text, 'kana', 'ko')))

def hira2ar(text): return _repair_reading(_convert(text, 'hira', 'ar'))
def kata2ar(text): return _repair_reading(_convert(text, 'kata', 'ar'))
def kana2ar(text): return _repair_reading(_convert(text, 'kana', 'ar'))

hira2romaji = hira2en
kata2romaji = kata2en
kana2romaji = kana2en

def _repair_reading(text):
  """
  @param  text
  @return  unicode
  """
  text = text.replace('ー', '-')
  text = text.replace('っ', '-')
  return text

_re_en_tsu = re.compile(r"っ([bcdfghjklmnprstvxz])")
def _repair_en(text): # unicode -> unicode  repair xtu
  """
  @param  text
  @return  unicode
  """
  if 'っ' in text:
    text = _re_en_tsu.sub(r'\1\1', text).replace('っ', '-')
  return text

# http://en.wikipedia.org/wiki/Russian_alphabet
_ru_i_vowel = "ауэояё" # vowel except "и"
_ru_consonant = "бвгдзклмнпрстфхцчшщъыь"
_re_ru_i = re.compile(r"(?<=[%s])и" % _ru_i_vowel)
_re_ru_ii = re.compile(r"[ий](и+)")
_re_ru_z = re.compile(r'\bз', re.UNICODE)
_re_ru_tsu = re.compile(r"っ([%s])" % _ru_consonant)
def _repair_ru(text): # unicode -> unicode  repair xtu
  """
  @param  text
  @return  unicode
  """
  if 'っ' in text:
    text = _re_ru_tsu.sub(r'\1\1', text)
  if 'и' in text:
    text = _re_ru_i.sub('й', text)
    text = _re_ru_ii.sub(r'\1й', text) # push i to the end
  if 'з' in text:
    text = _re_ru_z.sub('дз', text)
  return text

# http://en.wikipedia.org/wiki/Ukrainian_alphabet
_uk_i_vowel = _ru_i_vowel + 'еї' # vowel except "і"
_uk_consonant = _ru_consonant + 'ґ'
_re_macron_uk_tsu = re.compile(r"っ([%s])" % _uk_consonant)
_re_macron_uk_i = re.compile(r"(?<=[%s])і" % _uk_i_vowel)
_re_macron_uk_ii = re.compile(r"[ії](і+)")
def _repair_uk(text): # unicode -> unicode  repair xtu
  """
  @param  text
  @return  unicode
  """
  if 'っ' in text:
    text = _re_macron_uk_tsu.sub(r'\1\1', text)
  if 'і' in text:
    text = _re_macron_uk_i.sub('ї', text)
    text = _re_macron_uk_ii.sub(r'\1ї', text) # push i to the end
  return text

# http://en.wikipedia.org/wiki/Greek_alphabet
_el_consonant = 'βγδζθκλμνξπρτφχψω'
_re_el_tsu = re.compile(r"っ([%s])" % _el_consonant)
def _repair_el(text): # unicode -> unicode  repair xtu
  """
  @param  text
  @return  unicode
  """
  if 'っ' in text:
    text = _re_el_tsu.sub(r'\1\1', text)
  return text

# http://en.wikipedia.org/wiki/Thai_alphabet
# Thai unicode range: U+0E00–U+0E7F
_th_b = '(?:^|(?<![\u0e00-\u0e7f]))' # \b at the beginning
_th_e = '(?:$|(?![\u0e00-\u0e7f]))' # \e at the beginning
_re_th = (
  (re.compile(_th_b + 'ก'), 'ค'), # k
  #(re.compile(_th_b + u'จิ'), u'ชิ'), # chi
  (re.compile(_th_b + 'ตา'), 'ทา'), # ta
  #(re.compile(_th_b + ur"ย์"), u'อิ'), # i => yi
  (re.compile(_th_b + r"ย์"), 'อี'), # i => yi
  (re.compile(r"คุ" + _th_e), 'ขุ'), # ku
  (re.compile(r"า" + _th_e), 'ะ'),  # a
  (re.compile("คะ" + _th_e), 'กะ'), # ka (after applying a)
  (re.compile(r"([โเ][กรตน])" + _th_e), r'\1ะ'), # oe
)
def _repair_th(text):
  """
  @param  text
  @return  unicode
  """
  #return text
  for pat, repl in _re_th:
    text = pat.sub(repl, text)
  return text

# http://en.wikipedia.org/wiki/Hangul_Syllables
#_re_ko_tsu2 = re.compile(_ko_hangul + u'っ' + _ko_hangul)
#def _ko_tsu2_repl(m): # match -> unicode
#  t = m.group()
#  left = t[0]
#  right = t[-1]
#  from hangulconv import hangulconv
#  left_l = hangulconv.split_char(left)
#  right_l = hangulconv.split_char(right)
#
#  if left_l and right_l and len(left_l) == 2:
#    left_l = left_l[0], left_l[1], right_l[0]
#    left = hangulconv.join_char(left_l)
#    if left:
#      t = left + right
#  return t
#_re_ko_tsu1 = re.compile(u'っ' + _ko_hangul)
#def _ko_tsu1_repl(m): # match -> unicode
#  t = m.group()
#  left = t[0]
#  right = t[-1]
#  from hangulconv import hangulconv
#  right_l = hangulconv.split_char(right)
#
#  if right_l:
#    right_ch = right_l[0]
#    right_ch = hangulconv.join_consonant((right_ch, right_ch))
#    if right_ch:
#      right_l = list(right_l)
#      right_l[0] = right_ch
#      right = hangulconv.join_char(right_l)
#      t = right
#  return t
# http://en.wikipedia.org/wiki/Template:Unicode_chart_Hangul_Syllables
# http://en.wikipedia.org/wiki/Hangul_consonant_and_vowel_tables
_ko_hangul = '[\uac00-\ud7a3]' # all 2~3 hangul syllables
_re_ko_tsu = re.compile(_ko_hangul + 'っ')
def _ko_tsu_repl(m): # match -> unicode
  t = m.group()
  left = ord(t[0])
  if (left - 0xac00) % 28 == 0:
    t = chr(left + 19) # 19 is ㅅ
  #from hangulconv import hangulconv
  #left_l = hangulconv.split_char(left)
  #if left_l and len(left_l) == 2:
  #  left_l = left_l[0], left_l[1], u'ㅅ' #right_l[0]
  #  left = hangulconv.join_char(left_l)
  #  if left:
  #    t = left
  return t
def _repair_ko(text):
  """
  @param  text
  @return  unicode
  """
  if 'っ' in text:
    text = _re_ko_tsu.sub(_ko_tsu_repl, text)
  text = text.replace('っ', 'ㅅ')
  # Disabled as not quite useful
  #if u'っ' in text:
  #  text = _re_ko_tsu1.sub(_ko_tsu1_repl, text)
  return text

# Names

def kana2reading(text, lang, capital=True):
  """
  @param  text  unicode
  @param  lang  str
  @param* capital  bool
  @return  unicode or None
  """
  if lang == 'ko':
    text = kana2ko(text)
    text = text.replace('っ', '')
    text = text.replace('ッ', '')
    return text
  elif lang == 'th':
    text = text.replace('っ', '')
    text = text.replace('ッ', '')
    text = text.replace('おお', 'お')
    return kana2th(text)
  elif lang == 'ar':
    if 'ゆ' in text:
      text = text.replace('ゆう', 'ゆ')
      text = text.replace('ゆぅ', 'ゆ')
    return kana2ar(text)
  elif lang == 'ru':
    text = kana2ru(text)
  elif lang == 'uk':
    text = kana2uk(text)
  elif lang == 'el':
    text = kana2el(text)
  else:
    text = kana2romaji(text)
  if capital:
    text = capitalizeromaji(text)
  return text

def kana2name(text, lang, macron=None):
  """
  @param  text  unicode
  @param  lang  str
  @param* macron  bool
  @return  unicode
  """
  macron = _lang_is_latin(lang) and (OPT_NAME_MACRON if macron is None else macron)
  if macron:
    text = _convert_macron_before(text)
  text = _remove_macron(text)
  text = kana2reading(text, lang, capital=False)
  if macron:
    text = _convert_macron_after(text)
  if _lang_has_capital(lang):
    text = capitalizeromaji(text)
  return text

_re_capitalize = multireplacer({
  #' Da ': ' da ',
  ' De ': ' de ',
  ' Ha ': ' ha ',
  ' Na ': ' na ',
  ' No ': ' no ',
  ' Ni ': ' ni ',
  ' To ': ' to ',
  #' O ': ' o ',
  ' Wo ': ' wo ',
})
def capitalizeromaji(text):
  """
  @param  text  unicode
  @return  unicode
  """
  return _re_capitalize(text.title())

_macron_u_prefix = "\
おこそとのほもよろを\
ごぞどぼぽ\
ょ\
ゅ\
"
_re_macron_u = re.compile(r"(?<=[%s])う" % _macron_u_prefix)
_macron_o_prefix = "とど"
_re_macron_o = re.compile(r"(?<=[%s])お" % _macron_o_prefix)
def _remove_macron(text):
  """
  @param  text  unicode
  @return  unicode
  """
  text = text.replace("ー", '')
  if text and len(text) > 3 and 'う' in text:
    text = _re_macron_u.sub('', text)
  if text and len(text) > 3 and 'お' in text:
    text = _re_macron_o.sub('', text)
  return text

# http://en.wikipedia.org/wiki/Romanization_of_Japanese
# http://en.wikipedia.org/wiki/Hepburn_romanization
# http://en.wikipedia.org/wiki/Macron
#
# Use '〜' as intermediate character for long sound
def _convert_macron_before(text):
  """
  @param  text  unicode
  @return  unicode
  """
  if len(text) <= 2:
    return text
  text = text.replace("ー", '〜') or text
  if 'う' in text:
    text = _re_macron_u.sub('〜', text)
  if 'お' in text:
    text = _re_macron_o.sub('〜', text)
  return text

def _make_latin_macrons():
  ret = {
    'a': 'ā',
    'e': 'ē',
    'i': 'ī',
    'o': 'ō',
    'u': 'ū',
  }
  for k,v in list(ret.items()):
    ret[k.upper()] = v.upper()
  return ret
LATIN_MACRONS = _make_latin_macrons()
_re_macron_vowel = re.compile('[aeiouAEIOU]〜')
def _re_macron_vowel_repl(m):
  return LATIN_MACRONS[m.group()[0]]
def _convert_macron_after(text):
  """
  @param  text  unicode
  @return  unicode
  """
  if '〜' not in text:
    return text
  text = _re_macron_vowel.sub(_re_macron_vowel_repl, text)
  return text.replace('〜', '') or text

if __name__ == '__main__':
  #t = u"ウェブサイトツール"
  #t = u"うぇぶさいとつーる"
  #t = u"わかってる"
  t = 'さくらこうじ'
  print(hira2romaji(t))
  #print kata2romaji(t)
  #print kata2hira(t)
  #print hira2kata(t)
  #print kata2ko(t)
  print(kana2ko(t))
  print(kana2th(t))

  from jTransliterate import JapaneseTransliterator
  def test(text):
    return JapaneseTransliterator(text).transliterate_from_hrkt_to_latn()
  print(test(t))

  t = 'イイズミ-ちゃん'
  print(kana2ru(t)) # ийдзуми-чан, supposed to be Иизуми-чан
  t = 'ぱっつぁん'
  print(hira2ko(t))
  print(hira2romaji(t))
  print(hira2ru(t))

  t = 'みなとそふと'
  print(hira2ru(t))
  t = 'ソフトクリーム'
  print(kata2ru(t)) # correct translation is Софуто-куриму

  # Romaji
  l = [
    ('かわいい', 'kawaii'),
    ('いぇす', 'yesu'),
    ('ジャケット', 'jaketto'),
    ('せんせい', 'sensei'),
    ('ちゃん', 'chan'),
    ('ちょうきょう', 'choukyou'),
    ('ぐりぐり', 'guriguri'),
  ]
  for k,v in l:
    print(k, kana2en(k), v)
    assert kana2en(k) == v

  # Romaji with Macron
  l = [
    ('さとう', 'Satō'),
    ('りゅうくん', 'Ryūkun'),
    ('ゆうま', 'Yuuma'),
    ('そう', 'Sou'),
    ('そう', 'Sou'),
  ]
  for k,v in l:
    t = kana2name(k, 'en')
    print(k, t, v)
    assert t == v

  # Russian
  l = [
    ('かわいい', 'каваий'), # http://ru.wikipedia.org/wiki/каваий
    ('じい', 'дзий'), # not sure
    ('いぇす', 'иэсу'), # not sure
    ('ジャケット', 'дзякэтто'),
    ('せんせい', 'сэнсэй'),
    ('ちゃん', 'чан'),
    ('いえやす', 'иэясу'),
    #(u'サシャ', u'саша'), # wrong, got сася
    #(u'ちょうきょう', u'чоукёу'), # not sure
  ]
  for k,v in l:
    print(k, kana2ru(k), v)
    assert kana2ru(k) == v

  # Ukrainian
  l = [
    ('くん', 'кун'),
    ('いえやす', 'іеясу'),
    ('ほのか', 'гонока'),
    ('ほのっか', 'гонокка'),
    ('かわいい', 'каваії'),
    ('せんせい', 'сенсеї'),
    ('れん', 'рен'),
  ]
  for k,v in l:
    print(k, kana2uk(k), v)
    assert kana2uk(k) == v

  # Greek
  l = [
    ('かわいい', 'καωαιι'), # not sure how to say it
    #(u'こんと', u'κόντο'), # failed
    #(u'たろ', u'ταρό'), # failed
    #(u'やまた', u'γιαμάντα'), # failed
    # http://el.wikipedia.org/wiki/Ιαπωνική_γραφή
    ('イロハニホヘト', 'ιροχανιχοχετο'),  # 色は匂へと
    #(u'チリヌルヲ',  u'τσιρινουρουβο'),     # 散りぬるを failed since を is translated to ωο instead of βο
    #(u'ワカヨタレソ', u'βακαγιοταρεσο'),    # 我が世誰そ failed
    ('ツネナラム', 'τσουνεναραμου'),      # 常ならむ
    #(u'ウヰノオクヤマ', u'ουβινοοκουγιαμα'), # 有為の奥山
    ('ケフコエテ', 'κεφουκοετε'),         # 今日越えて
    ('アサキユメミシ', 'ασακιγιουμεμισι'), # 浅き夢見し
    #(u'ヱヒモセス', u'βεχιμοσεσου'),        # 酔ひもせす
  ]
  for k,v in l:
    print(k, kana2el(k), v)
    assert kana2el(k) == v

  # Korean
  l = [
    ('しおり', '시오리'),
    ('いぇす', '예스'),
    ('しっば', '싯바'),
    ('ゆっき', '윳키'),
    ('ゆっさ', '윳사'),
    ('かって', '캇테'),
    ('って', 'ㅅ테'),
    ('ゆりっぺ', '유릿페'),
    ('ゆりっっぺ', '유릿ㅅ페'),
    #(u'っさ', u'싸'), # disabled as not quite useful
  ]
  for k,v in l:
    print(k, kana2ko(k), v)
    assert kana2ko(k) == v
    assert kana2name(k, 'ko') == v

  # Thai
  l = [
    #(u'すず', u'ซูซุ'), fail
    #(u'すすら', u'ซึซึระ'), # fail
    #(u'すずしろ', u'ซุสึชิโระ'), # fail
    #(u'すずかけ', u'สุซึคาเคะ'), # fail because すす => すず
    #(u'いすず', u'อีซูซุ'),
    ('ちはや', 'จิฮายะ'),
    ('すかもり', 'สึคาโมริ'),
    ('たにゃ', 'ทาเนีย'),
    ('みかづき', 'มิคาซึกิ'),
    ('つぐみ', 'สึกุมิ'),
    ('かなり', 'คานาริ'),
    ('ましろ', 'มาชิโระ'),
    ('まどか', 'มาโดกะ'),
    ('かのん', 'คาน่อน'),
    ('まゆ', 'มายุ'),
    ('けせん', 'เคเซน'),
    #(u'ちばな', u'ชิบานะ'), # fail because of chi
    ('きさき', 'คิซากิ'),
    ('みやこ', 'มิยาโกะ'),
    ('ふじな', 'ฟุจินะ'),
    ('ひろはら', 'ฮิโรฮาระ'),
    ('さぎばら', 'ซาคิบาระ'),
    ('まる', 'มารุ'),
    ('おてんた', 'โอเท็นตะ'),
    ('むねちか', 'มุเนะจิกะ'),
    ('くろば', 'คุโรบะ'),
    ('けい', 'เคย์'),
    ('さねあき', 'ซาเนะอากิ'),
    ('はるかぜ', 'ฮารุคาเซะ'),
    ('きぬむら','คินุมุระ'),
    ('れんな', 'เร็นนะ'),
    #(u'はさくら', u'ฮาซากุระ'), # fail because of ku
    ('れんか', 'เร็นกะ'),
    ('りん', 'ริน'),
    ('みなもり', 'มินาโมริ'),
    ('ほのか', 'โฮโนกะ'),
    ('あやめ', 'อายาเมะ'),
    ('たくや', 'ทาคุยะ'),
    ('みうら', 'มิอุระ'), # http://th.wikipedia.org/wiki/เดป้าเปเป้
    ('よしなり', 'โยชินาริ'),
    ('とくおか', 'โทคุโอกะ'),
    ('まえだ', 'มาเอดะ'),
    ('ふうちゃん', 'ฟูจัง'), # http://th.wikipedia.org/wiki/รักลวงป่วนใจ
    ('ゆうま', 'ยูมะ'),
    ('とうこ', 'โทวโกะ'),
    #(u'つきの', u'สึคิโนะ'), # fail because of ki
    #(u'てんまく', u'เทนมาขุ'), # fail because of te
    #(u'えんにし', u'เอนิชิ'), # fail because ennishi => enishi
    #美愛: u'มิจิกะ
    #かがみ: คางามิ
    #幸和: ซาจิคาซุ
    #一悟: อิจิโกะ
    #左京: ซาเคียว
    #みずのみや: มิซุโนะมิยะ
    #冬馬: โทวมะ
  ]
  for k,v in l:
    print(k, hira2th(k), v)
    assert kana2th(k) == v

  # Arabic
  l = [
    ('さくら', 'ساكورا'),
    ('さと', 'ساتو'),
    ('かがみ', 'كاغامي'),
    ('かおる', 'كاورو'),
    ('さい', 'ساي'),
    ('さいと', 'سايتو'),
    ('やまだ', 'يامادا'),
    ('やまもと', 'ياماموتو'),
    ('なかむら', 'ناكامورا'),
    ('ふくだ', 'فوكودا'),
    ('さと', 'ساتو'),
    ('まつもと', 'ماتسوموتو'),
    ('かよ', 'كايو'),
    ('ぐれん', 'غورين'),
    ('しんご', 'شينغو'),
    ('すざく', 'سوزاكو'),
    ('となり の ととろ', 'توناري نو توتورو'),
    ('さおり', 'ساوري'),
    ('ゆうま', 'يوما'),
    ('かわいい', 'كاوايي'),
    ('ちゃん', 'تشان'),
    ('さま', 'ساما'),
    ('シャナ', 'شانا'),
    ('ぴこ', 'بيكو'),
    ('ぺこ', 'بيكو'),
    ('べこ', 'بيكو'),
    ('ボコ', 'بوكو'),
    ('さど', 'سادو'),
    ('ぱぴ', 'بابي'),
    ('かぶと', 'كابوتو'),
    ('つばさ', 'تسوباسا'),
    ('さすけ', 'ساسوكي'),
    ('あゆみ', 'ايومي'),
    ('めぐみ', 'ميغومي'),
    ('かおる', 'كاورو'),
    ('わだ', 'وادا'),
    ('あべ', 'ابي'),
    #(u'えいじ', u'إيجي'), # failed, totally wrong
    #(u'ぜん', u'زن'), # failed because zen is not handled
    #(u'かな', u'قانا'), # failed because of wrong ka
  ]
  for k,v in l:
    print(k, kana2name(k, 'ar'), v)
    assert kana2name(k, 'ar') == v

# EOF

## See: http://pypi.python.org/pypi/jTransliterate
#
#kata2romaji = kana2romaji
#hira2romaji = kana2romaji
