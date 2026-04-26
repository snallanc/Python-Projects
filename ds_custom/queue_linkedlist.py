"""
Queue implementation backed by LinkedList.
Enqueue appends to the tail, dequeue removes from the front — both O(1).
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))
from LinkedList import LinkedList, LinkedListNode


class Queue:
    def __init__(self):
        self.ll = LinkedList()

    def count(self):
        return self.ll.count

    def is_empty(self):
        return self.ll.is_empty()

    def enqueue(self, data):
        self.ll.insert_node(data)  # insert_node appends to tail — O(1)

    def dequeue(self):
        if self.is_empty():
            return None
        # delete_node starts from the sentinel head, so head.next is found on the first check — O(1)
        node = self.ll.delete_node(self.ll.head.next.data)
        return node.data if node else None

    def peek(self):
        if self.is_empty():
            return None
        return self.ll.head.next.data

    def peek_tail(self):
        if self.is_empty():
            return None
        return self.ll.tail.data

    def dequeue_all(self):
        self.ll.delete_all_nodes()

    def _print_queue(self):
        print("\n############## QUEUE ENTRIES (front: {}, rear: {}, count: {}) ##############".format(
            self.peek(), self.peek_tail(), self.count()))
        node = self.ll.head.next
        while node:
            print("Node Data {0}".format(node.data))
            node = node.next


"""
Test code
"""
if __name__ == "__main__":
    q = Queue()
    q._print_queue()

    enqueue_list = [100, 200, 300, 400, 500]
    print("\nEnqueueing items:")
    for e in enqueue_list:
        q.enqueue(e)
        print("Front: {0}, Rear: {1}".format(q.peek(), q.peek_tail()))
    q._print_queue()

    print("\nDequeueing items:")
    while not q.is_empty():
        data = q.dequeue()
        print("Dequeued: {0}, Front now: {1}".format(data, q.peek()))
