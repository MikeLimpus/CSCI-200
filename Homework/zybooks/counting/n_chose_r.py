import math 

def choose(n, r):
    if (n <= r):
        numer = math.factorial(n)
        denom = (math.factorial(r)) * (math.factorial(n - r)) 
        return numer / denom
    else:
        print("Error: n must be less than or equal to r")
    