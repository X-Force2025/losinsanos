from maxheap import MaxHeap

def test_max_heap():
    h = MaxHeap()
    h.insert(1)
    print("🦁 Test 1:", h.heap == [1])

    for v in [3, 2, 8, 5]:
        h.insert(v)
    print("🦁 Test 2:", h.heap[0] == max(h.heap))  # Root should be the max

    h.delete_max()
    print("🦁 Test 3:", h.heap[0] == max(h.heap))  # New root should still be max

    h = MaxHeap()
    for v in [5, 3, 1]:
        h.insert(v)
    h.delete_max()
    print("🦁 Test 4:", h.heap == [3, 1])  # After deleting 5

    h = MaxHeap()
    h.insert(10)
    print("🦁 Test 5:", h.delete_max() == 10 and h.heap == [])  # Delete single element

if __name__ == "__main__":
    test_max_heap()
