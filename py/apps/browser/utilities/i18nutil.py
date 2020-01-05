# coding: utf8
# i18nutil.py
# 10/8/2012 jichi

# Datetime

from datetime import datetime

WEEK_NAMES = [
  "日",
  "月",
  "火",
  "水",
  "木",
  "金",
  "土",
]

def unparsedatetime(d):
  #return d.strftime("%m/%d/%Y {0} %H:%M").format(
  #    WEEK_NAMES[d.weekday()]).lstrip('0')
  return "%s/%s/%s %s %s:%s" % (
      d.month, d.day, d.year,
      WEEK_NAMES[d.weekday()],
      d.hour, d.minute)

def unparsedate(d):
  """
  @param  sec  long
  @return  str
  """
  return "%s/%s/%s %s" % (
      d.month, d.day, d.year,
      WEEK_NAMES[d.weekday()])

def timestamp2datetime(sec):
  """
  @param  sec  long
  @return  str
  """
  return unparsedatetime(datetime.fromtimestamp(sec))

def timestamp2date(sec):
  """
  @param  sec  long
  @return  str
  """
  return unparsedate(datetime.fromtimestamp(sec))

# EOF
