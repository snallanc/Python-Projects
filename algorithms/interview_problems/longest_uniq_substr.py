def find_long_uniq_substr(S):
    if not S:
        return 0, ""
    l, max_l, max_len = 0, 0, 0
    seen = {}
    for r,c in enumerate(S):
        if c in seen and seen[c] >= l:
            l = seen[c] + 1
        seen[c] = r
        if r - l + 1 > max_len:
            max_len = r - l + 1
            max_l = l
    return max_len, S[max_l : max_l + max_len]

# Test code
if __name__ == "__main__":
    test_cases = [
        "abcabcbb",  # 3 ("abc")
        "bbbbb",     # 1 ("b")
        "pwwkew",    # 3 ("wke")
        "",          # 0
        " ",         # 1 (" ")
        "au",        # 2 ("au")
        "dvdf",      # 3 ("vdf")
        "anviaj",    # 5 ("nviaj")
    ]
    for s in test_cases:
        length, substr = find_long_uniq_substr(s)
        print("Length of longest unique substring in '{}' is {}, substring: '{}'".format(s, length, substr))