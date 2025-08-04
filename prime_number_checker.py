import numpy as np 
class prime_checker : 
  def __init__(self):
    pass 
  def is_prime(self , x ) : 
    if x < 2 : 
      return False
    elif x ==2 : 
      return True 
    else : 
      for i in range(int(x**0.5) +1 ) :
        if x%i ==0 :
          return False
      return True 
        
