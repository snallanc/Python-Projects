"""
Problem: Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.
Koko can decide her eating speed of k bananas per hour. If the pile has less than k bananas, she will eat all of them instead. We need to find the minimum integer k such that she can eat all the bananas within h hours.
Key Insight: Use binary search to find the minimum eating speed k. The search space is between 1 and the maximum number of bananas in a pile. For each mid value, calculate the total hours needed to eat all piles and adjust the search space accordingly.
Time Complexity: O(n log m) - where n is the number of piles and m is the maximum number of bananas in a pile. The binary search runs in log m time, and for each mid value, we iterate through all piles to calculate the total hours.
Space Complexity: O(1) - only a few variables are used for pointers and indices.
"""
import math

def max_eating_speed(piles=list[int], h=int):
    if not piles or h <= 0:
        return 0
    min_speed, max_speed = 0, max(piles)
    while min_speed < max_speed:
        cur_speed = (max_speed - min_speed) // 2 + min_speed
        hr_count = 0
        for p in piles:
            hr_count += math.ceil(p / cur_speed)
        if hr_count > h:
            min_speed = cur_speed + 1
        else:
            max_speed = cur_speed
    return max_speed

"""Test Code"""
if __name__ == "__main__":
    list_of_piles = [([3, 6, 7, 11], 8), ([30, 11, 23, 4, 20], 5), ([30, 11, 23, 4, 20], 6), ([5,4,3,2,1], 0), ([], 2)]
    for piles, h in list_of_piles:
        print(f"Input piles: {piles}, h: {h}")
        print(f"Max eating speed: {max_eating_speed(piles, h)}\n")
