# coding: utf8
# zhja.py
# 9/21/2014: jichi
# See: http://www.jcdic.com/chinese_convert/index.php

#JT = dict(zip(J, T)) # {unicode:unicode}
#TJ = dict(zip(T, J)) # {unicode:unicode}
TJ = {
  # Equivalent conversion
  "—": "ー",

  "誒": "欸",
  "內": "内",
  "晚": "晩",
  "說": "説",
  "悅": "悦",
  "蔥": "葱",
  "擊": "撃",
  "絕": "絶",
  "佈": "布",
  "幫": "幇",
  "雞": "鶏",
  "歲": "歳",
  "咖": "珈",
  "啡": "琲",
  "僱": "雇",
  "錄": "録",
  "莆": "蒲",
  "虛": "虚",
  "醬": "醤",
  "眾": "衆",
  "團": "団",
  "溫": "温",
  "狀": "状",
  "麽": "麼",
  "查": "査",
  "姬": "姫",
  "惠": "恵",
  "德": "徳",
  "綠": "緑",
  "沉": "沈",

  # To simplified version
  #u"號": u"号",
  #u"體": u"体",
  "遙": "遥",

  # Wide text

  #u"你": u"ｲ尓",
  #u"妳": u"ｲ尓",
  #u"謊": u"言荒",
  #u"哪": u"ﾛ那",
  #u"啪": u"ﾛ拍",
  #u"喵": u"ﾛ苗",
  #u"咕": u"ﾛ古",
  #u"噜": u"ﾛ魯",
  #u"吵": u"ﾛ少",
  #u"瞄": u"目苗",

  #u"她": u"他",

  #u"脖": u"月孛",

  # Inequivalent conversion
  #u"呢": u"吶",
  #u"啊": u"哦",
  #u"噢": u"哦",
  #u"喲": u"哦",
  #u"喔": u"哦",
  #u"啦": u"吶",
  #u"哎": u"欸",
  #u"呃": u"額",
  #u"嗎": u"麼",

  #u"吧": u"吶",
  #u"嗯": u"恩",
  #u"噗": u"璞",
  #u"呲": u"兹",
  #u"嘟": u"都",
  #u"噥": u"農",

  #u"筷": u"快",
  #u"爸": u"粑",
  #u"桌": u"卓",
  #u"夠": u"構",

  #u"凳": u"椅", # 凳子
  #u"糰": u"団", # おにぎり
  #u"碟": u"盤", # 碟子

  #u"辦": u"做", # 办法、怎么办
}

#def zhs2ja(s): # unicode -> unicode

def zht2ja(t): # unicode -> unicode
  return ''.join((TJ.get(c) or c for c in t))

if __name__ == '__main__':
  ja = "壹周刊:施明德說，目前藍綠惡鬥致使台灣無法變"
  zh = zht2ja(ja)
  print("歲"== "歳")
  print("內"== "内")
  print("晚" == "晩")
  print("虛" == "虚")
  print("查" == "査")

  from PySide2.QtCore import *
  c = QTextCodec.codecForName('sjis')
  t = c.toUnicode(c.fromUnicode(zh))
  print(t)

# EOF
