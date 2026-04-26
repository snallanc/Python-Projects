"""
Dictionary is an equivalent of associative memory data type in python.
It stores data in the form of key-value pairs indexed by keys though it is UNORDERED.
The keys have to be immutable for being able to hash them.
"""

"""
EXAMPLE:
Dict operations
"""

d=dict(English=90,Tamil=90,Maths=100,Science=95,History=90)
d['Geography']=95
print(d) # From python 3.7, dict preserves the insertion order like OrderedDict
for k,v in d.items():
    print("key:{:<10} value:{}".format(k,v))

print("science" in d)
print("History" not in d)
print(list(d))   # prints the list of keys
d.pop("English") # pops item with the given key
print(d) # Still the insertion order is preserved
d.popitem()      # pops the last item
print(d)
print("\n")

"""
EXAMPLE:
Dict comprehension
"""
d1={x: x**x for x in [5,4,3,2,1]}
print(d1)