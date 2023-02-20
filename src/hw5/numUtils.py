import math
import random
from config import *

def rand(lo=None, hi=None, input_seed=None):
  lo = lo or 0
  hi = hi or 1
  global Seed 
  if(input_seed):
    Seed = 1
  else:
    Seed = (16807 * Seed) % 2147483647
  # print('seed', Seed)
  return lo + (hi-lo) * Seed / 2147483647

def rint(lo, hi, input_seed=None):
  return math.floor(0.5 + rand(lo, hi, input_seed))

def rnd(n, nPlaces=2):
  # print(f"rnd n:{n}")
  nP = nPlaces
  mult = 10**nP
  return math.floor(n*mult + 0.5)/mult

# def cosine(a, b, c):
#   # print(f"a: {a}, b: {b}, c: {c}")

#   #######
#   ## sometime c=0
#   if(c == 0):
#     return 0, 0

#   x1 = (a**2 + c**2 - b**2) / (2*c)
#   x2 = max(0, min(1, x1))
#   y = (a**2 - x2**2) **0.5
#   return x2, y

def cliffsDelta(ns1, ns2):
  # ns1, ns2 are lists
  if len(ns1) > 256:
    ns1 = random.sample(ns1, 256)
  if len(ns2) > 256:
    ns2 = random.sample(ns2, 256)
  if len(ns1) > 10*len(ns2):
    ns1 = random.sample(ns1, 10*len(ns2))
  if len(ns2) > 10*len(ns1):
    ns2 = random.sample(ns2, 10*len(ns1))
  n, gt, lt = 0, 0, 0
  for x in ns1:
    for y in ns2:
      n += 1
      if x > y:
        gt += 1
      if x < y:
        lt += 1
  return abs(lt - gt)/n > the['cliffs']

def diffs(nums1, nums2):
  def func(k, nums):
    return cliffsDelta(nums['has'], nums2[k]['has']), nums['txt']
  from listUtils import kap
  return kap(nums1, func)