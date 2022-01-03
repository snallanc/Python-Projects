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
        partition_numbers(l, pidx, preserve_sorting)
        print("Lists after rearrangement:\n\t{0}\n##################################\n".format(l))