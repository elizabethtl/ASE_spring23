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
  # print(f"len of data.rows:{len(data.rows)}")
  # print(f"len of data.cols.y:{len(data.cols.y)}")
  # print(f"data.cols.y[0].w:{data.cols.y[0].w}")
  # print(f"data.cols.y[1].w:{data.cols.y[1].w}")
  # print(f"data.cols.x[0].at:{data.cols.x[0].at}")
  # print(f"len of data.cols.x:{len(data.cols.x)}")
  return len(data.rows) == 398 \
    and data.cols.y[0].w == -1 \
    and data.cols.x[0].at == 1 \
    and len(data.cols.x) == 4

def test_stats():
  data = Data(the['file'])
  for k, cols in enumerate([data.cols.y, data.cols.x]):
    print(k, "mid", o(data.stats("mid", cols, 2)))
    print("", "div", o(data.stats("div", cols, 2)))