#Procedural version of Division Algorithm


def ProceduralDivisionAlgorithm(n, d):
    if (n >= 0):    # Case 1
        q = 0
        r = n 
        while(r >= d):
            q += 1
            r -= d 
    else:           # Case 2
        q = 0
        r = n 
        while(r < 0):
            q -= 1
            r += d 
    return q, r