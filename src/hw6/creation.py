import math
import re

def COL(n, s):
  col = NUM(n, s) if re.search("^[A-Z]+", s) else SYM(n, s)
  col['isIgnored'] = re.search("X$", col['txt'])
  col['isKlass'] = re.search("!$", col['txt'])
  col['isGoal'] = re.search("[!+-]$", col['txt'])
  return col


def NUM(n=None, s=None):
  return {
    'at': n or 0,
    'txt': s or "",
    'n': 0,
    'hi': -math.inf,
    'lo': math.inf,
    'ok': True,
    'has': [],
    'w': -1 if re.search("-$", (s or "")) else 1
  }

def SYM(n=None, s=None):
  return {
    'at': n or 0,
    'txt': s or "",
    'n': 0,
    'mode': None,
    'most': 0,
    'isSym': True,
    'has': {}
  }

def COLS(ss):
  cols = {
    'names': ss,
    'all': [],
    'x': [],
    'y': []
  }

  for n, s in enumerate(ss):
    col = COL(n, s)
    cols['all'].append(col)
    
    if not col['isIgnored']:
      if col['isKlass']:
        cols['klass'] = col
      if col['isGoal']:
        cols['y'].append(col)
      else:
        cols['x'].append(col)
      # col.append(cols['y'] if col['isGoal'] else cols['x'], col)

  return cols

class DATA:
  def __init__(self):
    return {
      'rows': [],
      'cols': None
    }

  def new():
    return {
      'rows': [],
      'cols': None
    }

  def read(sfile):
    data = DATA.new()
    def func(t):
      from update import row
      row(data, t)
    from utils import csv
    csv(sfile, func)
    return data
  
  def clone(data, ts=[]):
    from update import row
    data1 = row(DATA.new(), data['cols']['names'])
    for t in ts:
      row(data1, t)
    return data1

def RANGE(at, txt, lo, hi=None):
  return {
    'at': at,
    'txt': txt,
    'lo': lo,
    'hi': hi or lo,
    'y': SYM()
  }

def RULE(ranges, maxSize):
  t = {}
  for range in ranges:
    if range['txt'] not in t:
      t[range['txt']] = []
    (t[range['txt']]).append({'lo':range['lo'], 'hi':range['hi'], 'at':range['at']})
  return prune(t, maxSize)

def prune(rule, maxSize):
  n = 0
  for txt, ranges in enumerate(rule):
    n += 1
    if len(ranges) == maxSize['txt']:
      n += 1
      rule['txt'] = None
  if n > 0:
    return rule