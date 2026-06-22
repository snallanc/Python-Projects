# Problem: Count distinct ways to climb n stairs, taking 1 or 2 steps at a time
# Pattern: 1D DP — same recurrence as Fibonacci
# Recurrence: ways(n) = ways(n-1) + ways(n-2), base: ways(0)=1, ways(1)=1
# Key insight: dp[0]=1 means 'one way to stand at ground' (empty path) — makes recurrence uniform
# Time: O(n) | Space: O(1)
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
