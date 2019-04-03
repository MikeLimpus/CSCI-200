"""An algorithm to determine the primality of 
a number using the trial division method"""


import math


def trial_division(n):
    for i in range(2, math.sqrt(n)):
        if (n % i == 0):
            return i
        return -1


foo = trial_division(3)
if(foo == -1):
    print("Prime")
else:
    print("not prime")
print("\n")