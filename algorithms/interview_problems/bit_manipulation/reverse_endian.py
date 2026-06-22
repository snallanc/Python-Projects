def reverse_endian_32bit(n):
    return ((n & 0xFF000000 >> 24) |
           (n & 0xFF000000 >> 8 ) |
           (n & 0xFF00 << 8) |
           (n & 0xFF << 24))

def reverse_endian_pythonic(n):
    bytes = n.to_bytes(4, 'big')
    #return int.from_bytes(bytes[::-1], 'big')
    #OR
    return int.from_bytes(bytes, 'little')
