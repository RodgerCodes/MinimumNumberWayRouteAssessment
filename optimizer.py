from graph import DirectedGraph
from collections import defaultdict
from kosajaru_algo import KosarajuSCC

class FlightRoutesOptimizer:
    def __init__(self, routes, airports):
        """Initialize the optimizer with routes and airports."""
        self.routes = routes
        self.airports = airports
        self.graph = DirectedGraph()
        self.build_graph()

    def build_graph(self):
        """Build the directed graph with the provided routes."""
        for src, dst in self.routes:
            self.graph.add_edge(src, dst)

    def build_component_graph(self, components):
        """Build a graph where each node represents an SCC."""
        # Create mapping of airport to component ID
        airport_to_component = {}
        for i, component in enumerate(components):
            for airport in component:
                airport_to_component[airport] = i

        # Build component graph
        component_graph = defaultdict(set)
        for src in self.graph.graph:
            src_component = airport_to_component[src]
            for dst in self.graph.graph[src]:
                dst_component = airport_to_component[dst]
                if src_component != dst_component:
                    component_graph[src_component].add(dst_component)

        return dict(component_graph), airport_to_component

    def min_additional_routes(self, start_airport):
        """Calculate minimum number of additional routes needed."""
        # Find SCCs
        scc_finder = KosarajuSCC(self.graph.graph, self.airports)
        components = scc_finder.kosaraju_scc()

        # If only one component, all airports are already reachable
        if len(components) == 1:
            return 0

        # Build component graph
        component_graph, airport_to_component = self.build_component_graph(components)

        # Find start component
        start_component = airport_to_component[start_airport]

        # Calculate in-degrees for each component
        in_degrees = defaultdict(int)
        for src in component_graph:
            for dst in component_graph[src]:
                in_degrees[dst] += 1

        # Count components with in-degree = 0 (excluding the start component)
        zero_in_degree_count = 0
        for component_id in range(len(components)):
            if component_id != start_component and in_degrees[component_id] == 0:
                zero_in_degree_count += 1

        return zero_in_degree_count
