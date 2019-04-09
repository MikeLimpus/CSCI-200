# a general algorithm for solving linear congruences in the form ax ≡ b(mod m)

def linear_congruence(a, b, m):
    for x in range(0, (m - 1)):
        if ((a * x) % m == b):
            return x 
