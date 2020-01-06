# coding: utf8
# app.py
# 12/13/2012 jichi

__all__ = 'Application',

from PySide2.QtCore import QTranslator
from Qt5.QtWidgets import QApplication
from sakurakit.skdebug import dprint, dwarn
import config, rc

class Application(QApplication):
  def __init__(self, argv):
    super(Application, self).__init__(argv)

    self.setApplicationName("Website Reader")
    self.setApplicationVersion(str(config.VERSION_TIMESTAMP))
    self.setOrganizationName(config.VERSION_ORGANIZATION)
    self.setOrganizationDomain(config.VERSION_DOMAIN)
    self.setWindowIcon(rc.icon('logo-browser'))

    dprint("pass")

  def loadTranslations(self):
    """加载yaml里的Qt翻译路径并安装"""
    locale = self.applicationLocale()
    #if locale in config.TR_LOCALES:
    dprint("loading translation for %s" % locale)

    t = QTranslator(self)
    ok = t.load('qt_%s' % locale, config.QT_TRANSLATIONS_LOCATION)
    #assert ok, "failed to load qt translation"
    if ok:
      self.installTranslator(t)
    else:
      location = config.QT_TRANSLATIONS_LOCATION
      dprint("cannot find translation at %s" % location)

    for location in config.TR_LOCATIONS:
      t = QTranslator(self)
      ok = t.load(locale, location)
      #assert ok, "failed to load translation"
      if ok:
        self.installTranslator(t)
      else:
        dprint("cannot find translation at %s" % location)

  @staticmethod
  def applicationLocale():
    import settings
    lang = settings.reader().userLanguage()
    locale = config.language2locale(lang)
    return locale

# EOF
