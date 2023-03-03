from numUtils import *
from creation import COLS

def row(data, t):
  if data['cols']:
    (data['rows']).append(t)

    # assume data.cols.x, data.cols.y are lists
    for cols in [data['cols']['x'], data['cols']['y']]:
      for col in cols:
        add(col, t[col['at']])
  else:
    data['cols'] = COLS(t)
  
  return data

def add(col, x, n=None):
  if x != '?':
    n = n or 1
    col['n'] = col['n'] + n

    # is a SYM
    if 'isSym' in col and col['isSym']:
      index = 0
      if x in col['has']:
        index = col['has'][x]
      # col['has'][x] = n + (col['has'][x] or 0)
      
      col['has'][x] = n + index
      if col['has'][x] > col['most']:
        col['most'], col['mode'] = col['has'][x], x
    
    # is a NUM
    else:
      col['lo'] = min(x, col['lo'])
      col['hi'] = max(x, col['hi'])
      all = len(col['has'])

      pos = None
      # from config import the
      if all < the['Max']:
        pos = all+1
      elif rand() < the['Max']/col['n']:
        pos = rint(1, all)
      if pos:
        ##################
        # print(col['has'])
        # print(pos)

        # col['has'][pos] = x
        col['has'].append(x)
        col['ok'] = False

def adds(col, t):
  for x in t:
    add(col, x)
  return col

def extend(range, n, s):
  range['lo'] = min(n, range['lo'])
  range['hi'] = max(n, range['hi'])
  add(range['y'], s)
