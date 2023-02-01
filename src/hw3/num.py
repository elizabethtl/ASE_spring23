import math
import re

from utils import *

class Num:
  def __init__(self, at=0, txt=''):
    # print(f"txt:{txt}")
    
    self.at = at
    self.txt = txt
    self.n = 0
    self.mu = 0
    self.m2 = 0
    self.lo = -math.inf
    self.hi = math.inf
    # print(re.search("-$", self.txt))
    self.w = -1 if re.search("-$", self.txt) else 1

  def add(self, x):
    if x != "?":
      self.n = self.n + 1
      d = x - self.mu
      self.mu = self.mu + d/self.n
      self.m2 = self.m2 + d*(x - self.mu)
      self.lo = min(x, self.lo)
      self.hi = max(x, self.hi)
  
  def mid(self):
    return self.mu

  # return standard deviation
  def div(self):
    return 0 if (self.m2<0 or self.n<2) else math.pow((self.m2/(self.n-1)), 0.5)

  def rnd(self, x, n):
    return x if x=="?" else rnd(x, n)