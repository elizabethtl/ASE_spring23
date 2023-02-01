from utils import *
from row import Row
from cols import Cols

class Data:
  def __init__(self, src={}):

    #######
    # print(f"data src: {src}")

    self.rows = []
    self.cols = None

    # fun = lambda x: self.add(x)

    if isinstance(src, str):
      csv(src, lambda x: self.add(x))
    else:
      map(src, lambda x: self.add(x))

    ######
    # print(f"data.cols {self.cols}")
  
  def add(self, t):
    ######
    # print(f"data.add t:{t}")
    if self.cols:
      # make t a Row
      t = t if "Row" in str(type(t)) else Row(t)
      self.rows.append(t)
      self.cols.add(t)
    else:
      self.cols = Cols(t)

  def clone(self, init={}):
    ######
    print(f"clone self.cols.names: {self.cols.names}")
    print(f"clone init len: {len(init)}")
    
    data = Data(self.cols.names)
    map(init, lambda x: data.add(x))
    return data

  def stats(self, what, cols, nPlaces):
    def fun(k, col):
      return col.rnd(getattr(col, what)(), nPlaces), col.txt
    return kap(cols or self.cols.y, fun)

  def dist(self, row1, row2, cols=None):
    n = 0
    d = 0 

    for _, col in enumerate(cols if cols else self.cols.x):
      n += 1
      # ^ operator is XOR in python
      d += col.dist(row1.cells[col.at], row2.cells[col.at])^the['p']
    return (d/n)^(1/the['p'])
  
  def around(self, row1, rows=None):
    def func(row2):
      return {'row':row2, 'dist':self.dist(row1, row2, self.cols)}
    return sort(map(rows if rows else self.rows), )