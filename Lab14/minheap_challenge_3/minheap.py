class MinHeap:
    def __init__(self):
        # Initialize an empty list to represent the heap
        self.heap = []

    def insert(self, value):
        # Add the new value at the end of the list
        self.heap.append(value)
        # Restore the heap property by bubbling it up
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        # Move the value at the given index up to its correct position
        parent = self._parent_index(index)
        while index > 0 and self.heap[index] < self.heap[parent]:
            # Swap if the current value is smaller than its parent
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = self._parent_index(index)

    def _parent_index(self, index):
        # Return the index of the parent node
        return (index - 1) // 2 if index > 0 else -1

    def size(self):
        # Return the number of elements in the heap
        return len(self.heap)

    def peek(self):
        # Return the smallest element without removing it
        return self.heap[0] if self.heap else None
