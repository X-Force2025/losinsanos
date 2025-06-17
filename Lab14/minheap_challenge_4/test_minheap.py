from minheap import MinHeap

test_results = []

def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

def test_1_4():
    heap = MinHeap()

    # 1.4.1 Empty heap deletion
    result = heap.delete_min()
    record_test("1.4.1 Empty heap deletion", result is None)

    # 1.4.2 Single element deletion
    heap.heap = [5]
    result = heap.delete_min()
    record_test("1.4.2 Single element deletion", result == 5 and heap.size() == 0)

    # 1.4.3 Multiple deletions
    heap.heap = [1, 3, 2, 7, 4]
    first = heap.delete_min()
    second = heap.delete_min()
    record_test("1.4.3 Multiple deletions", first == 1 and second == 2)

    # 1.4.4 Heap property maintenance
    heap.heap = [1, 3, 2, 7, 4, 5]
    heap.delete_min()
    valid_heap = all(
        heap.heap[i] <= heap.heap[2*i+1] if 2*i+1 < len(heap.heap) else True
        for i in range(len(heap.heap)//2)
    )
    record_test("1.4.4 Heap property maintenance", valid_heap)

    # 1.4.5 Size tracking
    initial_size = heap.size()
    heap.delete_min()
    record_test("1.4.5 Size tracking", heap.size() == initial_size - 1)

# Run tests
test_1_4()

# Print results
for r in test_results:
    print(r)
