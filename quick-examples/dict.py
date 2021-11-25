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
print(d)
for k,v in d.items():
    print("key:", k, "value:", v)

print("science" in d)
print("History" not in d)
print(list(d)) # prints the list of keys

# Dict comprehension
d1={x: x**x for x in [5,4,3,2,1]}
print(d1)