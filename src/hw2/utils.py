import math
import re
import sys
import os
dir_path = os.path.abspath(os.path.dirname(__file__))

from config import *

def rand(lo, hi):
  lo = lo or 0
  hi = hi or 1
  global Seed 
  Seed = (16807 * Seed) % 2147483647
  return lo + (hi-lo) * Seed / 2147483647

def rint(lo, hi):
  return math.floor(0.5 + rand(lo, hi))

def rnd(n, nPlaces=3):
  # print(f"rnd n:{n}")
  nP = nPlaces
  mult = 10**nP
  return math.floor(n*mult + 0.5)/mult

def map(t, fun):
  # print(f"map(), t: {t}")
  u = {}
  for k, v in t.items():
    # print(f"map(), k: {k}, v:{v}")
    v, k = fun(v)
    # print(f"fun(), v: {v}, k:{k}")
    # i = k if k else (1+len(u))
    i = k if k else (len(u))
    u[i] = v
  # print(f"map(), u: {u}")
  return u

def kap(t, fun):
  # print(f"kap(), t: {t}")
  u = {}
  for k, v in enumerate(t):
    # print(f"kap(), k: {k}, v:{v}")
    v, k = fun(k, v)
    # print(f"fun(), v: {v}, k:{k}")
    # i = k or (1+len(u))
    i = k if k else (len(u))
    u[i] = v
  
  return u

def sort(t, fun):
  t.sort(key=fun)
  return t

### strings
def o(t, isKeys=False):
  sort_t_keys = list(t.keys())
  sort_t_keys.sort()
  sort_t = {f"{k} {t[k]}" for k in sort_t_keys}

  return "{:" + " :".join(sort_t) + "}"

def oo(t):
  print(o(t))
  return t

def eg(key, str, fun):
  egs[key] = fun
  global help
  help = help + "  -g  "+key+"\t"+str+"\n"

#######
### csv
def csv(filename, csv_fun):

  ######
  # print(f"csv filename {filename}")
  # print(f"fun_csv {fun_csv}")

  s = open(dir_path+'/'+filename, 'r')
  lines = s.readlines()
  for line in lines:
    t = []
    for s1 in line.split(','):
      s1 = s1.replace('\n', '')
      t.append(coerce(s1))
    
    #######
    # print(f"csv t")
    # print(t)
    # t = ['Clndrs', 'Volume', 'Hp:', 'Lbs-', 'Acc+', 'Model', 'origin', 'Mpg+']
    # t = [8.0, 304.0, 193.0, 4732.0, 18.5, 70.0, 1.0, 10.0]
    # ....

    csv_fun(t)
  
#######
### cli
def cli(options):
  for k, v in options.items():
    v = str(v)

    argv = sys.argv[1:]
    for n, x in enumerate(argv):
      if x=='-'+k[0] or x=='--'+k:
        if v == 'false':
          v = 'true'
        if v == 'true':
          v = 'false'
        else:
          v = argv[n+1]
      options[k] = coerce(v)

  # print(options)
  return options

############
### settings
def settings(s):
  t = re.findall("\n[\s]+[-][\S]+[\s]+[-][-]([\S]+)[^\n]+= ([\S]+)", s)
  return dict(t)

##########
### coerce
def coerce(s):
  if s == "true": return True
  elif s == "false": return False
  else:
    try:
      return float(s)
    except:
        return s