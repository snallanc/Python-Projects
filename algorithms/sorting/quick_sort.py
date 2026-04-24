def _lomuto_partition_with_conditional_swap(arr, low, high):
    pivot = arr[high]
    i = low - 1
    swaps = 0
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            if i != j:
                arr[i], arr[j] = arr[j], arr[i]
                swaps += 1
    if i + 1 != high:
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        swaps += 1
    return i + 1, swaps

def _lomuto_partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    swaps = 0
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            swaps += 1
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    swaps += 1
    return i + 1, swaps

def _quick_sort(arr, low, high):
    if low < high:
        pi, swaps = _lomuto_partition(arr, low, high)
        return swaps + _quick_sort(arr, low, pi - 1) + _quick_sort(arr, pi + 1, high)
    return 0

def _quick_sort2(arr, low, high):
    if low < high:
        pi, swaps = _lomuto_partition_with_conditional_swap(arr, low, high)
        return swaps + _quick_sort2(arr, low, pi - 1) + _quick_sort2(arr, pi + 1, high)
    return 0

def quick_sort(arr):
    swaps = _quick_sort(arr, 0, len(arr) - 1)
    return swaps

def quick_sort_optimised(arr):
    swaps = _quick_sort2(arr, 0, len(arr) - 1)
    return swaps


if __name__ == "__main__":
    import copy
    arr_list = [[3, 1, 4, 1, 5, 9, 2, 6], [1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [], [1], [10, 20, 30, 5, 15, 25, 35], [50, 40, 30, 20, 25, 35, 45]]
    for arr in arr_list:
        arr1 = arr.copy()
        arr2 = arr.copy()
        swaps = quick_sort(arr1)
        swaps_opt = quick_sort_optimised(arr2)
        assert arr1 == arr2, "Sorted arrays do not match!"

        print(f"Original array: {arr}, Sorted array: {arr1}")
        print(f"Without optimisation: {swaps} swaps")
        print(f"With optimisation:    {swaps_opt} swaps\n")
