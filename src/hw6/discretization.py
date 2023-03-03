import math
import copy
from creation import RANGE
from config import *
from update import extend, add
from operator import itemgetter
from query import div

def bin(col, x):
  if x == '?' or ('isSym' in col and col['isSym']):
    return x
  tmp = (col['hi'] - col['lo']) / (the['bins'] - 1)
  
  if col['hi'] == col['lo']:
    return 1
  else:
    math.floor(x/tmp + 0.5)*tmp

def bins(cols, rowss):
  out = []
  for col in cols:
    ranges = []
    for y, rows in rowss.items():
      for row in rows:
        x, k = row[col['at']]
        if x != '?':
          k = bin(col, x)
          if(k > len(ranges)):
            for i in range(len(ranges), k):
              ranges.append([])
          ranges[k] = ranges[k] or RANGE(col['at'], col['txt'], x)
          extend(ranges[k], x, y)
    def itself(x):
      return x
    ranges = sorted(map(itself, ranges), itemgetter('lo'))
    
    if 'isSym' in col and col['isSym']:
      out.append(ranges)
    else:
      out.append(mergeAny(ranges))
  return out

def mergeAny(ranges0):
  def noGaps(t):
    for j in range(1, len(t)):
      t[j]['lo'] = t[j-1]['hi']
    t[0]['lo'] = -math.inf
    t[len(t)-1]['hi'] = math.inf
    return t
  ranges1 = []
  j = 0
  while j <= len(ranges0):
    left = ranges0[j]
    right = ranges0[j+1]
    if right:
      y = merge2(left['y'], right['y'])
      if y:
        j += 1
        left['hi'] = right['hi']
        left['y'] = y
    ranges1.append(left)
    j += 1
  if len(ranges0) == len(ranges1):
    return noGaps(ranges0)
  else:
    return mergeAny(ranges1)

def merge2(col1, col2):
  new = merge(col1, col2)
  if div(new) <= (div[col1]*col1['n'] + div(col2)*col2['n'])/new['n']:
    return new

def merge(col1, col2):
  new = copy.deepcopy(col1)
  if col1['isSym']:
    for x, n in col2['has'].items():
      add(new, x, n)
  else:
    for n in col2['has']:
      add(new, n)
      new['lo'] = min(col1['lo'], col2['lo'])
      new['hi'] = max(col1['hi'], col2['hi'])
  return new