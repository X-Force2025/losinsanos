class MaxHeap:
    def __init__(self):
        # Initialize an empty max heap
        self.heap = []

    def insert(self, value):
        # Add the value and restore max-heap property by bubbling up
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def delete_max(self):
        # Return None if heap is empty
        if not self.heap:
            return None
        max_val = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self._heapify_down(0)
        return max_val

    def build_heap(self, array):
        # Initialize heap with the given array
        self.heap = array[:]
        # Start from the last non-leaf node and heapify down
        for i in reversed(range(len(self.heap)//2)):
            self._heapify_down(i)

    def _heapify_up(self, index):
        parent = self._parent_index(index)
        while index > 0 and self.heap[index] > self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = self._parent_index(index)

    def _heapify_down(self, index):
        while self._has_left_child(index):
            larger_child_index = self._left_child_index(index)
            if self._has_right_child(index) and self.heap[self._right_child_index(index)] > self.heap[larger_child_index]:
                larger_child_index = self._right_child_index(index)

            if self.heap[index] >= self.heap[larger_child_index]:
                break
            self.heap[index], self.heap[larger_child_index] = self.heap[larger_child_index], self.heap[index]
            index = larger_child_index

    def _parent_index(self, index):
        return (index - 1) // 2 if index > 0 else -1

    def _left_child_index(self, index):
        return 2 * index + 1

    def _right_child_index(self, index):
        return 2 * index + 2

    def _has_left_child(self, index):
        return self._left_child_index(index) < len(self.heap)

    def _has_right_child(self, index):
        return self._right_child_index(index) < len(self.heap)
