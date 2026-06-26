"""
Problem:
Given a list of daily temperatures, return a list res such that, for each day i in the input, res[i] tells you how many days you would have to wait until a warmer temperature.
If there is no future day for which this is possible, put 0 instead. 
Pattern: Monotonic decreasing Stack
Time Complexity: O(n)
Space Complexity: O(n)
"""

def daily_temperatures(temperatures: list[int]) -> list[int]:
    if not temperatures or len(temperatures) == 0:
        return []
    stack = [(0, temperatures[0])]
    res = [0] * len(temperatures)

    for i in range(1, len(temperatures)):
        while stack and temperatures[i] > stack[-1][1]:
            t = stack.pop()
            res[t[0]] = i - t[0]
        stack.append((i, temperatures[i]))
    return res

"""Test code"""
if __name__ == "__main__":
    temperatures_list = [[73, 74, 75, 71, 69, 72, 76, 73], [], [100], [80, 80, 80, 90, 70, 85, 100], [30, 40, 50, 60], [30, 60, 90], [90, 80, 70], [70, 70, 70]]
    for temperatures in temperatures_list:
        print(f"Input: {temperatures} -> Output: {daily_temperatures(temperatures)}")