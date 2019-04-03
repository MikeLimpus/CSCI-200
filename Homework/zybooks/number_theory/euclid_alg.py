""" Implementation of Euclidian Algorithm to find 
greatest common denominator of two integers """


def gcd(foo, bar):
    x = foo
    y = bar
    while(y != 0):
        r = x % y
        x = y
        y = r
    return x