class MinHeap:
    def __init__(self):
        # Initializes the heap as an empty list
        self.heap = []

    def delete_min(self):
        # If heap is empty, return None
        if not self.heap:
            return None
        
        # The smallest element is at the root (index 0)
        min_element = self.heap[0]
        
        # Move the last element to the root and remove it from the end
        last_element = self.heap.pop()
        if self.heap:
            self.heap[0] = last_element
            # Restore the heap property starting from root
            self._heapify_down(0)
        
        return min_element

    def _heapify_down(self, index):
        # Keep moving down the tree until heap property is satisfied
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            smallest = index

            # Compare with left child
            if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
                smallest = left

            # Compare with right child
            if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
                smallest = right

            # If the smallest is not the current index, swap and continue
            if smallest != index:
                self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
                index = smallest
            else:
                break

def test_min_heap_delete_min():
    h = MinHeap()
    print("🧹 Test 1:", h.delete_min() is None)

    h.heap = [1]
    print("🧹 Test 2:", h.delete_min() == 1 and h.heap == [])

    h.heap = [1, 3, 2]
    print("🧹 Test 3:", h.delete_min() == 1 and h.heap == [2, 3])

    h.heap = [1, 3, 4, 5]
    print("🧹 Test 4:", h.delete_min() == 1 and h.heap == [3, 5, 4])

    h.heap = [1, 2, 3, 4, 5]
    print("🧹 Test 5:", h.delete_min() == 1)

if __name__ == "__main__":
    test_min_heap_delete_min()
