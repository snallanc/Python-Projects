"""
Python string examples
"""

"""
string[~] returns the last character of the string.
"""
def is_str_palindrome(s):
    return all(s[i] == s[~i] for i in (range(len(s)//2)))

"""
Built-in function all() takes a sequence and returns true if ALL of the items in the iterable are True.
Built-in function any() takes a sequence and returns true if ANY of the items in the iterable are True.
"""

"""
Test code
"""
if __name__ == "__main__":
    input_list = ["malayalam", "Deed", "wow", "nuN"]
    for s in input_list:
        print("Is string {0} a palindrome? {1}".format(s, is_str_palindrome(s)))
    input_list2 = [True, None]
    print(all(input_list2))
    print(any(input_list2))