def reverse_endian_32bit(n):
    return ((n & 0xFF000000) >> 24) | \
           ((n & 0xFF0000) >> 8 ) | \
           ((n & 0xFF00) << 8) | \
           ((n & 0xFF) << 24)

def reverse_endian_pythonic(n):
    bytes = n.to_bytes(4, 'big')
    #return int.from_bytes(bytes[::-1], 'big')
    #OR
    return int.from_bytes(bytes, 'little')

"""Test code"""
if __name__ == "__main__":
    test_values = [0x12345678, 0xAABBCCDD, 0x0, 0xFFFFFFFF, 0x01020304, 0xDEADBEEF]
    for val in test_values:
        print(f"Input: {hex(val)} -> Output: {hex(reverse_endian_32bit(val))}, Pythonic: {hex(reverse_endian_pythonic(val))}")