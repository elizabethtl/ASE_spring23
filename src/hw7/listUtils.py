from numUtils import *


def myMap(t, fun):
  # print(f"map(), len of t: {len(t)}")
  u = {}
  for k, v in enumerate(t):
    # print(f"map(), k: {k}, v:{v}")
    # v, k = fun(v)
    v = fun(v)
    # print(f"fun(), v: {v}, k:{k}")
    # i = k if k else (1+len(u))
    # i = k if k else (len(u))
    i = k
    u[i] = v
  # print(f"map(), u: {u}")
  return u

def kap(t, fun):
  # print(f"kap(), t: {t}")
  u = {}
  # for k, v in t.items():
  for k, v in enumerate(t):
    # print(f"kap(), k: {k}, v:{v}")
    v, k = fun(k, v)
    # print(f"fun(), v: {v}, k:{k}")
    # i = k or (1+len(u))
    i = k if k else (len(u))
    u[i] = v
  return u

def kap2(t, fun):
  # print(f"kap(), t: {t}")
  u = {}
  for k, v in t.items():
  # for k, v in enumerate(t):
    # print(f"kap(), k: {k}, v:{v}")
    v, k = fun(k, v)
    # print(f"fun(), v: {v}, k:{k}")
    # i = k or (1+len(u))
    i = k if k else (len(u))
    u[i] = v
  
  return u

def sort(t, fun):
  print("t in sort()")
  # print(t)
  print("key in sort()")
  print(fun, type(fun))
  # t.sort(key=fun)
  # return t
  return sorted(t, key=fun)

def any(t):
  return t[rint(0, len(t)-1)]

def many(t, n):
  # print(f"n: {n}")
  u = []
  for i in range(int(n)):
    u.append(any(t))
  return u

def per(t, p):
  p = math.floor(((p or 0.5)*len(t)) + 0.5)
  return t[max(1, min(len(t), p))]