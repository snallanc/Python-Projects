"""
Collections Module:
This implements specialized container data types as alternatives to python's built-in data types.
"""

import collections

"""
ChainMap:
Used for combining mappings from multiple dictionaries in a more efficient way than regular dictionary updates.
Combines mappings from last to first ie., mappings appear from last dict arg to first dict arg.

EXAMPLE:
"""
numberToAsciiMappings = {0:48, 1:49, 2:50, 3:51, 4:52, 5:53, 6:64, 7:55, 8:56, 9:57}
letterToAsciiMappings = {"A":65, "B":66, "C":67, "D":68, "E":69, "F":70}
punctuationToExtAsciiMappings = {"'":145, '"':147, ".":149, "-":150, "_":151, "~":152}

# mappings of punctuationToAsciiMappings appear first followed by letterToAsciiMappings and numberToAsciiMappings
cm = collections.ChainMap(numberToAsciiMappings, letterToAsciiMappings, punctuationToExtAsciiMappings)
print(list(cm))
print(0 in cm)
print("a" in cm, "\n")

# Update the mappings of punctuations from Extended ASCII table to ASCII table and add a few new ones
cm['"']=34
cm["&"]=38
cm["'"]=39
cm[","]=44
cm["."]=46
cm["-"]=45
for k in ['"', ",", "&", ".", "$"]:
    print(cm.get(k))
print("\n###################################\n")


"""
Counters:
Dict subclass that keeps track of the counts of the hashtable elements with hashtable elements as keys and their counts
as values.

EXAMPLE:
Create a counter, access and delete items.
"""
elems1 = ["Apple", "apple", "banana", "pear", "PEAR",  "Mango", "peach", "PEACH", "peacH"]
cnt1 = collections.Counter([k.lower() for k in elems1])
print(cnt1)
print(cnt1['kiwi']) # Count of a non-existent item returns 0
del cnt1['kiwi']    # Deleting a non-existent item doesn't return exception

"""
EXAMPLE:
most_common(), subtract(), total() methods.
"""
cnt2 = collections.Counter(apple=1, banana=2, pear=-1)
print("Counter1: {0}".format(cnt1))
print("Counter2: {0}".format(cnt2))
print("Most common item of Counter1:", cnt1.most_common(1))
print("Most common item of Counter2:", cnt2.most_common(1))
cnt1 = cnt1.__add__(cnt2)
print("Counter1 post add: {0}".format(cnt1))
cnt1.subtract(cnt2)
print("Counter1 post subtract: {0}".format(cnt1))
print("\n###################################\n")


"""
DEQUE:
double ended queue designed for faster appends and pops from either ends
"""

"""
EXAMPLE:
Simultaneously pop and append from a deque. 
"""
que = collections.deque(["apple", "banana", "grape", "mango", "peach", "pear"])
print(que)
que.append(que.popleft())
print(que)
que.append(que.popleft())
print(que)
print("\n###################################\n")


"""
defaultdict:
It is a subclass of a dict class which is used to override default values for keys instead of None.

EXAMPLE:
"""
l = [('Roger', 100), ('Matt', 95), ('Andrew', 97), ('Roger', 90), ('Matt', 95), ('Andrew', 93)]
d = collections.defaultdict(list) # Creates a defaultdict with a default empty list([]) as value to key
d2 = {} # dict class
k = "non-existing-key"
try:
    print('d[{0}]:{1}'.format(k, d[k]))  # prints an empty list for a non-existent key instead of raising an exception.
    print('d2[{0}]:{1}'.format(k, d2[k]))  # This would raise an exception though!!
except KeyError as e:
    print("Missing key '{0}' in dict {1}".format(k, d2))

del d[k]
for k,v in l:
    d[k].append(v)
print(d.items())
print("\n###################################\n")


"""
namedtuple:
It is a subclass of tuple class which assigns names/keywords to regular tuples enabling access by both keywords and
indices.

EXAMPLE: 
"""
c = ['X', 'Y', 'Z']
NT = collections.namedtuple('Coordinates', c) # Creates a namedtuple
nt = NT(100, 200, 300)                        # Instantiates a namedtuple
# print(nt[0], nt.X) ===> Both works ie., items in namedtuples can be accessed by both indices and keywords
print(nt.__repr__)
for f in nt._fields:
    print("name:{0} value:{1}".format(f, nt.__getattribute__(f)))
print("Count of items with val 100:", nt.count(100))
ntd = nt._asdict()                            # Convert namedtuple to a dict using _asdict()
print("Converting a dict {0} to a namedtuple: {1}".format(ntd, NT(**ntd))) # Convert a dict to a namedtuple using **
print("\n")
nt2 = NT._make([1000, 1500, 2000])            # _make creates a new instance of the namedtuple, Coordinates from an
                                              # existing sequence
print(nt2.__repr__)
print("New instance with 'Z' replaced: ", nt2._replace(Z=3000))
