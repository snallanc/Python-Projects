"""
EPI Problem 4.1: Find the parity of a 64-bit integer.
Parity is 1 if the number of 1s is odd and 0 if the number of 1s is even.

Eg. 10101010101 => 0, 10001001 => 1
"""

"""
Examine all bits of the number and compute parity.
"""
def parity_brute_force(x):
    parity = 0
    count = 0 # count is not required, just added for debugging purposes
    while x:
        if (x & 1):
            count += 1
            parity ^= 1
        x >>= 1
    return count, parity

"""
Just look at the bits that are 1s to compute the parity.
Trick: x = x & (x-1) gets rid off the lowermost bit in x that is 1.
"""
def parity_improved(x):
    parity = 0
    count = 0  # count is not required, just added for debugging purposes
    while x:
        count += 1
        parity ^= 1
        x &= (x-1)
    return count, parity


"""
Test code
"""
input_list = [0b0, 0b1, 0b10, 0b11, 0b111, 0b1111, 0b10000001, 0b10101010101010101, 0b0011000011110000000011111111,
              0b10111000111110000011111110000000111111111000000000]
for num in input_list:
    count1, parity1 = parity_brute_force(num)
    count2, parity2 = parity_improved(num)
    print("Count and Parity of number {0} via\n\t1.brute-force is {1}, {2}\n\t2.improved version is {3}, {4}".\
          format(num, count1, parity1, count2, parity2))
