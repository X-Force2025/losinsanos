from collections import deque

test_results = []
def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, vertex1, vertex2):
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
        if vertex2 not in self.adjacency_list[vertex1]:
            self.adjacency_list[vertex1].append(vertex2)
        if vertex1 not in self.adjacency_list[vertex2]:
            self.adjacency_list[vertex2].append(vertex1)

    def find_path(self, start, end):
        if start not in self.adjacency_list or end not in self.adjacency_list:
            return []
        queue = deque([[start]])
        visited = set()
        while queue:
            path = queue.popleft()
            vertex = path[-1]
            if vertex == end:
                return path
            if vertex not in visited:
                visited.add(vertex)
                for neighbor in self.adjacency_list[vertex]:
                    if neighbor not in visited:
                        queue.append(path + [neighbor])
        return []

    def is_connected(self, v1, v2):
        return bool(self.find_path(v1, v2))

def test_1_4():
    graph = Graph()
    graph.add_edge("Lima", "Cusco")
    graph.add_edge("Cusco", "Arequipa")
    graph.add_vertex("Trujillo")

    record_test("1.4.1 Direct connection path", graph.find_path("Lima", "Cusco") == ["Lima", "Cusco"])
    path = graph.find_path("Lima", "Arequipa")
    record_test("1.4.2 Indirect connection path", path[0] == "Lima" and path[-1] == "Arequipa")
    record_test("1.4.3 No path case", graph.find_path("Lima", "Trujillo") == [])
    record_test("1.4.4 Self path", graph.find_path("Lima", "Lima") == ["Lima"])
    record_test("1.4.5 Connectivity check", graph.is_connected("Lima", "Arequipa") and not graph.is_connected("Lima", "Trujillo"))

test_1_4()
for r in test_results:
    print(r)