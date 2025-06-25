test_results = []
def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, v):
        if v not in self.adjacency_list:
            self.adjacency_list[v] = []

    def add_edge(self, v1, v2):
        self.add_vertex(v1)
        self.add_vertex(v2)
        if v2 not in self.adjacency_list[v1]:
            self.adjacency_list[v1].append(v2)
        if v1 not in self.adjacency_list[v2]:
            self.adjacency_list[v2].append(v1)

    def get_degree(self, vertex):
        return len(self.adjacency_list.get(vertex, []))

    def find_all_paths(self, start, end, max_length=None, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if start not in self.adjacency_list:
            return []
        paths = []
        for neighbor in self.adjacency_list[start]:
            if neighbor not in path and (max_length is None or len(path) < max_length):
                newpaths = self.find_all_paths(neighbor, end, max_length, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths

    def get_connected_components(self):
        visited = set()
        components = []
        for v in self.adjacency_list:
            if v not in visited:
                stack = [v]
                component = []
                while stack:
                    node = stack.pop()
                    if node not in visited:
                        visited.add(node)
                        component.append(node)
                        stack.extend([n for n in self.adjacency_list[node] if n not in visited])
                components.append(component)
        return components

def test_1_5():
    graph = Graph()
    graph.add_edge("Lima", "Cusco")
    graph.add_edge("Lima", "Arequipa")
    graph.add_edge("Cusco", "Arequipa")
    graph.add_edge("Trujillo", "Piura")

    record_test("1.5.1 Degree calculation", graph.get_degree("Lima") == 2)
    paths = graph.find_all_paths("Lima", "Arequipa", max_length=3)
    record_test("1.5.2 Multiple paths finding", len(paths) >= 2)
    record_test("1.5.3 Connected components", len(graph.get_connected_components()) == 2)
    empty = Graph()
    record_test("1.5.4 Empty graph analysis", empty.get_connected_components() == [])
    record_test("1.5.5 Non-existent vertex handling", graph.get_degree("NonExistent") == 0)

test_1_5()
for r in test_results:
    print(r)