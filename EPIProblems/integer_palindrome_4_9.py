"""
EPI Problem 4.9: Find if the decimal digits of an integer form a palindrome or not.
12344321 => True
12344320 => False
-12344321 => False because of the negative sign.
"""

from reverse_digits_4_8 import reverse_digits
"""
1. Reverse the digits using 4.8 and compare the result with the original digits.
"""
def is_integer_palindrome(n):
    # Negative numbers can't be palindromes
    if n <= 0:
        return n == 0

    reversed_n = reverse_digits(n)
    return reversed_n == n

"""
2. Compare the LSB and MSB digits successively using mathematical expressions until they exhaust or there is a mismatch.
"""
import math
def is_integer_palindrome2(n):
    # Negative numbers can't be palindromes
    if n <= 0:
        return n == 0

    # Expression to find #digits of an integer n: floor(log10n) + 1
    num_digits = math.floor(math.log10(n)) + 1
    msb_mask = 10**(num_digits - 1)
    for i in range(num_digits // 2):
        # Expressions to get LSB and MSB: LSB = n%10, MSB = n//10**(#digits - 1)
        if n//msb_mask != n%10:
            return False
        # Adjust LSB, MSB and msb_mask by stripping off current LSB and MSB
        n %= msb_mask # strip off MSB
        n //= 10      # strip off LSB
        msb_mask //= 100 # Adjust mask by accounting for LSB and MSB adjustments
    return True

"""
Test code
"""
if __name__ == '__main__':
    input_list = [123456, -98766789, 1010101, 24688642, 0, 1, 10000]
    for n in input_list:
        res1 = is_integer_palindrome(n)
        res2 = is_integer_palindrome2(n)
        print("Is number {0} a palindrome? result1 {1}, result2 {2}".format(n, res1, res2))