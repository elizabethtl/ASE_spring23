import math
from config import *
from listUtils import *

def rand(lo, hi):
  lo = lo or 0
  hi = hi or 1
  global Seed 
  Seed = (16807 * Seed) % 2147483647
  return lo + (hi-lo) * Seed / 2147483647


def my_rint(lo, hi):
  print('rint')
  return math.floor(0.5 + rand(lo, hi))

def rnd(n, nPlaces=3):
  # print(f"rnd n:{n}")
  nP = nPlaces
  mult = 10**nP
  return math.floor(n*mult + 0.5)/mult

def cosine(a, b, c):
  # print(f"a: {a}, b: {b}, c: {c}")

  #######
  ## sometime c=0
  # if(c == 0):
  #   return 0, 0

  x1 = (a**2 + c**2 - b**2) / (2*c)
  x2 = max(0, min(1, x1))
  y = abs((a**2 - x2**2)) ** 0.5

  if isinstance(y, complex):
    print(f"a = {a}, b = {b}, c = {c}")
    print(f"x1 = {x1}, x2 = {x2}, y = {y}")
  return x2, y

def copy(t, u=None):
  # list or dict ??
  if isinstance(t, list):
    return t
  def func(k, v):
    return copy(v), copy(k)

  u = kap(t, func)
  # setmetatable(u, getmetatable(t))
  return {u, t}
  