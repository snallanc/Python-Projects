"""
namedtuple:
It is a subclass of tuple class which assigns names/keywords to regular tuples enabling access by both keywords and
indices.

EXAMPLE:
"""
import collections

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
