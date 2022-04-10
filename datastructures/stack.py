"""
Stack implementation in python. Just a thin wrapper around python's list implementation.
"""

class Stack:
    def __init__(self):
        self.stack = []
        self.top = None
        self.count = 0

    def count(self):
        return len(self.stack)

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, data):
        self.stack.append(data)
        self.top = self.stack[-1]

    def pop(self):
        if self.is_empty():
            return None
        data = self.stack.pop()
        if self.count() > 1:
            self.top = self.stack[-1]
        return data

    def pop_all_at_once(self):
        self.stack.clear()
        self.top = None

    def peek(self):
        return self.top

    """
    Printing the items of a stack is technically incorrect as it is a LIFO ADT but since this implementation
    purely uses list, it could be printed. Adding this API for debugging purposes.
    """
    def _print_stack(self):
        print("\n############## STACK ENTRIES (top: {}, count: {}) ##############".format(self.top, self.count()))
        for e in reversed(self.stack):
            print("Node data {0}".format(e))

"""
Test code
"""
if __name__ == "__main__":
    s = Stack()
    s._print_stack()
    push_list = [1000, 5000, 500, 250, 10000, 100, 10, -10000000]
    print("\nPushing items into the stack")
    for e in push_list:
        s.push(e)
        print("Top of stack is {0}".format(s.peek()))
    s._print_stack()
    print("\nPopping items from stack")
    while data := s.pop():
        print("Top of stack is {0}".format(s.peek()))
    s._print_stack()