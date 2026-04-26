"""
Linked List Implementation
"""

class LinkedListNode:
    def __init__(self, data = 0, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = LinkedListNode()
        self.tail = None
        self.count = 0

    def is_empty(self):
        return self.count == 0

    def search_node(self, data):
        if self.is_empty():
            return None
        node = self.head.next
        while node and node.data != data:
            node = node.next
        return node

    def insert_node(self, data):
        new_node = LinkedListNode(data)
        if not self.tail:
            self.tail = new_node
            self.head.next = self.tail
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.count += 1

    def delete_all_nodes(self):
        if self.is_empty():
            return
        node = self.head.next
        while node:
            next = node.next
            del node
            self.count -= 1
            node = next
        self.head.next = self.tail = None
        assert self.count == 0, "Node count != 0 after deleting all nodes"

    def delete_node(self, data):
        if self.is_empty():
            return None
        node = self.head
        while node.next and node.next.data != data:
            node = node.next
        if not node.next:
            return None
        del_node = node.next
        node.next = del_node.next
        del_node.next = None
        self.count -= 1
        return del_node

    def print_list(self):
        node = self.head
        print("\n############ LIST ENTRIES(head:{}, tail: {}, count: {}) ############".\
              format(self.head, self.tail, self.count))
        while node:
            print("Node: data {}, next {}".format(node.data, node.next))
            node = node.next
        print("\n")

"""
Test code
"""
if __name__ == "__main__":
    ll = LinkedList()
    ll.print_list()
    insert_nodes = [100, 200, 300, 400, 500, 600, 700]
    search_nodes = [1000, 200, 350, 700]
    del_nodes = [100, 250, 300, 700]

    # Insert
    for n in insert_nodes:
        ll.insert_node(n)
    ll.print_list()

    # Search
    for n in search_nodes:
        print("Searching node with data {}: {}".format(n, ll.search_node(n)))
    print("\n")

    # Delete
    for n in del_nodes:
        del_node = ll.delete_node(n)
        print("Deleting node with data {}: {}".format(n, del_node))
        del del_node
    print("\n")
    ll.print_list()

    # Delete List
    print("Deleting all nodes")
    ll.delete_all_nodes()
    assert ll.is_empty(), "List is not empty when it should be."
    ll.print_list()
    del ll