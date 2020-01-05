# coding: utf8
# growl.py
# 10/28/2012 jichi

from PySide2.QtCore import Signal, Qt, QObject

class GrowlBean(QObject):

  instance = None

  def __init__(self, parent=None):
    super(GrowlBean, self).__init__(parent)
    GrowlBean.instance = self
    #self.__d = _GrowlBean(self)

    for k in 'message', 'warning', 'error', 'notification', 'pageBreak':
      q = getattr(self, 'q_' + k)
      s = getattr(self, k)
      q.connect(s, Qt.QueuedConnection)

    self.q_pageBreak.connect(self.pageBreak, Qt.QueuedConnection)
    self.q_message.connect(self.message, Qt.QueuedConnection)
    self.q_warning.connect(self.warning, Qt.QueuedConnection)
    self.q_error.connect(self.error, Qt.QueuedConnection)
    self.q_notification.connect(self.notification, Qt.QueuedConnection)
    #dprint("pass")

  ## Sequential signals ##
  message = Signal(str)
  warning = Signal(str)
  error = Signal(str)
  notification = Signal(str)
  pageBreak = Signal()

  ## Queued Signals ##
  q_message = Signal(str)
  q_warning = Signal(str)
  q_error = Signal(str)
  q_notification = Signal(str)
  q_pageBreak = Signal()

def msg(text, _async=False):
  try:
    if _async: GrowlBean.instance.q_message.emit(text)
    else: GrowlBean.instance.message.emit(text)
  except AttributeError: pass

def warn(text, _async=False):
  try:
    if _async: GrowlBean.instance.q_warning.emit(text)
    else: GrowlBean.instance.warning.emit(text)
  except AttributeError: pass

def error(text, _async=False):
  try:
    if _async: GrowlBean.instance.q_error.emit(text)
    else: GrowlBean.instance.error.emit(text)
  except AttributeError: pass

def notify(text, _async=False):
  try:
    if _async: GrowlBean.instance.q_notification.emit(text)
    else: GrowlBean.instance.notification.emit(text)
  except AttributeError: pass

def pageBreak(_async=False):
  try:
    if _async: GrowlBean.instance.q_pageBreak.emit()
    else: GrowlBean.instance.pageBreak.emit()
  except AttributeError: pass

# EOF

#def show(_async=False):
#  try:
#    if _async: GrowlBean.instance.q_show.emit()
#    else: GrowlBean.instance.show.emit()
#  except AttributeError: pass
