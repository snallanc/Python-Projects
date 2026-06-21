
def remove_adjacent_dup_chars(s: str, k: int) -> str:
    if k == 0:
        return s
    if k == 1:
        return ""
    if s is None or len(s) == 0:
        return ""

    idx = 0
    run_start = 0
    run_len = 0

    while idx < len(s):
        if idx == 0 or s[idx] != s[idx - 1]:
            run_start = idx
            run_len = 1
        else:
            run_len += 1

        if run_len == k:
            s = s[:run_start] + s[idx + 1:]
            idx = max(run_start - (k - 1), 0)
            run_len = 0
            continue
        idx += 1

    return s

def remove_adjacent_dup_chars_stack(s: str, k: int) -> str:
    if k == 0:
        return s
    if k == 1:
        return ""
    if s is None or len(s) == 0:
        return ""
    
    stack = []
    for c in s:
        if stack and stack[-1][0] ==  c:
            stack[-1][1] += 1
        else:
            stack.append([c, 1])
        if stack[-1][1] == k:
            stack.pop()
    return "".join(count * char for count, char in stack)

    
"""Test Code"""
if __name__ == "__main__":
    test_cases = {"deeedbbcccbdaa": 3, "pbbcggttciiippooaais": 2, "abcd": 2, "aabbcc": 2, "bbccdd": 3, "": 2, "b": 1, "a": 0}
    for s, k in test_cases.items():
        #print(f"Input: {s}, K: {k}, Output: {remove_adjacent_dup_chars(str(s), k)}") 
        print(f"Input: {s}, K: {k}, Output: {remove_adjacent_dup_chars_stack(str(s), k)}")