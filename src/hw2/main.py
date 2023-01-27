
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
  eg("rand", "generate, reset, regenerate same", test_rand)
  eg("sym", "check syms", test_sym)
  eg("num", "check nums", test_num)
  eg("csv", "read from csv", test_csv)
  eg("data", "read DATA csv", test_data)
  eg("stats", "stats from DATA", test_stats)
  main()