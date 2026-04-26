"""
Set is an unordered collection of unique items.
Supports union, intersection, difference and symmetric difference operations.
"""

"""
EXAMPLE:
Set operations
"""

a={3,6,9,12,15,18}
b={2,4,6,8,10,12,14,16,18}
print("a|b:", a|b) # union
print("a&b:", a&b) # intersection
print("a-b:", a-b) # items in a that are not in b
print("b-a:", b-a) # items in b that are not in a
print("a^b:", a^b) # symmetric difference => a-b + b-a

"""
EXAMPLE:
Set comprehension
"""
c={x for x in a|b if x%4 == 0} # Multiples of 4 in a union b
print("Multiples of 4 in a|b:",c)
