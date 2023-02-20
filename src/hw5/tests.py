from creation import *
from utils import *
from numUtils import *
# from config import *
from query import *
from optimization import sway

from update import *
from cluster import *
from discretization import *

##################
### test functions
def test_the():
  oo(the)

def test_rand():
  t = []
  u = []

  # global Seed
  # Seed = 1
  for i in range(1, 1000):
    t.append(rint(0, 100, 1))
  for i in range(1, 1000):
    u.append(rint(0, 100, 1))
  
  for n, num in enumerate(t):
    # print(num, u[n])
    assert(num == u[n])

def test_some():
  the['max'] = 32
  num1 = NUM()
  for i in range(1, 10000):
    add(num1, i)
  # oo(has(num1))

def test_num():
  num1 = NUM()
  num2 = NUM()

  for i in range(1, 10000):
    add(num1, rand())

  for i in range(1, 10000):
    add(num2, rand()**2)

  print(1, rnd(mid(num1)), rnd(div(num1)))
  print(2, rnd(mid(num2)), rnd(div(num2)))
  return 0.5 == rnd(mid(num1)) and mid(num1) > mid(num2)

def test_sym():
  sym = adds(SYM(), ['a', 'a', 'a', 'a', 'b', 'b', 'c'])
  print(mid(sym), rnd(div(sym)))
  return 1.38==rnd(div(sym))

def test_csv():
  global n
  n = 0
  def csv_fun(t):
    global n
    n += len(t)
  csv(the["file"], csv_fun)

  return n == 8*399

def test_data():
  data = DATA.read(the['file'])
  col = data['cols']['x'][0]
  print(col['lo'], col['hi'], mid(col), div(col))
  oo(stats(data))

def test_clone():
  data1 = DATA.read(the['file'])
  data2 = DATA.clone(data1, data1['rows'])

  oo(stats(data1))
  oo(stats(data2))

def test_cliffs():
  assert(False == cliffsDelta([8,7,6,2,5,8,7,3], [8,7,6,2,5,8,7,3]), "1")
  assert(True == cliffsDelta([8,7,6,2,5,8,7,3], [9,9,7,8,10,9,6]), "2")
  t1 = []
  t2 = []
  for i in range(0, 1000):
    t1.append(rand())
  for i in range(0, 1000):
    t2.append(rand()**0.5)
  
  assert(False == cliffsDelta(t1, t1), "3")
  assert(True == cliffsDelta(t1, t2), "4")
  diff = False
  j = 1.0
  while not diff:
    def func(x):
      return x*j
    t3 = list(map(func, t1))
    diff = cliffsDelta(t1, t3)
    print(">", rnd(j), diff)
    j = j*1.025

def test_dist():
  data = DATA.read(the['file'])
  num = NUM()
  for row in data['rows']:
    add(num, dist(data, row, data['rows'][1]))
  oo({'lo': num['lo'], 'hi': num['hi'], 'mid': rnd(mid(num)), 'div': rnd(div(num))})

def test_half():
  data = DATA.read(the['file'])
  left, right, A, B, c = half(data)
  print(len(left), len(right))
  l = DATA.clone(data, left)
  r = DATA.clone(data, right)
  print('l', o(stats(l)))
  print('r', o(stats(r)))
  
def test_tree():
  showTree(tree(DATA.read(the['file'])))

def test_sway():
  data = DATA.read(the['file'])
  best, rest = sway(data)
  print("\nall ", o(stats(data))) 
  print("    ",   o(stats(data,div))) 
  print("\nbest", o(stats(best))) 
  print("    ",   o(stats(best,div))) 
  print("\nrest", o(stats(rest))) 
  print("    ",   o(stats(rest,div))) 
  print("\nall ~= best?", o(diffs(best['cols']['y'], data['cols']['y'])))
  print("best ~= rest?", o(diffs(best['cols']['y'], rest['cols']['y'])))

def test_bins():
  data = DATA.read(the['file'])
  best, rest = sway(data)
  print('all', '', '', '', o({'best': len(best['rows']), 'rest': len(rest['rows'])}))
  for k, t in (bins(data['cols']['x'], {'best': best['rows'], 'rest': rest['rows']})):
    for range in t:
      if range['txt'] != b4:
        print('')
      b4 = range['txt']
      print(range['txt'], range['lo'], range['hi'], 
            rnd(value(range['y']['has'], len(best['rows']), len(rest['rows']), "best")), 
            o(range['y']['has']))