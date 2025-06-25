# 📘 Challenge 1: Basic Graph Foundation

test_results = []
def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

class Graph:
    def __init__(self):
        """Initialize an empty graph using an adjacency list."""
        self.adjacency_list = {}

    def get_vertices(self):
        """Return all vertices in the graph as a list."""
        return list(self.adjacency_list.keys())

    def get_vertex_count(self):
        """Return the number of vertices in the graph."""
        return len(self.adjacency_list)

    def has_vertex(self, vertex):
        """Check whether a vertex exists in the graph."""
        return vertex in self.adjacency_list

def test_1_1():
    graph = Graph()
    record_test("1.1.1 Empty graph initialization", graph.get_vertex_count() == 0)
    graph.adjacency_list = {"Lima": [], "Cusco": []}
    record_test("1.1.2 Vertex counting", graph.get_vertex_count() == 2)
    record_test("1.1.3 Vertex existence check", graph.has_vertex("Lima") == True)
    empty_graph = Graph()
    record_test("1.1.4 Empty graph edge case", empty_graph.has_vertex("Lima") == False)
    record_test("1.1.5 Type validation", isinstance(graph.get_vertices(), list))

test_1_1()

for r in test_results:
    print(r)