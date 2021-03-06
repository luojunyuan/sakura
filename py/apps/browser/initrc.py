# coding: utf8
# initrc.py
# 10/5/2012 jichi
# Note: this file is shared by all apps

import os, sys

#def u_from_native(s):
#  # Following contents are copied from sakurakit.skunicode
#  import locale
#  lc, enc = locale.getdefaultlocale()
#  return s.decode(enc, errors='ignore')
#u = u_from_native

## Helpers ##

def reset_win_path():
  try:
    print("initrc:reset_win_path: enter", file=sys.stderr)
    windir = os.environ['windir'] or os.environ['SystemRoot'] or r"C:\Windows"
    path = os.pathsep.join((
      windir,
      os.path.join(windir, 'System32'),
    ))
    os.environ['PATH'] = path
    print("initrc:reset_win_path: leave", file=sys.stderr)
  except Exception as e:
    print("initrc:reset_win_path: leave, exception =", e, file=sys.stderr)

MB_OK = 0               # win32con.MB_OK
MB_ICONERROR = 0x10     # win32con.MB_ICONERROR
MB_ICONWARNING = 0x30   # win32con.MB_ICONWARNING
def msgbox(text, title, type=MB_OK):
  """A message box independent of pywin32.
  @param  title  str not unicode
  @param  text  str not unicode
  """
  if os.name == 'nt':
    from ctypes import windll
    windll.user32.MessageBoxA(None, text.encode('utf8'), title.encode('utf8'), type)

## Procedures ##

def probemod():
  print("initrc:probemod: enter", file=sys.stderr)
  try: from PySide2 import QtCore
  except ImportError as e:
    print("initrc:probemod: ImportError:", e, file=sys.stderr)
    msgbox("""\
I am sorry that VNR got a severe error on startup m(_ _)m

It seems VNR is corrupted that one of the following files are missing, broken, renamed, or quarantined by antivirus software.
Note that the paths and file names are CASE-SENSITIVE.

    Library/Frameworks/Qt/PySide/QtCore4.dll
    Library/Frameworks/Qt/PySide/QtCore.pyd

I hope if you can turn off your antivirus soft and redownload VNR manually from one of the following:

    Google Drive: http://goo.gl/t31MqY
    Megashares: https://mega.co.nz/#F!g00SQJZS!pm3bAcS6qHotPzJQUT596Q

If VNR is on a NTFS drive, the following post about file permissions might also be helpful:

    http://sakuradite.com/topic/136

Feel free to complain to me (annotcloud@gmail.com) if this error keeps bothering you.

ERROR MESSAGE BEGIN
%s
ERROR MESSAGE END""" % e,
      "VNR Startup Error",
      MB_OK|MB_ICONERROR)
    sys.exit(1)
  except UnicodeDecodeError as e:
    print("initrc:probemod: UnicodeDecodeError:", e, file=sys.stderr)
    msgbox("""\
I am sorry that VNR got a severe error on startup m(_ _)m

It seems that you have UNICODE (non-English) characters in the path to VNR.
Due to technical difficulties, UNICODE path would crash VNR.
I hope if you could try removing UNICODE characters including Japanese, Chinese, etc.

Feel free to complain to me (annotcloud@gmail.com) if this error keeps bothering you.

ERROR MESSAGE BEGIN
%s
ERROR MESSAGE END""" % e,
      "VNR Startup Error",
      MB_OK|MB_ICONERROR)
    sys.exit(1)
  print("initrc:probemod: leave", file=sys.stderr)

#I am sorry that VNR got a severe error on startup m(_ _)m
#It seems that some of the following libraries are missing:
#
#* msvc 2008 sp1 x86 redist:
#  http://www.microsoft.com/download/details.aspx?id=5582
#* msvc 2010 sp1 x86 redist:
#  http://www.microsoft.com/download/details.aspx?id=26999
#
#Feel free to complain to me (annotcloud@gmail.com) if this error keeps bothering you.

def checkintegrity():
  print("initrc:checkintegrity: enter", file=sys.stderr)
  error = None
  import config
  try:
    for it in config.ENV_INTEGRITYPATH:
      if not os.path.exists(it):
        error = "File does not exist: %s" % it
        break
  except Exception as e:
    error = "%s" % e
  if error:
    # Force using ascii encoding
    error = error.encode('ascii', errors='ignore')
    msgbox("""\
I am sorry that VNR got a severe problem on startup m(_ _)m

It seems that some of the files needed by VNR are missing.
Either VNR is corrupted after download, or some files are quarantined by anti-virus soft after update.

I hope if you can turn off your antivirus soft and redownload VNR manually from one of the following:

    Google Drive: http://goo.gl/t31MqY
    Megashares: https://mega.co.nz/#F!g00SQJZS!pm3bAcS6qHotPzJQUT596Q

Feel free to complain to me (annotcloud@gmail.com) if this error keeps bothering you.

ERROR MESSAGE BEGIN
%s
ERROR MESSAGE END""" % error,
      "VNR Integrity Error",
      MB_OK|MB_ICONERROR)
    sys.exit(2)
  print("initrc:checkintegrity: leave", file=sys.stderr)

def initenv():
  print("initrc:initenv: enter", file=sys.stderr)
  # Enforce UTF-8
  # * Reload sys
  #   See: http://hain.jp/index.php/tech-j/2008/01/07/Pythonの文字化け
  # * Create sitecustomize.py
  #   See: http://laugh-labo.blogspot.com/2012/02/sitecustomizepy.html
  #import sys
  #reload(sys) # make 'setdefaultencoding' visible
  #sys.setdefaultencoding('utf8')

  # Add current and parent folder to module path
  mainfile = os.path.abspath(__file__)
  maindir = os.path.dirname(mainfile)

  sys.path.append(maindir)

  if os.name == 'nt':
    reset_win_path()

  # Python chdir is buggy for unicode
  #os.chdir(maindir)

  import config

  # http://stackoverflow.com/questions/196930/how-to-check-if-os-is-vista-in-python
  #import platform
  #if platform.release() == 'XP':
  #  map(sys.path.append, config.ENV_PYTHONPATH_XP)

  #for path in config.ENV_PYTHONPATH:
  #  sys.path.append(path)
  list(map(sys.path.append, config.ENV_PYTHONPATH))
  if hasattr(config, 'APP_PYTHONPATH'):
    list(map(sys.path.append, config.APP_PYTHONPATH))

  paths = os.pathsep.join(config.ENV_PATH)
  try:
    os.environ['PATH'] = paths + os.pathsep + os.environ['PATH']
  except KeyError: # PATH does not exists?!
    os.environ['PATH'] = paths

  if os.name == 'nt' and hasattr(config, 'ENV_MECABRC'):
    assert os.path.exists(config.ENV_MECABRC), "mecabrc does not exist"
    os.putenv('MECABRC',
        config.ENV_MECABRC.replace('/', os.path.sep))
  else:
    print("initrc:initenv: ignore mecabrc")

  #from distutils.sysconfig import get_python_lib
  #sitedir = get_python_lib()
  #pyside_home =sitedir + '/PySide'
  #sys.path.append(pyside_home)

  #python_home = dirname(rootdir) + '/Python'
  #qt_home = dirname(rootdir) + '/Qt'
  #sys.path.append(qt_home + '/bin')

  print("initrc:initenv: leave")

if __name__ == '__main__':
  print("initrc: enter", file=sys.stderr)
  #print __file__
  initenv()
  probemod()
  checkintegrity()

# EOF
