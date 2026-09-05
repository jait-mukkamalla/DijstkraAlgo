from typing import Dict, List, Set, Tuple
import networkx as nx
from graph import Graph, construct_path

def compute_graph_layout(
        custom_graph: Graph, start_node: str, end_node: str
) -> Tuple[nx.Graph, Dict[str, Tuple[float, float]], List[str], Set[Tuple[str, str]]]:
    """ Take a custom graph input, run Dijkstra's, and get 2D coordinates using NetworkX """
    # Build NetworkX graph from custom_graph's edges
    nx_graph = nx.Graph()
    for u, v, weight in custom_graph.get_edges():
        nx_graph.add_edge(u, v, weight=weight)

    # Run Dijkstra's and construct the shortest path
    _, previous = custom_graph.dijkstra(start_node)
    shortest_path = construct_path(previous, start_node, end_node)

    # Convert the shortest path list into a set of edge tuples for O(1) lookup
    path_edges = set(zip(shortest_path[:-1], shortest_path[1:]))

    # Calculate 2D coordinates using NetworkX layout
    pos: Dict[str, Tuple[float, float]] = nx.spring_layout(nx_graph, seed=42)

    return nx_graph, pos, shortest_path, path_edges
