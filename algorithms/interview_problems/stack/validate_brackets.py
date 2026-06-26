"""
Problem:
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Pattern: Use stack to push opening braces and pop when a closing brace is found. If the stack is empty at the end, the string is valid.
Time Complexity: O(n)
Space Complexity: O(n)
"""

def is_valid(s: str) -> bool:
    stack = []
    for c in s:
        if c in ["(", "[", "{"]:
            stack.append(c)
        elif (c == ")" and stack[-1] == "(") or \
             (c == "]" and stack[-1] == "[") or \
             (c == "}" and stack[-1] == "{"):
             stack.pop()
    return len(stack) == 0

"""Test code"""
if __name__ == "__main__":
    test_strings = ["()", "()[]{}", "(]", "([)]", "{[]}"]
    for s in test_strings:
        print(f"Input: {s} -> Output: {is_valid(s)}")