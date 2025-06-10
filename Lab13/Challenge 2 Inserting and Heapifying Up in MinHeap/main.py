class MinHeap:
    def __init__(self):
        # Initialize an empty list to store heap elements
        self.heap = []

    def insert(self, value):
        # Add the new value at the end of the heap
        self.heap.append(value)
        # Restore the min-heap property by heapifying up from the last index
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        # Continue to compare the node with its parent until the heap property is satisfied
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index] < self.heap[parent_index]:
                # Swap the child with its parent
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index  # Move up the tree
            else:
                break  # Stop if the parent is smaller or equal

def test_min_heap_insert():
    h = MinHeap()
    h.insert(5); print("🍀 Test 1:", h.heap == [5])
    h.insert(3); print("🍀 Test 2:", h.heap == [3,5])
    h.insert(4); print("🍀 Test 3:", h.heap == [3,5,4])
    h.insert(1); print("🍀 Test 4:", h.heap == [1,3,4,5])
    
    # 🍀 Test 5: All parent nodes must be less than or equal to their children
    valid = all(
        (h.heap[i] <= h.heap[2*i+1] if 2*i+1 < len(h.heap) else True) and
        (h.heap[i] <= h.heap[2*i+2] if 2*i+2 < len(h.heap) else True)
        for i in range(len(h.heap))
    )
    print("🍀 Test 5:", valid)

if __name__ == "__main__":
    test_min_heap_insert()
