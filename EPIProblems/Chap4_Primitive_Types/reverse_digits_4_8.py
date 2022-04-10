"""
EPI Problem 4.8: Reverse the digits of an integer.
-9876 => -6789
"""

"""
1. Naive approach:
- Convert number to a string
- Reverse the string
- Convert it back to a number and aoply the sign
"""

"""
2. Improved version:
Use floor division with divisor as 10 and extract the quotient and remainder to reverse the digits.
"""

def reverse_digits(n):
    n2 = -n if n < 0 else n
    result = 0
    while n2 >= 10:
        result = (result * 10) + n2 % 10
        n2 //= 10
    result = (result * 10) + n2 # set the units place
    return -result if n < 0 else result

"""
Test code
"""
if __name__ == '__main__':
    input_list = [123456, -987654321, -1010101, -123321, 161612, 0, 1, 10001]
    for n in input_list:
        res = reverse_digits(n)
        print("Reverse of number {0} is {1}. Is this a palindrome? {2}".format(n, res, ((n >= 0) and (n == res))))
