def insertion_sort(arr):
    loop_counter = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            loop_counter += 1
        arr[j + 1] = key
        loop_counter += 1
    print(f"Total iterations: {loop_counter}")

# test code
if __name__ == "__main__":
    arr_list = [[12, 11, 13, 5, 6], [], [1], [5, 4, 3, 2, 1], [1, 2, 3, 4, 5]]
    for arr in arr_list:
        print("Original array:", arr)
        insertion_sort(arr)
        print(f"Sorted array: {arr} \n\n")