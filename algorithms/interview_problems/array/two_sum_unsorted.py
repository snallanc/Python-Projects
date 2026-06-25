"""
Problem: Two Sum (Unsorted)
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice. 
Example:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Pattern: Hash Map
Time Complexity: O(n)
Space Complexity: O(n)
"""

def two_sum(nums: list[int], target: int) -> list[int]:
    if not nums or len(nums) == 0:
        return []
    
    seen = {}
    for i,n in enumerate(nums):
        diff = target - n
        if diff in seen:
            return [seen[diff], i]
        
        seen[n] = i
    
    return []

"""Test code"""
if __name__ == "__main__":
    test_cases = [
        ([2, 7, 11, 15], 9),
        ([], 9),
        ([1], 10),
        ([3, 2, 4], 6),
        ([3, 3], 6),
        ([11, 10, 12, -5, -7], 8)
    ]
    
    for nums, target in test_cases:
        print(f"nums: {nums}, target: {target} => {two_sum(nums, target)}")