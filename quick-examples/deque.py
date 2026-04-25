"""
Deque:
Double ended queue designed for faster appends and pops from either ends.

EXAMPLE:
Simultaneously pop and append from a deque.
"""
import collections

que = collections.deque(["apple", "banana", "grape", "mango", "peach", "pear"])
print("Initial queue: {0}".format(que))
que.append(que.popleft())
print("Queue post pop left and append: {0}".format(que))
que.append(que.popleft())
print("Queue post pop left and append: {0}".format(que))
que.appendleft(que.pop())
print("Queue post pop and appendleft: {0}".format(que))