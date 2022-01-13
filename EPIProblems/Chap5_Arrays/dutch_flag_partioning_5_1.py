"""
EPI Problem 5.1: Dutch Flag Partitioning(used in quick sort) - re-arrange/partition a list of numbers based on pivot in
such a way that numbers lesser than pivot appear first, followed by numbers equal to the pivot followed by
numbers greater than the pivot.
"""

"""
Solution 1: Re-arrange in 2 passes:
1. Move numbers lesser than the pivot to the left end in the first pass and then
2. Move numbers greater than the pivot in the second pass.
Complexity: O(n^2)
"""

import copy
def partition_numbers(A, pivot_idx, preserve_sorting=False):
    pivot = A[pivot_idx]
    # Pass 1: numbers < pivot move to the left end
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if A[j] < pivot:
                if preserve_sorting and A[i] < A[j]:
                    continue
                # Swap A[i] and A[j], i tracks the pos where next number < pivot needs to go
                A[i], A[j] = A[j], A[i]
                # Pos i is now taken, so break here to bump i and proceed
                break

    # Pass 2: numbers > pivot move to the right end
    for i in reversed(range(len(A))):
        for j in reversed(range(i)):
            if A[j] > pivot:
                if preserve_sorting and A[i] > A[j]:
                    continue
                # Swap A[i] and A[j], i tracks the pos where next number > pivot needs to go
                A[i], A[j] = A[j], A[i]
                # Pos i is now taken, so break here to bump i and proceed
                break
    return A

"""
Solution 2: Re-arrange in 2 passes but in each pass just walk over the list of numbers once without using a nested loop.
Complexity: O(n)
"""
def partition_numbers_linear_2pass(A, pivot_idx):
    i = 0
    pivot = A[pivot_idx]
    # Pass 1
    for j in range(len(A)):
        if A[j] < pivot:
            A[i], A[j] = A[j], A[i]
            i += 1
    # Pass 2
    i, j = len(A) - 1, len(A) - 1
    while A[j] >= pivot:
        if A[j] > pivot:
            A[i], A[j] = A[j], A[i]
            i -= 1
        j -= 1
    return A

"""
Solution 3: Similar to solution 2 but rearrange in one pass.
Complexity: O(n)
"""
def partition_numbers_linear_1pass(A, pivot_idx):
    """
    i -> tracks indices for nos < pivot
    j -> tracks indices for nos > pivot
    k -> tracks the index of the current number
    """
    i, j, k = 0, len(A)-1, 0
    pivot = A[pivot_idx]
    while k <= j:
        if A[k] < pivot:
            A[i], A[k] = A[k], A[i]
            i, k = i + 1, k + 1
        elif A[k] > pivot:
            A[j], A[k] = A[k], A[j]
            j -= 1
        else:
            k += 1
    return A

"""
Test code
"""
if __name__ == '__main__':
    input_list = [
                     ([1000, 500, 1500, 750, 1250, 250, 1750, -250, -1000, 2000, 775, 725, 750], 3, False), # unsorted list
                     ([1000, 500, 1500, 750, 1250, 250, 1750, -250, -1000, 2000, 775, 725, 750], 3, True),  # unsorted list, preserve order
                     ([100, 200, 300, 400, 400, 500, 600, 700, 800], 2, False),  # sorted list
                     ([100, 200, 300, 400, 400, 500, 600, 700, 800], 2, True),  # sorted list, preserve order
                     ([1000, 800, 600, 400, 200, 0, -200, -400, -600, -800], 5, False), # reverse sorted list
                     ([1000, 800, 600, 400, 200, 0, -200, -400, -600, -800], 5, True)  # reverse sorted list, preserve order
                 ]
    for t in input_list:
        l, pidx, preserve_sorting = t
        print("List before rearrangement:\n\t{0}, pivot:{1}, preserve sort order? {2}".format(l, l[pidx], preserve_sorting))
        res1 = partition_numbers(copy.deepcopy(l), pidx, preserve_sorting)
        res2 = partition_numbers_linear_2pass(copy.deepcopy(l), pidx)
        res3 = partition_numbers_linear_1pass(copy.deepcopy(l), pidx)
        print("List after rearrangement(sol1):\n\t{0}".format(res1))
        print("List after rearrangement(sol2):\n\t{0}".format(res2))
        print("List after rearrangement(sol3):\n\t{0}\n\n##################################\n".format(res3))