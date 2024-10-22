from collections import defaultdict

class DirectedGraph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, src, dst):
        """Add an edge from `src` to `dst` in the directed graph."""
        self.graph[src].append(dst)

    def reverse(self):
        """Return the reversed version of the graph."""
        reversed_graph = defaultdict(list)
        for src in self.graph:
            for dst in self.graph[src]:
                reversed_graph[dst].append(src)
        return reversed_graph
