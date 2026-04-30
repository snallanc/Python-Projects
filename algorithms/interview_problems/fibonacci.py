def fibonacci(n):
    if n <= 1:
        return n
    p1, p2 = 0, 1
    for _ in range(2, n+1):
        p1, p2 = p2, p1 + p2
    return p2

# Test code
if __name__ == "__main__":
    for n in range(5):
        print("Fibonacci of {}: {}".format(n, fibonacci(n)))