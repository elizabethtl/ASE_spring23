
from config import *
from utils import *
from tests import *

#########
### main
def main():
  saved = {}
  fails = 0

  for k, v in cli(settings(help)).items():
    ######
    # print(k, v)
    
    the[k] = v
    saved[k] = v

  if the['help'] == True:
    print(help)

  else:
    # run test functions
    for what, fun in egs.items():
      
      ######
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
  eg("sym", "check syms", test_sym)
  eg("num", "check nums", test_num)
  eg("data", "read DATA csv", test_data)
  eg("clone", "duplicate structure", test_clone)
  eg("around", "sorting nearest neighbors", test_around)
  # eg("half", "1-level bi-clustering", test_half)
  # eg("cluster", "N-level bi-clustering", test_cluster)
  # eg("optimize", "semi-supervised optimization", test_optimize)
  main()