# import pytest
from hw1 import *

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

