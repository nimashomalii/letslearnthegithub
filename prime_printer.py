import numpy as np 
import prime_number_checker as pnc
from prime_number_checker import prime_checker 
import sys
prime_check = prime_checker()
a = int(sys.argv[1])
b = int(sys.argv[2])
if a >  b : 
  c = a 
  a = b 
  b = c
l = [] 
for i in range(a , b , 1 ) : 
  if prime_check(i) : 
    l.append(i)
print(l)


