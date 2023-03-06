from config import *
from query import dist, stats
from utils import o
import random
from operator import itemgetter
from creation import DATA

def half(data, rows=None, cols=None, above=None):
  left = []
  right = []
  A, B, c = None, None, None
  def gap(r1, r2):
    # print(F"gap, {r1}, {r2}")
    return dist(data, r1, r2, cols)
  def cos(a, b, c):
    return (a**2 + c**2 - b**2) / (2*c)
  def proj(r):
    return {'row': r, 'x': cos(gap(r, A), gap(r, B), c)}
  
  rows = rows or data['rows']
  some = []
  for i in range(0, int(the['Halves'])):
    # get random element from rows and add to some
    some.append(random.choice(rows))

  A = above if (above and the['Reuse']) else random.choice(some)
  # print(the['Reuse'], random.choice(some))
  # print("A", A)
  def func(r):
    return {'row': r, 'd': gap(r, A)}
  tmp = sorted(map(func, some), key=itemgetter('d'))
  far = tmp[int(len(tmp)*the['Far']//1) - 1]
  B = far['row']
  c = far['d']
  for n, two in enumerate(sorted(map(proj, rows), key=itemgetter('x'))):
    if n <= len(rows)/2:
      left.append(two['row'])
    else:
      right.append(two['row'])
  evals = 1 if (above and the['Reuse']) else 2
  return left, right, A, B, c, evals

def tree(data, rows=None, cols=None, above=None):
  rows = rows or data['rows']
  here = {'data': DATA.clone(data, rows)}
  if len(rows) >= 2*len(data['rows'])**the['min']:
    left, right, A, B, _ = half(data, rows, cols, above)
    here['left'] = tree(data, left, cols, A)
    here['right'] = tree(data, right, cols, B)
  return here

def showTree(tree, lvl=0):
  if tree:
    print('|..'*lvl, len(tree['data']['rows']), end='')
    if (lvl == 0 or (not 'left' in tree.keys())):
      print(o(stats(tree['data'])))
    else:
      print("")
    if not 'left' in tree:
      return
    else:
      showTree(tree['left'], lvl+1)
    if not 'right' in tree:
      return
    else:
      showTree(tree['right'], lvl+1)