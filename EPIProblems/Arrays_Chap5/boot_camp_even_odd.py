"""
Chapter 5: Boot camp problem.
Re-aarange an array of integers in such a way that even numbers appear before odd numbers without using additional
space.

Eg. 1 2 3 4 5 6 7 8 => 2 4 6 8 <followed by odd numbers>
Note: Order of odd numbers could change.
"""

"""
Solution: Have two indices - one index to keep track of the position to place the next even number and other to iterate
the list.
"""
def even_odd_numbers(A):
    even_idx = 0
    for j in range(len(A)):
        if A[j] % 2 != 0: # Odd number
            continue
        # Even number, move A[j] to the next even_idx
        A[even_idx], A[j] = A[j], A[even_idx]
        even_idx += 1

"""
Test code:
"""
if __name__ == '__main__':
    input_list = [[i*2+1 for i in range(0, 9)],  # Odd numbers
                  [i * 2 for i in range(0, 15)], # even numbers
                  [1, 2, 3, 4, 5, 6, 7, 8],     # even and odd numbers
                  [-i for i in range(0, 10)]]    # even and odd negative numbers
    print("Lists before rearrangement:\n\t{0}".format(input_list))
    for l in input_list:
        even_odd_numbers(l)
    print("Lists after rearrangement:\n\t{0}".format(input_list))
