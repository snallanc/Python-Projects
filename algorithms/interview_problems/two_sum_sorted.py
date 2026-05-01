# Problem: Find two numbers in a SORTED array that sum to target (Leetcode 167)
# Pattern: Two Pointers from opposite ends
# Key: sum < target → move left pointer right (increase sum)
#      sum > target → move right pointer left (decrease sum)
# NOTE: Array MUST be sorted. For unsorted arrays, use hash map O(n) space.
# Time: O(n) | Space: O(1)
def two_sum_sorted(nums=[], target=0):
    if not nums:
        return []
    p0, p1 = 0, len(nums) - 1
    while p0 != p1:
        if nums[p0] + nums[p1] == target:
            return [p0, p1]
        elif nums[p0] + nums[p1] < target:
            p0 += 1
        else:
            p1 -= 1

    return []

# Test code
if __name__ == "__main__":
    test_cases = [
        ([2, 7, 11, 15], 9),
        ([1, 2, 3, 4, 5], 9),
        ([1, 2, 3, 4, 5], 10),
        ([], 0),
        ([1], 1),
        ([1, 2], 3),
        ([1, 2], 4),
        ([-3, -1, 0, 2, 4, 6], -1)
    ]
    for i, (nums, target) in enumerate(test_cases):
        print("Test case {}: nums = {}, target = {}, result = {}".format(i+1, nums, target, two_sum_sorted(nums, target)))
