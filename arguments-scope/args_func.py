#*args means that your function can receive multiple parameters.
#*args are treated as a tuple.

import math

def multiply_all(*args):
  
  multiplied = math.prod(args)
  return multiplied

print(multiply_all(1, 2, 3, 4, 5, 6, 7))