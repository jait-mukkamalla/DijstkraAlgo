import heapq

# Create Graph class to represent a weighted, bidirectional graph data structure
class Graph:
    def __init__(self):
        # Use an adjacency list to store (node, weight) tuples representing connections between nodes
        self.adj_list = {}

    def add_node(self, u: str, v: str, weight: int) -> None:
        """ Adds an undirected, weighted edge between node u and node v to the adjacency list """
        # Initialize an empty list for a new node getting added to the adjacency list
        if u not in self.adj_list:
            self.adj_list[u] = []
        if v not in self.adj_list:
            self.adj_list[v] = []

        # Add bidirectional edges because we are choosing to have an undirected graph
        self.adj_list[u].append((v, weight))
        self.adj_list[v].append((u, weight))

    def dijkstra(self, start_node: str) -> tuple[dict, dict]:
        """ Find the shortest path from the start_node to every other node in the graph """
        pass

    def construct_path(self, previous: list[str], start_node: str, end_node: str) -> dict:
        """ Build the shortest path from start_node to end_node that was given by dijkstra's algorithm """
        pass
