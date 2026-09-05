import heapq
from typing import Dict, List, Tuple, Optional

# Create Graph class to represent a weighted, bidirectional graph data structure
class Graph:
    def __init__(self):
        # Use an adjacency list to store (node, weight) tuples representing connections between nodes
        self.adj_list: Dict[str, List[Tuple[str, float]]] = {}

    def add_node(self, u: str, v: str, weight: float) -> None:
        """ Adds an undirected, weighted edge between node u and node v to the adjacency list """
        # Initialize an empty list for a new node getting added to the adjacency list
        if u not in self.adj_list:
            self.adj_list[u] = []
        if v not in self.adj_list:
            self.adj_list[v] = []

        # Add bidirectional edges because we are choosing to have an undirected graph
        self.adj_list[u].append((v, float(weight)))
        self.adj_list[v].append((u, float(weight)))

    def dijkstra(self, start_node: str) -> Tuple[Dict[str, float], Dict[str, Optional[str]]]:
        """ Find the shortest path from the start_node to every other node in the graph """
        # Track distances and previous nodes for use in `construct_path()`
        distances: Dict[str, float] = {node : float('inf') for node in self.adj_list}
        previous: Dict[str, Optional[str]]  = {node: None for node in self.adj_list}
        distances[start_node] = 0.0

        # Create min-heap to store (distance, node) tuples [distance is first because we sort using them in min-heap]
        priority_queue: List[Tuple[float, str]] = [(0.0, start_node)]

        while priority_queue:
            cur_distance, cur_node = heapq.heappop(priority_queue)  # Get current distance, current node from min heap

            if cur_distance > distances[cur_node]:  # Skip processing if we already have a shorter path for the cur_node
                continue

            # Explore the neighboring nodes
            for neighbor, weight in self.adj_list[cur_node]:
                distance = cur_distance + weight

                # IF we find a shorter path, update tracker dicts and min-heap
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous[neighbor] = cur_node
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances, previous

def construct_path(previous: Dict[str, Optional[str]], start_node: str, end_node: str) -> List[str]:
    """ Build the shortest path from start_node to end_node by traversing the 'previous' dict in reverse """
    path: List[str] = []
    curr: Optional[str] = end_node

    while curr:
        path.append(curr)
        curr = previous.get(curr)

    path.reverse()
    return path if (path and path[0] == start_node) else []
