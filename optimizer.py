from graph import Graph
from kosajaru_algo import KosarajuAlgorithm


class FlightRouteOptimizer:
    """
    Class to optimize flight routes by minimizing the number of additional routes required
    to make all airports reachable from a starting airport.
    """
    def __init__(self, routes, airports):
        self.routes = routes
        self.airports = airports
        self.graph = Graph(airports)
        self.build_graph()

    def build_graph(self):
        """
        Build the directed graph using the provided routes.
        """
        for route in self.routes:
            self.graph.add_edge(route[0], route[1])

    def find_reachable_airports(self, start_airport):
        """
        Find all reachable airports using Kosaraju's Algorithm:
        1. Find Strongly Connected Components (SCCs).
        2. Compress the graph based on SCCs.
        3. Determine which SCCs have no incoming edges (in-degree = 0), excluding the start SCC.
        """
        kosaraju = KosarajuAlgorithm(self.graph)
        sccs = kosaraju.find_scc()

        # Step 2: Compress the graph using the SCCs (treat each SCC as a node)
        scc_map = {}
        for i, scc in enumerate(sccs):
            for node in scc:
                scc_map[node] = i

        compressed_graph = Graph(range(len(sccs)))
        for u, v in self.routes:
            u_scc = scc_map[u]
            v_scc = scc_map[v]
            if u_scc != v_scc:
                compressed_graph.add_edge(u_scc, v_scc)

        # Step 3: Calculate in-degree for each SCC in the compressed graph
        in_degrees = [0] * len(sccs)
        for u_scc in compressed_graph.graph:
            for v_scc in compressed_graph.graph[u_scc]:
                in_degrees[v_scc] += 1

        # Find SCCs with in-degree = 0
        zero_in_degree_sccs = []
        start_scc = scc_map[start_airport]
        for i in range(len(in_degrees)):
            if in_degrees[i] == 0 and i != start_scc:
                zero_in_degree_sccs.append(i)

        return zero_in_degree_sccs, sccs, scc_map

    def min_additional_routes(self, start_airport):
        """
        Calculate the minimum number of additional one-way routes needed to make
        all airports reachable from the starting airport.
        """
        zero_in_degree_sccs, sccs, scc_map = self.find_reachable_airports(start_airport)

        # We need one route to each SCC that has in-degree = 0
        num_additional_routes = len(zero_in_degree_sccs)

        # Convert SCC indices back to airport names for suggestions
        unreachable_airports = []
        for scc_index in zero_in_degree_sccs:
            unreachable_airports.append(sccs[scc_index][0])  # Pick one airport from the SCC

        return num_additional_routes, unreachable_airports