# 📘 Challenge 2: Adding Vertices and Basic Structure

test_results = []
def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

class Graph:
    def __init__(self):
        """Initialize the graph with an empty adjacency list."""
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        """Add a vertex to the graph if it doesn't exist."""
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def get_vertices(self):
        """Return all vertex names in the graph."""
        return list(self.adjacency_list.keys())

    def get_vertex_count(self):
        """Return the number of vertices."""
        return len(self.adjacency_list)

    def has_vertex(self, vertex):
        """Check if a vertex exists."""
        return vertex in self.adjacency_list

def test_1_2():
    graph = Graph()
    graph.add_vertex("Lima")
    record_test("1.2.1 Single vertex addition", graph.has_vertex("Lima"))
    graph.add_vertex("Cusco")
    graph.add_vertex("Arequipa")
    record_test("1.2.2 Multiple vertex addition", graph.get_vertex_count() == 3)
    initial_count = graph.get_vertex_count()
    graph.add_vertex("Lima")
    record_test("1.2.3 Duplicate prevention", graph.get_vertex_count() == initial_count)
    record_test("1.2.4 Vertex isolation", len(graph.adjacency_list.get("Lima", [])) == 0)
    graph.add_vertex("Trujillo")
    record_test("1.2.5 Graph size tracking", "Trujillo" in graph.get_vertices())

test_1_2()

for r in test_results:
    print(r)