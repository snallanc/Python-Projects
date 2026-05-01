# Problem: Compute the nth Fibonacci number
# Pattern: 1D DP (space-optimized iteration)
# Recurrence: fib(n) = fib(n-1) + fib(n-2), base: fib(0)=0, fib(1)=1
# Time: O(n) | Space: O(1)
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