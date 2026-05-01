# Problem: Check if any duplicates exist in a list
# Pattern: Set-based existence check
# Key insight: len(set(items)) < len(items) iff duplicates exist — set discards duplicates
# Time: O(n) | Space: O(n)
def duplicates_exist(items):
    return len(items) != len(set(items))

# Test cases
print(duplicates_exist([1, 2, 3, 4, 5]))
print(duplicates_exist([1, 2, 3, 4, 5, 1]))
print(duplicates_exist(["a", "b", "c", "d"]))
print(duplicates_exist(["a", "b", "c", "d", "d"]))
print(duplicates_exist([]))
print(duplicates_exist([1, 1, 1, 1, 1]))
print(duplicates_exist([1]))