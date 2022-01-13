"""
EPI Problem 6.1: Inter-convert strings and numbers accounting for the negative sign.
ie., convert a string to its equivalent number and a number to a string of digits.
Eg. "123" => 123, "-314" => -314, 413 => "413", -526 => "-526"
"""

"""
String to number implementation:
"""
def string_to_number(s):
    neg = False
    result = 0
    for c in s:
        if c == "-":
            if neg:
                print("\t!!!Invalid number format {0}!!!".format(s))
                return None
            neg = True
            continue
        result = (result * 10) + (ord(c) - ord('0'))
    return -result if neg else result

"""
Number to string implementation:
"""
def number_to_string(n):
    neg, n2, num_list = False, n, []
    if n < 0:
        neg, n2 = True, -n
    while n2 >= 10:
        num_list.append(str(n2 % 10))
        n2 //= 10
    num_list.append(str(n2))
    if neg:
        num_list.append("-")
    num_list.reverse()
    return "".join(num_list)

"""
Test code
"""
if __name__ == "__main__":
    num_list = [123456789, -987654321]
    str_list = ["-24680", "13579", "-1234-5"]
    for n in num_list:
        print("Convert number {0} to string '{1}'".format(n, number_to_string(n)))
    for s in str_list:
        print("Convert string '{0}' to number {1}".format(s, string_to_number(s)))