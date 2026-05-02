# Problem: Find all unique triplets in array that sum to zero (Leetcode 15)
# Pattern: Sort + Two Pointers
# Approach: Fix nums[i], then use two pointers on nums[i+1..n-1] to find pair summing to -nums[i]
# Duplicate handling:
#   - Outer: skip nums[i] if same as previous (avoids duplicate triplets with same fixed element)
#   - Inner: after match, skip duplicate p0/p1 values before advancing pointers
#   - nums[i] > 0 → break: sorted array, all remaining elements positive, zero sum impossible
# Time: O(n log n + n²) = O(n²) | Space: O(1) excluding output
def three_sum_zero(nums=[]):
    if not nums:
        return []
    nums.sort()
    result = []
    for i in range(len(nums)):
        # Skip duplicates for i
        if i > 0 and nums[i] == nums[i-1]:
            continue
        p0, p1 = i+1, len(nums) - 1
        if nums[i] > 0:   # sorted, all right elements positive, no zero sum possible
            break
        while p0 < p1:
            if nums[i] + nums[p0] + nums[p1] == 0:
                result.append([nums[i], nums[p0], nums[p1]])
                # Skip duplicates for p0 and p1
                while p0 < p1 and nums[p0] == nums[p0+1]: p0 += 1
                while p0 < p1 and nums[p1] == nums[p1-1]: p1 -= 1
                p0 += 1
                p1 -= 1
            elif nums[i] + nums[p0] + nums[p1] < 0:
                p0 += 1
            else:
                p1 -= 1
    return result

# Test code
if __name__ == "__main__":
    test_cases = [
        [-4, -1, 0, 1, 2],  # [[-1, 0, 1]]
        [-3, 0, 3],          # [[-3,0,3]]
        [-1, 0, 1, 2],       # [[-1,0,1]]
        [0, 1, 2],           # [] (no negatives)
        [-1, -2, 3],         # [[-2,-1,3]]
        [],                  # []
        [0],                 # []
        [-1, -1, 0, 1, 1, 2], # [[-1,0,1], [-1,-1,2]]
        [-2, -1, -1, 0, 1, 1, 2, 2], # [[-2,0,2], [-1,-1,2], [-1,0,1]]
        [0, 0, 0]             # [[0,0,0]]
    ]
    for nums in test_cases:
        print("three_sum({}) = {}".format(nums, three_sum_zero(nums[:])))
