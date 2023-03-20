from discretization import bins
from query import value
from operator import itemgetter
from creation import RULE
from listUtils import kap2
from numUtils import rnd
from utils import oo, o

def xpln(data, best, rest):
  def v(has):
    return value(has, len(best['rows']), len(rest['rows']), "best")
  def score(ranges):

    ### rule
    # print(rule)

    rule = RULE(ranges, maxSizes)
    if rule:
      # oo(showRule(rule))
      print(showRule(rule))
      bestr = selects(rule, best['rows'])
      restr = selects(rule, rest['rows'])

      ### 
      # print(bestr)
      # print(restr)

      if len(bestr)+len(restr) > 0:
        return v({'best': len(bestr), 'rest': len(restr)}), rule
  tmp, maxSizes = [], {}
  for ranges in (bins(data['cols']['x'], {'best': best['rows'], 'rest': rest['rows']})):
    maxSizes[ranges[0]['txt']] = len(ranges)
    print()

    for range in ranges:
      print(range['txt'], range['lo'], range['hi'])
      tmp.append({'range': range, 'max': len(ranges), 'val': v(range['y']['has'])})
  
  # reverser=True ??
  rule, most = firstN(sorted(tmp, key=itemgetter('val')), score)
  return rule, most

def firstN(sortedRanges, scoreFun):
  print()

  def func(r):
    print(r['range']['txt'], r['range']['lo'], r['range']['hi'], rnd(r['val']), o(r['range']['y']['has']))
  map(func, sortedRanges)
  first = sortedRanges[0]['val']
  def useful(range):
    if(range['val'] > 0.05 and range['val'] > first/10):
      return range
  # sortedRanges = map(useful, sortedRanges)
  sortedRanges = [x for x in sortedRanges if useful(x)]
  most, out = -1, -1
  # not sure if python slice is the same as the slice() in the lua code
  for n in range(1, len(sortedRanges)+1):
    split = sortedRanges[0:n]
    split_range = [x['range'] for x in split]
    tmp, rule = scoreFun(split_range)
    if tmp and tmp > most:
      out, most = rule, tmp
  return out, most

def showRule(rule):
  def pretty(range):
    return range['lo'] if range['lo']==range['hi'] else [range['lo'], range['hi']]
  def merge(t0):
    t, j = [], 1
    while j <= len(t0):
      # left, right = t0[j], t0[j+1]
      # print(j, len(t0))
      left = t0[j-1]
      if j < len(t0):
        right = t0[j]
      else:
        right = None
      if right and left['hi'] == right['lo']:
        left['hi'] = right['hi']
        j += 1
      t.append({'lo':left['lo'], 'hi':left['hi']})
      j += 1
    return t if len(t0) == len(t) else merge(t)
  def merges(attr, ranges):
    # print(merge(sorted(ranges, key=itemgetter('lo'))))
    # for range in ranges:

    return list(map(pretty, merge(sorted(ranges, key=itemgetter('lo'))))), attr

  return kap2(rule, merges)    

def selects(rule, rows):
  def disjunction(ranges, row):
    for range in ranges:
      lo, hi, at = range['lo'], range['hi'], range['at']
      x = row[at]
      if x == '?':
        return True
      if lo == hi and lo == x:
        return True
      if lo <= x and x < hi:
        return True
    return False
  def conjunction(row):
    for ranges in rule.values():
      if not disjunction(ranges, row):
        return False
    return True
  
  def func(r):
    if None in r or r is None:
      # print(f"func(r):")
      # print(r)  
      return
    if conjunction(r):
      return r
  
  return list(map(func, rows))