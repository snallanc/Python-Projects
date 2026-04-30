def climbing_stair_combinations(n):
    if n <= 1:
        return 1
    a, b = 1, 1
    for _ in range(2, n+1):
        a, b = b, a+b
    return b

# Test code
if __name__ == "__main__":
    for n in range(10):
        print("Number of ways to climb {} steps: {}".format(n, climbing_stair_combinations(n))) 
