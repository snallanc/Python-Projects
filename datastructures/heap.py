class Heap:
    def __init__(self, comparator):
        """comparator(a, b) returns True when a should be closer to the root than b."""
        self._data = []
        self._cmp = comparator

    def _parent(self, i):
        if i <= 0:
            raise IndexError("root has no parent")
        return (i - 1) // 2

    def _left(self, i):
        return 2 * i + 1

    def _right(self, i):
        return 2 * i + 2

    def _sift_up(self, i):
        while i > 0:
            p = self._parent(i)
            if self._cmp(self._data[i], self._data[p]):
                self._data[p], self._data[i] = self._data[i], self._data[p]
                i = p
            else:
                break

    def _sift_down(self, i):
        n = len(self._data)
        while True:
            top = i
            l, r = self._left(i), self._right(i)
            if l < n and self._cmp(self._data[l], self._data[top]):
                top = l
            if r < n and self._cmp(self._data[r], self._data[top]):
                top = r
            if top == i:
                break
            self._data[i], self._data[top] = self._data[top], self._data[i]
            i = top

    def push(self, val):
        self._data.append(val)
        self._sift_up(len(self._data) - 1)

    def pop(self):
        if not self._data:
            raise IndexError("pop from empty heap")
        root = self._data[0]
        self._data[0] = self._data[-1]
        self._data.pop()
        if self._data:
            self._sift_down(0)
        return root

    def peek(self):
        if not self._data:
            raise IndexError("peek from empty heap")
        return self._data[0]

    def __len__(self):
        return len(self._data)

def heapify(iterable, comparator):
    h = Heap(comparator)
    for v in iterable:
        h.push(v)
    return h

def MinHeap(iterable=[]):
    return heapify(iterable, comparator=lambda a, b: a < b)

def MaxHeap(iterable=[]):
    return heapify(iterable, comparator=lambda a, b: a > b)

# Test code
if __name__ == "__main__":
    elems = [5, 3, 8, 1, 9, 2]
    print("Original list:", elems)
    min_h = MinHeap(elems)
    res = [min_h.pop() for _ in range(len(min_h))]
    print("Min-heap sorted:", res)
    assert res == sorted(elems.copy())

    max_h = MaxHeap(elems)
    res = [max_h.pop() for _ in range(len(max_h))]
    print("Max-heap sorted:", res)
    assert res == sorted(elems, reverse=True)