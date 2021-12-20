"""
EPI Problem 4.3: Rearrange the bits of a 64-bit integer such that the bits appear in the reverse order.

Eg. 11001010 => 01010011
"""

from swap_bits_4_2 import *

"""
This uses the logic of swap_bits to reverse a number by incrementally swapping bit positions from the ends to the middle.
"""
def reverse_bits(x, sz):
    i, j = 0, sz - 1
    while i < j:
        # Incrementally swap from the end to the middle
        x = swap_bits(x, i, j)
        i += 1
        j -= 1

    return x

"""
Test code
"""
# 8-bit number
reverse_bits(0b11001010, 8)  # 202

# 13-bit number - odd #bits case:
reverse_bits(0b1100101000001, 13) # 6465

# 16-bit number
print("################################\n")
reverse_bits(0b1110101001100000, 16) # 60,000

# 32-bit number
print("################################\n")
reverse_bits(0b10101100110110000001110000101001, 32) # 2899844137
print("################################\n")

# 64-bit number where all bits are swapped
reverse_bits(0b1010101010101010101010101010101010101010101010101010101010101010, 64) #12297829382473034410
print("################################\n")

# 64-bit number where none of the bits are swapped
reverse_bits(0b101010101010101010101010101010101010101010101010101010101010101, 63) #6148914691236517205