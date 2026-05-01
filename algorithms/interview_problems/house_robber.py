# Problem: Find max sum of non-adjacent elements in an array (Leetcode 198)
# Pattern: 1D Dynamic Programming
# Recurrence: dp[i] = max(dp[i-1], dp[i-2] + nums[i])
#   - Skip house i → best is dp[i-1]
#   - Rob house i  → can't rob i-1, so dp[i-2] + nums[i]
# Time: O(n) | Space: O(1)
def house_robber(money=[]):
    if not money:
        return 0
    if len(money) == 1:
        return money[0]
    p1, p2 = money[0], max(money[0], money[1])
    for i in range(2, len(money)):
        p1, p2 = p2, max(p2, p1 + money[i])
    return p2

# Test code
if __name__ == "__main__":
    test_cases = [
        [1, 2, 3, 1],
        [2, 7, 9, 3, 1],
        [2, 1, 1, 2],
        [0],
        [1],
        [1, 2],
        [2, 1],
    ]
    for i, test in enumerate(test_cases):
        print("Test case {}: House money = {}, Max loot = {}".format(i+1, test, house_robber(test)))