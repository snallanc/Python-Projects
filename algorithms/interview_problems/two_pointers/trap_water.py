"""
Problem: Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
Pattern: Two Pointers on either side of the array
Time Complexity: O(n)
Space Complexity: O(1)
"""
def trap_rain_water(height: list[int]) -> int:
    if not height or len(height) == 0:
        return 0
    l, r, left_max, right_max, water_trapped = 0, len(height) - 1, 0, 0, 0
    while l < r:
        left_max = max(height[l], left_max)
        right_max = max(height[r], right_max)
        water_trapped += (left_max - height[l]) + (right_max - height[r])
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return water_trapped

"""Test code"""
if __name__ == "__main__":
    heights = [[0,1,0,2,1,0,1,3,2,1,2,1], [], [4,2,0,3,2,5], [10, 10, 10], [0, 0, 0, 0], [1, 0, 1, 0, 1]]
    for height in heights:
        print(f"trap_rain_water({height}) = {trap_rain_water(height)}")  # Output: 6, 0, 9