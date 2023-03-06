
from config import *
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
  eg("the", "show options", test_the)
  eg("rand", "demo random number generation", test_rand)
  eg("some", "demo or reservoir sampling", test_some)
  eg("num", "demo of NUM", test_num)
  eg("sym", "demo SYMS", test_sym)
  eg("csv", "reading csv files", test_csv)
  eg("data", "showing data sets", test_data)
  eg("clone", "replicate structure of a DATA", test_clone)

  eg("cliffs", "stats tests", test_cliffs)
  eg("dist", "distance test", test_dist)
  eg("half", "divide data in half", test_half)
  eg("tree", "make and show tree of clusters", test_tree)
  eg("sway", "optimizing", test_sway)
  eg("bins", "find deltas between best and rest", test_bins)

  main()