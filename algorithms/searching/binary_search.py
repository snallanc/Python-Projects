"""
Problem: Implement binary search algorithm to find the index of a target element in a sorted array.
Pattern: Divide and Conquer
Key insight: Use two pointers to narrow down the search space by comparing the middle element with the target.
Time Complexity: O(log n) - each iteration halves the search space
Space Complexity: O(1) - only a few variables are used for pointers and indices
"""
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    print(f"Searching for {target} in a regular array {arr}")

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

"""
Problem: Implement lower_bound and upper_bound functions to find the first and last positions of a target element in a sorted array.
Pattern: Binary Search
Key insight: Use binary search to efficiently find the boundaries of the target element.
Time Complexity: O(log n) - each iteration halves the search space
Space Complexity: O(1) - only a few variables are used for pointers and indices
"""
def lower_bound(arr, target):
    l, r = 0, len(arr)
    print(f"Searching for lower bound of {target} in a sorted array {arr}")
    while l < r:
        mid = (l + r) // 2
        if arr[mid] >= target:
            r = mid
        else:
            l = mid + 1
    return l

def upper_bound(arr, target):
    l, r = 0, len(arr)
    print(f"Searching for upper bound of {target} in a sorted array {arr}")
    while l < r:
        mid = (l + r) // 2
        if arr[mid] > target:
            r = mid
        else:
            l = mid + 1
    return l

def bin_search_test_cases(fn=None):
    # Define formatter based on function type
    if fn == binary_search:
        def format_result(result):
            return f">> Element found at index: {result}" if result != -1 else "Element not found."
    elif fn == lower_bound:
        def format_result(result):
            return f">> Lower bound index: {result}"
    elif fn == upper_bound:
        def format_result(result):
            return f">> Upper bound index: {result}"
    else:
        def format_result(result):
            return str(result)
    
    # Test cases
    test_cases = [
        ([1, 2, 3, 4, 5], 3),
        ([1, 2, 3, 4, 5], 6),
        ([], 1),
        ([1, 2, 3, 4, 5], 1),
        ([1, 2, 3, 4, 5], 5),
        ([1], 0),
        ([1], 1),
    ]
    
    # Run all test cases with consistent formatter
    for arr, target in test_cases:
        ret = fn(arr, target)
        succ_str = format_result(ret)
        print(succ_str)

"""
Problem: Implement binary search algorithm to find a target element in a 2D matrix where each row is sorted and the first integer of each row is greater than the last integer of the previous row.
Pattern: Divide and Conquer 
Key insight: Treat the 2D matrix as a 1D sorted array and apply binary search. Map the 1D index back to 2D coordinates using row and column calculations.
Time Complexity: O(log(m*n)) - where m is the number of rows and n is the number of columns
Space Complexity: O(1) - only a few variables are used for pointers and indices
"""
def binary_search_2D_matrix(matrix=list[list[int]], target=int):
    if not matrix or not matrix[0]:
        return False
    rows,cols = len(matrix), len(matrix[0])
    low, high = 0, rows * cols -1
    while low <= high:
        mid = (high - low) // 2 + low
        row, col = mid // cols, mid % cols
        if target == matrix[row][col]:
            return True
        elif target > matrix[row][col]:
            low = mid + 1
        else:
            high = mid - 1
    return False
def bin_search_2D_matrix_test_cases(fn=None):
    test_cases = [
        ([[1, 3, 5], [7, 9, 11], [13, 15, 17]], 9),
        ([[1, 3, 5], [7, 9, 11], [13, 15, 17]], 4),
        ([], 1),
        ([[1]], 1),
        ([[1]], 2),
    ]
    
    for matrix, target in test_cases:
        ret = fn(matrix, target)
        print(f"Searching for {target} in matrix {matrix} => Result: {ret}")

if __name__ == "__main__":
    bin_search_test_cases(fn=binary_search)
    bin_search_test_cases(fn=lower_bound)
    bin_search_test_cases(fn=upper_bound)
    bin_search_2D_matrix_test_cases(fn=binary_search_2D_matrix)
