"""
List is an ordered collection of items of identical or different types where duplicates are allowed.
"""

"""
enumerate():
Enumerates a sequence and returns a sequence of tuples each of len 2 wherein the 1st item is the index
and the second item being the value from the original sequence.

EXAMPLE:
Enumerate a list
"""
l=["One","Two","Three","Four","Five"]
for i,j in enumerate(l, start=1):
    print(i,j)
print("\n")

"""
zip():
Walks multiple sequences in parallel and returns a iterable sequence of tuples containing one element
from each sequence. Implicitly assumes that the input sequences are of the same length.

EXAMPLE:
zip a list
"""
l2=[1,2,3,4,5]
for x,y in zip(l,l2):
    print(x,y)
print("\n")


"""
LIST COMPREHENSION:
list comprehension is a concise way to operate on a list.

EXAMPLE:
Return a list of tuples such that the elements of the tuples are unique
"""
lc = [(x,y,z) for x in [1,2,3] for y in [2,3,4] for z in [3,4,5] if x!=y if y!=z if x!=z]
print(lc)
print("\n")

"""
sorted():
Returns a new sequence of sorted elements independent of the original sequence.

EXAMPLE:
"""
for i in sorted([10,8,6,4,2,0]):
    print(i)
print("\n")

"""
reversed():
Returns a reversed sequence of elements from the original sequence.

EXAMPLE:
"""
for i in reversed(range(10)):
    print(i)
print("\n")
