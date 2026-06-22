"""
Problem: Given an integer array nums and an integer k, return true if nums has a continuous subarray of size at least two whose elements sum up to a multiple of k, or false otherwise.
Pattern: Prefix sum with hash map
Key insight: If the sum of elements from index i to j is a multiple of k, then (prefix_sum[j] - prefix_sum[i-1]) % k == 0. This implies that prefix_sum[j] % k == prefix_sum[i-1] % k. We can use a hash map to store the first occurrence of each remainder when the prefix sum is divided by k.
Time: O(n) | Space: O(min(n, k))
"""
def find_subarray_sum_multiple_of_k(nums, k):
    prefix_sum = 0
    remainder_map = {0:-1}
    PREFIX_SUM_MIN_LENGTH = 2
    for idx, num in enumerate(nums):
        prefix_sum += num
        remainder = prefix_sum if k == 0 else ((prefix_sum % k) + k) % k
        if remainder not in remainder_map:
            remainder_map[remainder] = idx
        elif idx - remainder_map[remainder] >= PREFIX_SUM_MIN_LENGTH:
            subarray_start_idx = remainder_map[remainder] + 1
            return True, nums[subarray_start_idx:idx+1]
    return False, []

"""Test code"""
if __name__ == "__main__":
    test_cases = [
        ([23, 2, 4, 6, 7], 6),
        ([23, 2, 6, 4, 7], 6),
        ([23, 2, 6, 4, 7], 13),
        ([23, 2, 6, 4, 7], 0),
        ([0, 0], 0),
        ([1, 2, 3], 5),
        ([1, 2, 3], 0),
        ([1, 2, 3], -5)]
    for nums, k in test_cases:
        result, subarray = find_subarray_sum_multiple_of_k(nums, k)
        print(f"Input: nums={nums}, k={k} => Output: {result}, Subarray: {subarray}")
