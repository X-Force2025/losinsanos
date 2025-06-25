# 📘 Challenge 3: Adding Edges and Creating Connections

test_results = []
def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

class Graph:
    def __init__(self):
        """Initialize an empty adjacency list."""
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        """Add vertex if not already in the graph."""
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, vertex1, vertex2):
        """Add undirected edge between vertex1 and vertex2."""
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
        if vertex2 not in self.adjacency_list[vertex1]:
            self.adjacency_list[vertex1].append(vertex2)
        if vertex1 not in self.adjacency_list[vertex2]:
            self.adjacency_list[vertex2].append(vertex1)

    def has_edge(self, vertex1, vertex2):
        """Check if an edge exists between vertex1 and vertex2."""
        return vertex2 in self.adjacency_list.get(vertex1, [])

    def get_neighbors(self, vertex):
        """Return all adjacent vertices (neighbors)."""
        return self.adjacency_list.get(vertex, [])

def test_1_3():
    graph = Graph()
    graph.add_vertex("Lima")
    graph.add_vertex("Cusco")
    graph.add_edge("Lima", "Cusco")
    record_test("1.3.1 Basic edge creation", graph.has_edge("Lima", "Cusco"))
    record_test("1.3.2 Bidirectional connection", graph.has_edge("Cusco", "Lima"))
    graph.add_edge("Arequipa", "Trujillo")
    record_test("1.3.3 Auto vertex creation", graph.has_edge("Arequipa", "Trujillo"))
    initial_neighbors = len(graph.get_neighbors("Lima"))
    graph.add_edge("Lima", "Cusco")
    final_neighbors = len(graph.get_neighbors("Lima"))
    record_test("1.3.4 Duplicate edge prevention", initial_neighbors == final_neighbors)
    record_test("1.3.5 Connection verification", "Cusco" in graph.get_neighbors("Lima"))

test_1_3()
for r in test_results:
    print(r)
