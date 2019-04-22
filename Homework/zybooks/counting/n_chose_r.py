import math 

def choose(n, r):
    numer = math.factorial(n)
    denom = (math.factorial(r)) * (math.factorial(n - r)) 
    return numer / denom
 