"""
EPI Problem 4.3: Rearrange the bits of a 64-bit integer such that the bits appear in the reverse order.

Eg. 11001010 => 01010011
"""

from swap_bits_4_2 import swap_bits

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
input_list = [
          "0b11001010", # 8-bit number, 202
          "0b1100101000001", # 13-bit number, 6465 ie., odd number of bits case
          "0b1110101001100000", # 16-bit number, 60,000
          "0b10101100110110000001110000101001", # 32-bit number, 2899844137
          "0b1010101010101010101010101010101010101010101010101010101010101010", # 64-bit number, 12297829382473034410
                                                                                # where all bits are swapped
          "0b101010101010101010101010101010101010101010101010101010101010101"   # 64-bit number, 6148914691236517205
                                                                                # where none of the bits are swapped
          ]

for num in input_list:
    reverse_bits(int(num, 2), len(num) - 2 ) # len - 2 to discard the prefix 0b)
    print("################################\n")