"""
Compute power(x, y) where x is double and y is an integer(positive or negative).
Obviously, don't use python's power operator x**y :)
"""

"""
Brute force:
Keep multiplying x (y-1) times. Has exponential complexity.
"""

"""
Use recursion with memoization to compute power(x, y) for one branch and cache the results to save computing for
the other branch.
"""
cache = {}
def power_recursive(x, y):
    result = 0
    if y == 0:
        return 1
    if y == 1:
        return x
    if (x, y) in cache:
        # print("\treturning pow({0},{1}) from cache".format(x, y))
        return cache[(x, y)]
    # print("\tpow({0},{1}) not in cache, computing".format(x, y))
    if ((y % 2) == 0):
        result = power_recursive(x, int(y/2)) * power_recursive(x, int(y/2))
    else:
        result = power_recursive(x, int(y/2)) * power_recursive(x, int(y/2)) * x
    cache[(x, y)] = result
    return result

"""
Use iterative approach and save #multiplications by squaring x and right shifting y in each iteration. 
"""
def power_iterative(x, y):
    result = 1
    while y:
        if y & 1:
            result *= x
        x, y = x*x, y>>1
    return result

def compute_power(x, y):
    x2, y2 = x, y
    if y < 0:
        x2, y2 = 1/x, -y
    result1 = power_recursive(x2, y2)
    result2 = power_iterative(x2, y2)
    print("Power({0},{1}) using recursion is {2}".format(x, y, result1))
    print("Power({0},{1}) using iteration is {2}\n###############################".format(x, y, result2))


"""
Test code
"""
compute_power(2, 30)
compute_power(3.2, 20)
compute_power(5, -10)
compute_power(10.5, -4)
print("Cache entries used by recursion are {0}".format(cache))