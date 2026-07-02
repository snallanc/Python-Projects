"""
Problem: 
Given an array nums of n integers where n > 1, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].
Example:
Input:  [1,2,3,4]
Output: [24,12,8,6]
Time Complexity: O(n)
Space Complexity: O(1) (excluding the output array)
"""
def productExceptSelf(nums: list[int]) -> list[int]:
    if not nums or len(nums) == 0:
        return []
    i, prod_sofar = len(nums) - 1, 1
    res = [1] * len(nums)

    #Pass 1 - Compute Suffix product
    while i>=0:
        res[i] = prod_sofar
        prod_sofar *= nums[i]
        i -= 1
    
    #Pass 2- Compute the final product
    i, prod_sofar = 0, 1
    while i<len(nums):
        res[i] *= prod_sofar
        prod_sofar *= nums[i]
        i += 1
    return res

"""Test code"""
if __name__ == "__main__":
    nums_list = [[1, 2, 3, 4],
                 [0, 1, 2, 3],
                 [1, 0, 3, 4],
                 [1, 2, 0, 4],
                 [1, 2, 3, 0],
                 [0, 0, 3, 4],
                 [1, 0, 0, 4],
                 [1, 2, 0, 0],
                 [0, 0, 0, 4],
                 [1, 2, 3, -4]]
    for nums in nums_list:
        print(f"nums: {nums}, productExceptSelf: {productExceptSelf(nums)}")
