# Create Graph class to represent an unweighted, bidirectional graph data structure
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
