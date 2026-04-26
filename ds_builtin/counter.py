"""
Counter:
Dict subclass that keeps track of the counts of the hashtable elements with hashtable elements as keys and their counts
as values.

EXAMPLE:
Create a counter, access and delete items.
"""
import collections

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
