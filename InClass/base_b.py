from math import floor

def BaseBExpansion(n, b):
    L = []
    q = n
    while(q != 0):
        L.insert(0, q % b)
        # L[-1] = q % b  # Index -1 is the last element of a list  
        q = floor(q / b) 
    return L 

