from collections import defaultdict


class Graph:

    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.vertices = vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, v, visited, stack=None):
        """
        Depth First Search (DFS) utility.
        - Marks nodes as visited.
        - If 'stack' is provided, stores the finishing order of nodes in the stack.
        """
        visited[v] = True
        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self.dfs(neighbor, visited, stack)
        if stack is not None:
            stack.append(v)

    def reverse_graph(self):
        """
        Returns the reverse (transpose) of the graph where all edges are reversed.
        This is required for the second phase of Kosaraju's algorithm.
        """
        reversed_graph = Graph(self.vertices)
        for node in self.graph:
            for neighbor in self.graph[node]:
                reversed_graph.add_edge(neighbor, node)
        return reversed_graph