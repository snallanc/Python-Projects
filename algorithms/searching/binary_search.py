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

def bin_search_test_cases():
    ret = binary_search([1, 2, 3, 4, 5], 3)
    print(f"Element found at index: {ret}" if ret != -1 else "Element not found.")
    ret = binary_search([1, 2, 3, 4, 5], 6)
    print(f"Element found at index: {ret}" if ret != -1 else "Element not found.")
    ret = binary_search([], 1)
    print(f"Element found at index: {ret}" if ret != -1 else "Element not found.")
    ret = binary_search([1, 2, 3, 4, 5], 1)
    print(f"Element found at index: {ret}" if ret != -1 else "Element not found.")
    ret = binary_search([1, 2, 3, 4, 5], 5)
    print(f"Element found at index: {ret}" if ret != -1 else "Element not found.")
    ret = binary_search([1], 0)
    print(f"Element found at index: {ret}" if ret != -1 else "Element not found.")
    ret = binary_search([1], 1)
    print(f"Element found at index: {ret}" if ret != -1 else "Element not found.")

if __name__ == "__main__":
    bin_search_test_cases()
