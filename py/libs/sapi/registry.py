# coding: utf8
# registry.py
# 4/7/2013 jichi

if __name__ == '__main__': # debug
  import sys
  sys.path.append("..")

from sakurakit import skstr
from sakurakit.skclass import memoized
from sakurakit.skdebug import dprint, dwarn
from sakurakit.skunicode import u
from windefs import winlocale

SAPI_HKCU_PATH = r"SOFTWARE\Microsoft\Speech\Voices\TokenEnums"
SAPI_HKLM_PATH = r"SOFTWARE\Microsoft\Speech\Voices\Tokens"

def _parselang(lcid):
  """
  @param  lcid  int
  @return  str
  """
  try: return winlocale.lcid2locale(lcid)[:2] # only keep the first 2 characters
  except Exception as e:
    dwarn(e)
    return ''

_GENDERS = {
 'Female': 'f',
 'Male': 'm',
}
def _parsegender(g):
  """
  @param  g  str
  @return  str
  """
  return _GENDERS.get(g) or ''

def exists(path, hk):
  """
  @param  hk  str
  @param  path  str
  @return  bool
  """
  import winreg
  try:
    with winreg.ConnectRegistry(None, getattr(_winreg, hk)) as reg: # None = computer_name
      with winreg.OpenKey(reg, path):
        return True
  except: return False

@memoized
def get():
  """
  @return  [{kw}] not None
  """
  #REG = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens"

  ret = []
  import winreg
  for (hk,path) in (
      (winreg.HKEY_LOCAL_MACHINE, SAPI_HKLM_PATH),
      (winreg.HKEY_CURRENT_USER, SAPI_HKCU_PATH),
    ):
    try:
      with winreg.ConnectRegistry(None, hk) as reg: # None = computer_name
        with winreg.OpenKey(reg, path) as rootkey:
          nsubkeys = winreg.QueryInfoKey(rootkey)[0]
          for i in range(nsubkeys):
            try:
              voicekeyname = winreg.EnumKey(rootkey, i)
              dprint("sapi key: %s" % voicekeyname)
              with winreg.OpenKey(rootkey, voicekeyname) as voicekey:
                clsid = winreg.QueryValueEx(voicekey, 'CLSID')[0]
                try: location = winreg.QueryValueEx(voicekey, 'VoiceData')[0]
                except WindowsError:
                  try: location = winreg.QueryValueEx(voicekey, 'VoicePath')[0]
                  except WindowsError:
                    location = ""
                with winreg.OpenKey(voicekey, 'Attributes') as attrkey:
                  # ja: "411", en_US: "409:9"
                  language = winreg.QueryValueEx(attrkey, 'Language')[0]
                  lcid = int(language.split(';', 1)[0], 16) # such as '411;9' where 411 => 0x411
                  age = winreg.QueryValueEx(attrkey, 'Age')[0]
                  gender = winreg.QueryValueEx(attrkey, 'Gender')[0]
                  name = winreg.QueryValueEx(attrkey, 'Name')[0]
                  vendor = winreg.QueryValueEx(attrkey, 'Vendor')[0]
                  uk = u(voicekeyname) # convert to u8 using native encoding
                  if uk:
                    ret.append({
                      'key': uk,
                      'clsid': clsid, # str
                      'location': u(location), # unicode
                      'age': age, # str
                      #'name': u(name), # unicode
                      'name': name, # use str instead
                      'vendor': u(vendor), # unicode
                      'lcid': lcid, # long
                      'language': _parselang(lcid), #
                      'gender': _parsegender(gender), #
                    })
                  else:
                    dwarn("failed to convert registry key to unicode: %s" % voicekeyname)
            except WindowsError as e:
              dwarn(e)
            except (ValueError, TypeError) as e:  # failed to convert lcid to long
              dwarn(e)
    except WindowsError as e:
      dprint(e)
  return ret

def querylist(language=''):
  """
  @param  language  str
  @return  [kw] not None
  """
  ret = []
  for it in get():
    if not language or language == it['language']:
      ret.append(it)
  return ret

def query(key=''):
  """
  @param  key  str
  @return  kw or None
  """
  if key:
    for it in get():
      if key == it['key']:
        return it

if __name__ == '__main__': # debug
  print(get())

# EOF

#class WinTtsVoice(object):
#  def __init__(self, key="", clsid="", location="", name="", vendor="", lcid=0, gender="", age=""):
#    self.key = key # unicode, registry key
#    self.location = location # unicode path, VoiceData
#    self.clsid = clsid    # str
#    self.lcid = lcid      # int, such as 411 for Japanese
#
#    self.name = name      # unicode, Attributes.Name
#    self.vendor = vendor  # unicode, Attributes.Vendor
#    self.gender = gender  # unicode, Male or Female
#    self.age = age        # unicode, such as Adult
#
#  @property
#  def language(self):
#    """
#    @return  str not None
#    """
#    return LCID_LANG.get(self.lcid) or ''

