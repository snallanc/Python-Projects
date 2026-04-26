def find_longest_consecutive_sequence(nums):
    nums_set = set(nums)
    max_seq_len = 0
    for n in nums:
        # Only start counting if n is the start of a sequence
        if n - 1 not in nums_set:
            len_seq = 1
            # Count the length of the sequence starting at n
            while n + len_seq in nums_set:
                len_seq += 1
            max_seq_len = max(max_seq_len, len_seq)
    return max_seq_len

# Test cases
sequences = [
    [100, 4, 200, 1, 3, 2],
    [0, -1, 1, 2, -2, 3],
    [1, 2, 0, 1],
    [9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6],
    [1, 2, 3, 4, 5],
    [10, 20, 30, 40, 50],
]

for seq in sequences:
    print(f"Longest consecutive sequence length in {seq}: {find_longest_consecutive_sequence(seq)}")

