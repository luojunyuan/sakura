# coding: utf8
# termview.py
# 1/10/2015 jichi

from sakurakit.skdebug import dprint, dwarn
from PySide2.QtCore import QObject, Signal, Slot

class TermViewBean(QObject):

  instance = None

  searchText = None # unicode or None
  searchCol = None # unicode or None
  searchLanguage = None # unicode or None

  def __init__(self, parent=None):
    super(TermViewBean, self).__init__(parent)
    TermViewBean.instance = self
    dprint("pass")

  searchRequested = Signal(str, str, str) # text, col, language

  @Slot(result=str)
  def getSearchText(self): return self.searchText
  @Slot(result=str)
  def getSearchCol(self): return self.searchCol
  @Slot(result=str)
  def getSearchLanguage(self): return self.searchLanguage

def search(text="", col="", language=""):
  """
  @param* text  unicode
  @param* col  str
  @param* language  str
  """
  if TermViewBean.instance: # width & height are ignored
    TermViewBean.instance.searchRequested.emit(text, col, language)
  else:
    TermViewBean.searchText = text
    TermViewBean.searchCol = col
    TermViewBean.searchLanguage = language

    dwarn("termview is not ready")

# EOF
