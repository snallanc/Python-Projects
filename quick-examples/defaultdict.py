"""
defaultdict:
It is a subclass of a dict class which is used to override default values for keys instead of None.

EXAMPLE:
"""
import collections

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
    print(d[k])
print("\n\n")

d2 = collections.defaultdict(list)
anagrams = ["tea", "eat", "tan", "ate", "nat", "bat", "tab", "abc", "xyz","",""]
c1 = collections.Counter(anagrams)
c2 = collections.Counter()
for w in anagrams:
    key = "".join(sorted(w))
    c2.update({key: 1}) # Update the count of the key in c2
    d2[key].append(w)

print("List of words: {0}\nAnagrams: {1}".format(anagrams, d2.values()))
print("Counter of anagrams: {0}".format(c1))
print("Counter of sorted anagrams: {0}".format(c2))
least_common = c2.most_common()[-2:]
print("\tTop 2 Most common anagrams: {0}\n\tTop 2 Least common anagrams: {1}".format(c2.most_common(2), least_common))