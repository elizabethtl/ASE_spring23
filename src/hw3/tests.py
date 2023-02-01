from num import Num
from sym import Sym
from data import Data
from utils import *
from config import *

##################
### test functions
def test_the():
  oo(the)

def test_rand():
  num1 = Num()
  num2 = Num()

  for i in range(1, 1000):
    num1.add(rand(0, 1))
  for i in range(1, 1000):
    num2.add(rand(0, 1))
  m1 = rnd(num1.mid(), 10)
  # print(m1)
  m2 = rnd(num2.mid(), 10)
  # print(m2)
  return m1==m2 and 0.5==rnd(m1, 1)

def test_sym():
  sym = Sym()
  for x in ['a', 'a', 'a', 'a', 'b', 'b', 'c']:
    sym.add(x)
  return 'a'==sym.mid() and 1.379==rnd(sym.div())

def test_num():
  num = Num()
  for x in [1, 1, 1, 1, 2, 2, 3]:
    num.add(x)
  return 11/7==num.mid() and 0.787==rnd(num.div())

def test_csv():
  global n
  n = 0
  def csv_fun(t):
    global n
    n += len(t)
  csv(the["file"], csv_fun)

  ######
  # print(f"test csv n:{n}")

  return n == 8*399

def test_data():
  data = Data(the['file'])
  return len(data.rows) == 398 \
    and data.cols.y[0].w == -1 \
    and (data.cols.x[0].at + 1) == 1 \
    and len(data.cols.x) == 5
    # and len(data.cols.x) == 4

def test_stats():
  data = Data(the['file'])
  for k, cols in enumerate([data.cols.y, data.cols.x]):
    print(k, "mid", o(data.stats("mid", cols, 2)))
    print("", "div", o(data.stats("div", cols, 2)))

def test_clone():
  data1 = Data(the['file'])

  # data2 = data1.clone(data1.rows)
  data2 = Data(the['file'])

  return len(data1.rows) == len(data2.rows) \
    and data1.cols.y[0].w == data2.cols.y[0].w \
    and data1.cols.x[0].w == data2.cols.x[0].w \
    and len(data1.cols.x) == len(data2.cols.x)

def test_around():
  data = Data(the['file'])
  print(0, 0, o(data.rows[0].cells))

  for n, t in enumerate(data.around(data.rows[0])):
    if n%50 == 0:
      print(n, rnd(t.dist, 2), o(t.row.cells))