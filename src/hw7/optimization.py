from config import *
from cluster import half
from creation import DATA
from query import better
import random

def sway(data):
  def worker(rows, worse, evals0=None, above=None):
    if len(rows) <= len(data['rows'])**the['min']:
      # get random item from 
      tmp = []
      for i in range(0, int(the['rest']*len(rows))):
        tmp.append(random.choice(worse))
      return rows, tmp, evals0
    else:
      l, r, A, B, c, evals = half(data, rows, None, above)
      if better(data, B, A):
        l, r, A, B = r, l, B, A
      # def func(row):
      #   worse.append(row)
      # map(func, r)
      for row in r:
        worse.append(row)
      return worker(l, worse, evals+evals0, A)
  best, rest, evals = worker(data['rows'], [], 0)
  return DATA.clone(data, best), DATA.clone(data, rest), evals