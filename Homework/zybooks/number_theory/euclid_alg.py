""" Implementation of Euclidian Algorithm to find 
greatest common denominator of two integers """


def gcd(a, b):
    x = a
    y = b
    while(y != 0):
        r = x % y
        x = y
        y = r
    return x