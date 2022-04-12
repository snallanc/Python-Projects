"""
Stack implementation in python. Just a thin wrapper around python's list implementation.
"""

class Stack:
    def __init__(self):
        self.stack = [] # Actual stack
        self.top = None
        self.max_stack = [] # Stack to keep track of max data items

    def count(self):
        return len(self.stack)

    def count_max_stack(self):
        return len(self.max_stack)

    def is_empty(self):
        return len(self.stack) == 0

    def is_max_stack_empty(self):
        return len(self.max_stack) == 0

    def push(self, data):
        self.stack.append(data)
        self.top = self.stack[-1]
        self.update_max(data, False)

    def pop(self):
        if self.is_empty():
            return None
        data = self.stack.pop()
        self.update_max(data, True)
        self.top = None if self.is_empty() else self.stack[-1]

        return data

    def pop_all(self):
        self.stack.clear()
        self.max_stack.clear()
        self.top = None

    def peek(self):
        return self.top

    """
    Update the max data in max_stack based on push and pop operations
    max data is maintained as a tuple of the format: (data, refcount)
    when the refcount drops to 1, max data is removed as part of pop operation.
    """
    def update_max(self, data, is_pop = False):
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
            else:
                return

    # Get the node with the max data
    def get_max(self):
        return None if self.is_max_stack_empty() else self.max_stack[-1]

    """
    Printing the items of a stack is technically incorrect as it is a LIFO ADT but since this implementation
    purely uses list, it could be printed. Adding this API for debugging purposes.
    """
    def _print_stack(self):
        print("\n############## STACK ENTRIES (top: {}, count: {}) ##############".format(self.peek(), self.count()))
        for e in reversed(self.stack):
            print("Node Data {0}".format(e))
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
    s._print_stack()