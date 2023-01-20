import math
import random
import sys
import re

the = {}
help = """script.lua : an example script with help text and a test suite
          (c)2022, Tim Menzies <timm@ieee.org>, BSD-2 
          USAGE:   script.lua  [OPTIONS] [-g ACTION]
          OPTIONS:
            -d  --dump  on crash, dump stack = false
            -g  --go    start-up action      = data
            -h  --help  show help            = false
            -s  --seed  random number seed   = 937162211
          ACTIONS:"""

class Sym:
  def __init__(self):
    self.n = 0
    self.has = {}
    self.most = 0
    self.mode = None
  
  def add(self, x):
    if x != "?":
      self.n += 1
      self.has[x] = 1 + (self.has[x] if x in self.has else 0)
      
      if self.has[x] > self.most:
        self.most = self.has[x]
        self.mode = x
  
  def mid(self):
    return self.mode
  
  # return entropy
  def div(self):
    def fun(p):
      return p*math.log(p, 2)
    
    e = 0
    for _, n in self.has.items():
      e = e + fun(n/self.n)
    
    return -e

class Num:
  def __init__(self):
    self.n = 0
    self.mu = 0
    self.m2 = 0
    self.lo = -math.inf
    self.hi = math.inf

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
    return (self.m2<0 or self.n<2) and 0 or math.pow((self.m2/(self.n-1)), 0.5)


Seed = 937162211
def rand(lo, hi):
  lo = lo or 0
  hi = hi or 1
  global Seed 
  Seed = (16807 * Seed) % 2147483647
  return lo + (hi-lo) * Seed / 2147483647

def rint(lo, hi):
  return math.floor(0.5 + rand(lo, hi))

def rnd(n, nPlaces=3):
  nP = nPlaces
  mult = 10**nP
  return math.floor(n*mult + 0.5)/mult

### lists

def map(t, fun):
  # print(f"map(), t: {t}")
  u = {}
  for k, v in t.items():
    # print(f"map(), k: {k}, v:{v}")
    v, k = fun(v)
    # print(f"fun(), v: {v}, k:{k}")
    i = k if k else (1+len(u))
    u[i] = v
  # print(f"map(), u: {u}")
  return u

def kap(t, fun):
  # print(f"kap(), t: {t}")
  u = {}
  for k, v in t.items():
    # print(f"kap(), k: {k}, v:{v}")
    v, k = fun(k, v)
    # print(f"fun(), v: {v}, k:{k}")
    i = k or (1+len(u))
    u[i] = v
  
  return u

def sort(t, fun):
  t.sort(key=fun)
  return t

# don't understand this
def keys(t):
  return sort(kap(t, ))


### strings
def o(t, isKeys=False):
  # print(f"o(t), t: {t}, type: {type(t)}, is: {not isinstance(t, dict)}")

  # d = {}
  # # if type(t) != 'dict':
  # if not isinstance(t, dict):
  #   print(f"not isinstance {t}")
  #   return str(t), isKeys

  # def fun(k, v):
  #   if not str(k).startswith("_"):
  #     return f":{o(k)} {o(v)}"
  
  sort_t_keys = list(t.keys())
  sort_t_keys.sort()
  # print(sort_t_keys)
  # sort_t = {i: t[i] for i in sort_t_keys}
  sort_t = {f"{k} {t[k]}" for k in sort_t_keys}

  return "{:" + " :".join(sort_t) + "}"
  # return "{" + " ".join(not isKeys and (map(t, o) or sort(kap(t, fun)))) + "}"

def oo(t):

  # print(f"oo(), map")

  print(o(t))
  return t


##########
# examples
egs = {}
def eg(key, str, fun):
  egs[key] = fun
  global help
  help = help + "  -g  "+key+"\t"+str+"\n"

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

#######
### cli
def cli(options):
  # print('cli')

  # options is dict
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
  # print('settings')
  # print(t)
  return dict(t)

##########
### coerce
def coerce(s):
  def fun(s1):
        if s1 == "true": return True
        if s1 == "false": return False
        return s1
  try:
    return float(s)
  except:
      return s


#########
### main
def main():
  saved = {}
  fails = 0

  for k, v in cli(settings(help)).items():
    # print(k, v)
    the[k] = v
    saved[k] = v

  if the['help'] == True:
    print(help)

  

  else:

    # run test functions
    for what, fun in egs.items():
      # print(what, fun)

      if the['go'] == 'all' or what == the['go']:
        for k, v in saved.items():
          the[k] = v
          Seed = the['seed']

        if egs[what]() == False:
          fails += 1
          print("❌ fail:", what)
        else:
          print("✅ pass:", what)



if __name__ == '__main__':
  eg("the", "show settings", test_the)
  eg("rand", "generate, reset, regenerate same", test_rand)
  eg("sym", "check syms", test_sym)
  eg("num", "check nums", test_num)
  main()

  