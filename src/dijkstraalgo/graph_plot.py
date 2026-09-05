# graph_plot.py
import plotly.graph_objects as go
from coordinates import compute_graph_layout
from graph import Graph


def plot_shortest_path(
    custom_graph: Graph, source: str, target: str
) -> None:
    # Get layout data from coordinates.py
    nx_graph, pos, shortest_path, path_edges = compute_graph_layout(custom_graph, source, target)

    # 1. Separate standard edges vs path edges
    edge_x, edge_y = [], []
    path_x, path_y = [], []

    for u, v in nx_graph.edges():
        x0, y0 = pos[u]
        x1, y1 = pos[v]

        if (u, v) in path_edges or (v, u) in path_edges:
            path_x.extend([x0, x1, None])
            path_y.extend([y0, y1, None])
        else:
            edge_x.extend([x0, x1, None])
            edge_y.extend([y0, y1, None])

    # Standard Edge Trace
    edge_trace = go.Scatter(
        x=edge_x,
        y=edge_y,
        line=dict(width=2, color="#aaa"),
        hoverinfo="none",
        mode="lines",
    )

    # Highlighted Path Trace
    path_trace = go.Scatter(
        x=path_x,
        y=path_y,
        line=dict(width=5, color="#e74c3c"),
        hoverinfo="none",
        mode="lines",
    )

    # 2. Node Trace
    node_x = [pos[node][0] for node in nx_graph.nodes()]
    node_y = [pos[node][1] for node in nx_graph.nodes()]

    node_colors = [
        "#e74c3c" if node in shortest_path else "#3498db"
        for node in nx_graph.nodes()
    ]

    node_trace = go.Scatter(
        x=node_x,
        y=node_y,
        mode="markers+text",
        text=list(nx_graph.nodes()),
        textposition="top center",
        hoverinfo="text",
        marker=dict(size=20, color=node_colors, line_width=2),
    )

    # 3. Assemble Plotly Figure
    fig = go.Figure(
        data=[edge_trace, path_trace, node_trace],
        layout=go.Layout(
            title=f"Dijkstra Shortest Path ({source} -> {target}): {' -> '.join(shortest_path)}",
            showlegend=False,
            hovermode="closest",
            margin=dict(b=20, l=5, r=5, t=40),
            xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
            yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        ),
    )

    fig.show()


if __name__ == "__main__":
    # Create sample graph
    g = Graph()
    g.add_edge("A", "B", 4)
    g.add_edge("A", "C", 2)
    g.add_edge("B", "C", 1)
    g.add_edge("B", "D", 5)
    g.add_edge("C", "D", 8)
    g.add_edge("C", "E", 10)
    g.add_edge("D", "E", 2)

    # Render interactive Plotly graph
    plot_shortest_path(g, source="A", target="E")