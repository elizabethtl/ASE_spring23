
import re
import sys
import os
dir_path = os.path.abspath(os.path.dirname(__file__))

from config import *
  

### strings
def o(t, isKeys=False):

  if not isinstance(t, dict):
    return str(t)

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
  t = []
  for line in lines:
    # t = []
    row = []
    for s1 in line.split(','):
      s1 = s1.replace('\n', '')
      row.append(coerce(s1))
    t.append(row)
    
    #######
    # print(f"csv t")
    # print(t)
    # t = ['Clndrs', 'Volume', 'Hp:', 'Lbs-', 'Acc+', 'Model', 'origin', 'Mpg+']
    # t = [8.0, 304.0, 193.0, 4732.0, 18.5, 70.0, 1.0, 10.0]
    # ....

    csv_fun(row)
  
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

def show(node, what, cols, nPlaces, lvl=0):
  if node:

    print('| '*lvl + str(len(node['data'].rows)) + '', end='')
    
    if ((not 'left' in node) or lvl==0):
      print(o(node['data'].stats("mid", node['data'].cols.y, nPlaces)))
    else:
      print('')
    # print(o(node['data'].stats("mid", node['data'].cols.y, nPlaces)) if ((not 'left' in node) or lvl==0) else "")
    # show(node['left'], what, cols, nPlaces, lvl+1)
    show(node.get('left'), what, cols, nPlaces, lvl+1)
    # show(node['right'], what, cols, nPlaces, lvl+1)
    show(node.get('right'), what, cols, nPlaces, lvl+1)