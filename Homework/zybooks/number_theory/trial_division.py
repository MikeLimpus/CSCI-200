def trial_division(n): 
    for i in range (2, sqrt(n)):
        if (n % i == 0): 
            return i
        return -1

def main(): 
    foo = trial_division(3) 
    if(foo == -1):
        print("Prime") 
    else:
        print("not prime")
    

