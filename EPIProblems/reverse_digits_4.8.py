"""
EPI Problem 4.8: Reverse the digits of an integer.
Eg. 4321 => 1234
    -9876 => -6789
"""

"""
Naive approach:
- Convert number to a string
- Reverse the string
- Convert it back to a number and aoply the sign
"""

"""
Improved version:
Use floor division with divisor as 10 and extract the quotient and remainder to reverse the digits.
"""

def reverse_digits(n):
    n2 = -n if n < 0 else n
    result = 0
    while n2 >= 10:
        r = n2 % 10
        n2 //= 10
        if not result:
            result = r
        else:
            result = (result * 10) + r
    result = (result * 10) + n2 # set the units place
    return -result if n < 0 else result

"""
Test code
"""
input_list = [123456, -987654321, 10000, -12321, 16161, 0, 1]
for n in input_list:
    print("Reverse of {0} is {1}".format(n, reverse_digits(n)))