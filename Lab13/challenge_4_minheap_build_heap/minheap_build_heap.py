class MinHeap:
    def __init__(self):
        # Initialize the heap as an empty list
        self.heap = []

    def build_heap(self, array):
        # Copy the input array to self.heap
        self.heap = array[:]
        
        # Start from the last non-leaf node and heapify down to root
        start_index = (len(self.heap) // 2) - 1
        for i in range(start_index, -1, -1):
            self._heapify_down(i)

    def _heapify_down(self, index):
        # Maintain min-heap property starting from a given index
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            smallest = index

            if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest != index:
                # Swap and continue down
                self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
                index = smallest
            else:
                break
            
def test_build_heap():
    h = MinHeap()

    h.build_heap([5, 3, 8, 1, 2])
    print("🔨 Test 1:", h.heap[0] == 1)

    h.build_heap([7, 6, 5, 4, 3, 2, 1])
    print("🔨 Test 2:", h.heap[0] == 1)

    h.build_heap([2, 1])
    print("🔨 Test 3:", h.heap == [1, 2])

    h.build_heap([10])
    print("🔨 Test 4:", h.heap == [10])

    h.build_heap([])
    print("🔨 Test 5:", h.heap == [])

if __name__ == "__main__":
    test_build_heap()
