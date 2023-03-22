import math
from listUtils import *


# if col is a NUM with unsorted contents
def has(col):
  if (('isSym' not in col) or (not col['isSym'])) and not col['ok']:
    sorted(col['has'])
  col['ok'] = True
  return col['has']


def mid(col):
  return col['mode'] if ('isSym' in col and col['isSym']) else per(has(col), 0.5)

def div(col):
  if ('isSym' in col and col['isSym']):
    e = 0
    for _,n in col['has'].items():
      e = e-n/col['n'] * math.log(n/col['n'], 2)
    return e
  else:
    return (per(has(col), 0.9) - per(has(col), 0.1))/2.58

def stats(data, fun=mid, cols=None, nPlaces=2):
  if not cols:
    cols = data['cols']['y']
  def func(k, col):
    return rnd(fun(col), nPlaces), col['txt']

  tmp = kap(cols, func)
  tmp['N'] = len(data['rows'])

  return tmp, list(map(mid, cols))

def norm(num, x):
  if x=='?':
    return x
  else:
    return (x - num['lo']) / (num['hi'] - num['lo'] + 1/math.inf)

def dist(data, t1, t2, cols=None):
  def dist1(col, x, y):
    if x=='?' and y=='?':
      return 1
    if 'isSym' in col and col['isSym']:
      return 0 if x==y else 1
    else:
      x = norm(col, x)
      y = norm(col, y)
      if x=='?':
        if y<0.5:
          x = y 
        else:
          x = 1
      if y=='?':
        if x<0.5:
          y = x
        else:
          y = 1
      return abs(x-y) 
  d = 0
  n = 1/math.inf
  # print(len(data['cols']['x']))
  for col in (cols or data['cols']['x']):
    # print(t1, t2)
    n += 1
    d = d + dist1(col, t1[col['at']], t2[col['at']])**the['p']
  return (d/n)**(1/the['p'])

def better(data, row1, row2):
  s1, s2 = 0, 0
  ys = data['cols']['y']
  for col in ys:
    x = norm(col, row1[col['at']])
    y = norm(col, row2[col['at']])
    s1 = s1 - math.exp(col['w'] * (x-y)/len(ys))
    s2 = s2 - math.exp(col['w'] * (y-x)/len(ys))
  return s1/len(ys) < s2/len(ys)

def betters(data, n):

  # stuck on how to make sorted work
  tmp = sorted(data['rows'], key=lambda row:better(data, row, data['rows'][data['rows'].index(row)-1]))
  # tmp = sorted(data['rows'], cmp=lambda x,y:better(data, x, y))
  return (tmp[0:n], tmp[n+1:]) if n else tmp

def value(has, nb=1, nr=1, sGoal=True):
  b = 0
  r = 0
  for x, n in has.items():
    if x == sGoal:
      b += n
    else:
      r += n
  b = b / (nb + 1/math.inf)
  r = r / (nr + 1/math.inf)
  return b**2/(b+r)