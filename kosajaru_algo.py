from collections import defaultdict

"""
Since we are dealing with a directed graph we will use Kosaraju's algorithm 
This algorithm has a linear Time Complexity
And uses the Depth First Search Algorithm 
"""

class KosarajuSCC:
    def __init__(self, graph, airports):
        self.graph = graph
        self.airports = airports

    def kosaraju_scc(self):
        """Find SCCs using Kosaraju's algorithm."""
        # Step 1: First Depth First Search to get finishing times (reverse post-order)
        #Depth First Search is a graph traversal algorithm used to explore nodes and edges of a graph
        def dfs_first(node, visited, finish_order):
            visited.add(node)
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    dfs_first(neighbor, visited, finish_order)
            finish_order.append(node)

        # Step 2: Second Depth First Search on reversed graph (from end to begining)
        def dfs_second(node, visited, component, reversed_graph):
            visited.add(node)
            component.append(node)
            for neighbor in reversed_graph[node]:
                if neighbor not in visited:
                    dfs_second(neighbor, visited, component, reversed_graph)

        # First DFS
        visited = set()
        finish_order = []
        for airport in self.airports:
            if airport not in visited:
                dfs_first(airport, visited, finish_order)

        # Reverse the graph
        reversed_graph = defaultdict(list)
        for src in self.graph:
            for dst in self.graph[src]:
                reversed_graph[dst].append(src)

        # Second DFS
        visited = set()
        components = []
        for airport in reversed(finish_order):
            if airport not in visited:
                current_component = []
                dfs_second(airport, visited, current_component, reversed_graph)
                components.append(current_component)

        return components
