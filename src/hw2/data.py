from utils import *
from row import Row
from cols import Cols

class Data:
  def __init__(self, src):

    #######
    # print(f"data src: {src}")

    self.rows = []
    self.cols = None

    # fun = lambda x: self.add(x)

    if isinstance(src, str):
      csv(src, lambda x: self.add(x))
    else:
      map(src if src else {}, lambda x: self.add(x))

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

  def clone(self, init):
    data = Data({self.cols.names})
    map(init or {}, lambda x: data.add(x))
    return data

  def stats(self, what, cols, nPlaces):
    def fun(k, col):
      return col.rnd(getattr(col, what)(), nPlaces), col.txt
    return kap(cols or self.cols.y, fun)