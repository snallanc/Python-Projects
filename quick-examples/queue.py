"""
DEQUE:
double ended queue designed for faster appends and pops from either ends
"""

from collections import deque
"""
EXAMPLE:
Simultaneously pop and append from a deque. 
"""
que = deque(["apple", "banana", "grape", "mango", "peach", "pear"])
print(que)
que.append(que.popleft())
print(que)
que.append(que.popleft())
print(que)