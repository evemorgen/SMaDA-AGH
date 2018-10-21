import sys

import networkx as nx
import matplotlib.pyplot as plt
from networkx import DiGraph


def load_data(filename: str) -> DiGraph:
    """Function for loading graph data from specified file

    Args:
        filename (str): filename where graph data is located

    Returns:
        DiGraph: It returns ready to go DiGraph instance
    """
    graph = DiGraph()
    lines = open(filename, 'r').readlines()
    for line in lines:
        node1, node2, weight, _ = line.replace("\n", "").split("\t")
        node1 = node1.replace(" ", "")
        node2 = node2.replace(" ", "")
        if node1 not in graph.nodes():
            graph.add_node(node1)
        if node2 not in graph.nodes():
            graph.add_node(node2)
        graph.add_weighted_edges_from([(node1, node2, float(weight))], weight='capacity')
    return graph


def draw_graph(graph: DiGraph) -> None:
    """Helper function for automagicaly drawing graph object

    Args:
        graph (DiGraph): Graph instance that will be mutated

    Returns:
        None
    """
    plt.figure(figsize=(40, 28))
    pos = nx.nx_agraph.graphviz_layout(graph)
    nx.draw(graph, pos=pos, node_size=1200, node_color='lightblue',
            linewidths=0.25, font_size=10, font_weight='bold', with_labels=True, dpi=1000)

    plt.show()


def ford_fulkerson(graph: DiGraph, s: str, t: str) -> float:
    """Function computing maximum flow using Ford–Fulkerson method

    Args:
        graph (DiGraph): Graph instance
        s (str): start node
        t (str): end node

    Returns:
        float: maximum flow calculated
    """
    flow = 0.0

    while True:
        try:
            path_nodes = nx.bidirectional_shortest_path(graph, s, t)
        except nx.NetworkXNoPath:
            break

        path_edges = list(zip(path_nodes[:-1], path_nodes[1:]))

        path_capacity = min([graph[u][v]['capacity'] for u, v in path_edges if 'capacity' in graph[u][v]])
        flow += path_capacity

        for u, v in path_edges:
            edge_attr = graph[u][v]
            edge_attr['capacity'] -= path_capacity
            if edge_attr['capacity'] == 0:
                graph.remove_edge(u, v)

            if graph.has_edge(v, u):
                if 'capacity' in graph[v][u]:
                    graph[v][u]['capacity'] += path_capacity
            else:
                graph.add_edge(v, u, capacity=path_capacity)

    return flow


graph_name = sys.argv[1]
source, sink = sys.argv[2], sys.argv[3]
graph = load_data(graph_name)

# draw_graph(graph)

f_value1, _ = nx.maximum_flow(graph, source, sink)
f_value2 = ford_fulkerson(graph, source, sink)

assert -0.01 < f_value1 - f_value2 < 0.01
print(f"{f_value2}:{source}:{sink}")
