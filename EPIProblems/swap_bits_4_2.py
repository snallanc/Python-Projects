"""
EPI Problem 4.1: Swap bits at positions i and j of a 64-bit integer.
Solution: A bit is always 0 or 1. XORing bits i and j with 1 would flip the bits which would in turn swap them.
"""

def swap_bits(x, i, j):
    old_x = x
    swap_res = "skipped"
    if ((x >> i) & 1) != ((x >> j) & 1):
        bit_mask = (1 << i) | (1 << j)
        x ^= bit_mask
        swap_res = "done"
    print("BEGIN: Number {0}({1}), Swap bits are {2} and {3}, Swap opr {4}, END: Number {5}({6})".
          format(old_x, bin(old_x), i, j, swap_res, x, bin(x)))
    return x

"""
Test Code

swap_bits(75, 1, 2)
swap_bits(75, 0, 1)
swap_bits(75, 2, 6)
"""