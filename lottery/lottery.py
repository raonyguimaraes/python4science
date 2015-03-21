from itertools import combinations

possibilities = combinations(range(1,60), 6)

import random

def random_line(afile):
    line = next(afile)
    for num, aline in enumerate(afile):
      if random.randrange(num + 2): continue
      line = aline
    return line


print random_line(possibilities)