def rotated_binary_search(arr, target):
    left, right = 0, len(arr) - 1
    print(f"Searching for {target} in a rotated array {arr}")

    while left <= right:
        mid = left + (right - left)
        if arr[mid] == target:
            return mid
        if arr[left] <= arr[mid]:
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1

def rotated_bin_search_test_cases():
    ret = rotated_binary_search([4, 5, 6, 7, 0, 1, 2], 0)
    print(f"Element found at index: {ret}" if ret != -1 else "Element not found.")
    ret = rotated_binary_search([4, 5, 6, 1, 2, 3], 3)
    print(f"Element found at index: {ret}" if ret != -1 else "Element not found.")
    ret = rotated_binary_search([1], 0)
    print(f"Element found at index: {ret}" if ret != -1 else "Element not found.")
    ret = rotated_binary_search([1], 1)
    print(f"Element found at index: {ret}" if ret != -1 else "Element not found.")

if __name__ == "__main__":
    rotated_bin_search_test_cases() 