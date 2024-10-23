from collections import defaultdict

"""
Since we are dealing with a directed graph we will use Kosaraju's algorithm to find all Strongly Connected Components (SCCs)
This algorithm has a linear Time Complexity
And uses the Depth First Search Algorithm 
"""

class KosarajuAlgorithm:
    def __init__(self, graph):
        self.graph = graph

    def find_scc(self):
        """
        Finds all Strongly Connected Components (SCCs) in the graph.
        Returns a list of SCCs, where each SCC is a list of vertices.
        """
        vertices = self.graph.vertices
        visited = {v: False for v in vertices}
        stack = []

        # Step 1: Perform DFS on the original graph to get the finish order
        for vertex in vertices:
            if not visited[vertex]:
                self.graph.dfs(vertex, visited, stack)

        # Step 2: Reverse the graph
        reversed_graph = self.graph.reverse_graph()

        # Step 3: Perform DFS on the reversed graph in order of the stack (finish order)
        visited = {v: False for v in vertices}
        sccs = []  # List to hold all the strongly connected components

        while stack:
            v = stack.pop()
            if not visited[v]:
                component = []
                reversed_graph.dfs(v, visited, component)
                sccs.append(component)

        return sccs
