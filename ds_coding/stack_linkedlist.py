"""
Stack implementation backed by LinkedList.
Push and pop operate on the front of the list (after the sentinel head) for O(1) complexity.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))
from LinkedList import LinkedList, LinkedListNode


class Stack:
    def __init__(self):
        self.ll = LinkedList()
        self.max_stack = []  # Tracks max as (data, refcount) tuples

    def count(self):
        return self.ll.count

    def count_max_stack(self):
        return len(self.max_stack)

    def is_empty(self):
        return self.ll.is_empty()

    def is_max_stack_empty(self):
        return len(self.max_stack) == 0

    def peek(self):
        if self.is_empty():
            return None
        return self.ll.head.next.data  # Top is always at the front

    def push(self, data):
        # Prepend after the sentinel head node for O(1) push
        new_node = LinkedListNode(data)
        new_node.next = self.ll.head.next
        self.ll.head.next = new_node
        if self.ll.tail is None:
            self.ll.tail = new_node
        self.ll.count += 1
        self.update_max(data, False)

    def pop(self):
        if self.is_empty():
            return None
        # Remove from front for O(1) pop
        node = self.ll.head.next
        self.ll.head.next = node.next
        if self.ll.head.next is None:
            self.ll.tail = None
        node.next = None
        self.ll.count -= 1
        self.update_max(node.data, True)
        return node.data

    def pop_all(self):
        self.ll.delete_all_nodes()
        self.max_stack.clear()

    """
    Update the max data in max_stack based on push and pop operations.
    max data is maintained as a tuple of the format: (data, refcount)
    when the refcount drops to 1, max data is removed as part of pop operation.
    """
    def update_max(self, data, is_pop=False):
        if is_pop:
            if data < self.max_stack[-1][0]:
                return
            if self.max_stack[-1][1] == 1:
                self.max_stack.pop()
            else:
                t = self.max_stack[-1]
                self.max_stack[-1] = (t[0], t[1] - 1)
        else:
            if self.is_max_stack_empty() or data > self.max_stack[-1][0]:
                self.max_stack.append((data, 1))
            elif data == self.max_stack[-1][0]:
                t = self.max_stack[-1]
                self.max_stack[-1] = (t[0], t[1] + 1)

    def get_max(self):
        return None if self.is_max_stack_empty() else self.max_stack[-1]

    """
    Printing the items of a stack is technically incorrect as it is a LIFO ADT but since this implementation
    uses a linked list, it could be printed. Adding this API for debugging purposes.
    """
    def _print_stack(self):
        print("\n############## STACK ENTRIES (top: {}, count: {}) ##############".format(self.peek(), self.count()))
        node = self.ll.head.next
        while node:
            print("Node Data {0}".format(node.data))
            node = node.next
        print("\n############## MAX-STACK ENTRIES (top: {}, count: {}) ##############".\
              format(self.get_max(), self.count_max_stack()))
        for e in reversed(self.max_stack):
            print("Node Data {0}".format(e))


"""
Test code
"""
if __name__ == "__main__":
    s = Stack()
    s._print_stack()
    push_list = [1000, 500, 1000, 5000, 1000, 2500, 5000, 10000, -10000000, 20000, 1000]
    print("\nPushing items into the stack:")
    for e in push_list:
        s.push(e)
        print("Top of stack is {0}, max data is {1}".format(s.peek(), s.get_max()))
    s._print_stack()
    print("\nPopping items from stack:")
    while not s.is_empty():
        data = s.pop()
        print("Top of stack after popping {0} is {1}, max data is {2}".format(data, s.peek(), s.get_max()))
