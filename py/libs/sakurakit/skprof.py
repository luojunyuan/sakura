# coding: utf8
# skprof.py
# 1/16/2014 jichi
#
# http://preshing.com/20110924/timing-your-code-using-pythons-with-statement/

import time
from . import skdebug

class SkProfiler(object):
  def __init__(self, text=None, verbose=skdebug.DEBUG):
    self.verbose = verbose # bool
    self.text = text # str, or anything that can be printed

  def __enter__(self):
    self.start()
    return self

  def __exit__(self, *args):
    self.stop()

  def start(self):
    self.starttime = time.clock()

  def stop(self):
    self.endtime = time.clock()
    self.interval = self.endtime - self.starttime
    if self.verbose:
      if self.text is not None:
        msg = "prof time: %s = %s sec" % (self.text, self.interval)
      else:
        msg = "prof time: %s sec" % self.interval
      skdebug.dprint(msg)

if __name__ == '__main__':
  count = 1
  size = 100000 * 20
  text = "日本語で"
  table = {str(k):'test' for k in range(0, size)}

  print("replace")
  with SkProfiler():
    for i in range(0, count):
      for k,v in table.items():
        text = text.replace(k, v)

  from . import skstr
  print("prepare")
  with SkProfiler():
    repl = skstr.multireplacer(table)
  print("apply")
  with SkProfiler():
    for i in range(0, count):
      text = repl(text)

# EOF
