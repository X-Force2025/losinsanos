class MinHeap:
    def __init__(self):
        # Initialize an empty heap
        self.heap = []

    def delete_min(self):
        # Return None if the heap is empty
        if not self.heap:
            return None
        # Swap the root with the last element
        min_val = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()  # Remove the last element
        # Restore heap property by bubbling down the new root
        self._heapify_down(0)
        return min_val

    def _heapify_down(self, index):
        # Restore heap property by moving the value at index down
        while self._has_left_child(index):
            # Find smaller child to potentially swap with
            smaller_child_index = self._left_child_index(index)
            if self._has_right_child(index) and self.heap[self._right_child_index(index)] < self.heap[smaller_child_index]:
                smaller_child_index = self._right_child_index(index)

            if self.heap[index] <= self.heap[smaller_child_index]:
                break
            # Swap and continue
            self.heap[index], self.heap[smaller_child_index] = self.heap[smaller_child_index], self.heap[index]
            index = smaller_child_index

    def _left_child_index(self, index):
        return 2 * index + 1

    def _right_child_index(self, index):
        return 2 * index + 2

    def _has_left_child(self, index):
        return self._left_child_index(index) < len(self.heap)

    def _has_right_child(self, index):
        return self._right_child_index(index) < len(self.heap)

    def size(self):
        return len(self.heap)
