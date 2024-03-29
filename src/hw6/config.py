the = {}
help = """xpln: multi-goal semi-supervised explanation
          (c) 2023 Tim Menzies <timm@ieee.org> BSD-2
            
          USAGE: lua xpln.lua [OPTIONS] [-g ACTIONS]
            
          OPTIONS:
            -b  --bins    initial number of bins       = 16
            -c  --cliffs  cliff's delta threshold      = .147
            -d  --d       different is over sd*d       = .35
            -f  --file    data file                    = ../../etc/data/auto93.csv
            -F  --Far     distance to distant          = .95
            -g  --go      start-up action              = nothing
            -h  --help    show help                    = false
            -H  --Halves  search space for clustering  = 512
            -m  --min     size of smallest cluster     = .5
            -M  --Max     numbers                      = 512
            -p  --p       dist coefficient             = 2
            -r  --rest    how many of rest to sample   = 4
            -R  --Reuse   child splits reuse a parent pole = true
            -s  --seed    random number seed           = 937162211"""

egs = {}

Seed = 937162211

b4 = []