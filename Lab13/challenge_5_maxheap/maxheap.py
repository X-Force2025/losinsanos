class MaxHeap:
    def __init__(self):
        # Initialize an empty list for the max-heap
        self.heap = []

    def insert(self, value):
        # Add the value at the end of the heap list
        self.heap.append(value)
        # Restore the max-heap property by bubbling up
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        # Compare the element with its parent
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index] > self.heap[parent_index]:
                # If child > parent, swap them
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index
            else:
                break  # Stop when parent ≥ child

    def delete_max(self):
        if not self.heap:
            return None  # Heap is empty

        max_element = self.heap[0]  # Root is the max
        last_element = self.heap.pop()  # Remove last element

        if self.heap:
            # Replace root with last element and restore heap
            self.heap[0] = last_element
            self._heapify_down(0)

        return max_element

    def _heapify_down(self, index):
        # Compare with children and move down to restore heap
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            largest = index

            if left < len(self.heap) and self.heap[left] > self.heap[largest]:
                largest = left
            if right < len(self.heap) and self.heap[right] > self.heap[largest]:
                largest = right

            if largest != index:
                # Swap current with the larger child
                self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
                index = largest
            else:
                break

