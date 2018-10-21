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
        graph.add_weighted_edges_from([(node1, node2, float(weight))])
    return graph


def draw_graph(graph: DiGraph) -> None:
    """Helper function for automagicaly drawing graph object

    Args:
        graph (DiGraph): Graph instance that will be mutated

    Returns:
        None
    """
    plt.figure(figsize=(40, 28))
    #pos = nx.spring_layout(graph, scale=1000)
    pos = nx.nx_agraph.graphviz_layout(graph)
    nx.draw(graph, pos=pos, node_size=1200, node_color='lightblue',
            linewidths=0.25, font_size=10, font_weight='bold', with_labels=True, dpi=1000)

    """
    nx.draw_networkx_nodes(graph, pos)
    nx.draw_networkx_labels(graph, pos)
    nx.draw_networkx_edges(graph, pos, arrowstyle='->')
    nx.draw_networkx_edge_labels(graph, pos, alpha=0.5, font_size=9)
    """
    plt.show()


def set_initial_flow(graph: DiGraph) -> None:
    """Function initializing flow parameter on all edges

    Args:
        graph (DiGraph): Graph instance that will be mutated

    Returns:
        None: It returns None, however, mark that graph object has been mutated

    """
    nx.set_edge_attributes(graph, 0, 'flow')

def ff(graph: DiGraph) -> int:
    """Function computing maximum flow using Ford–Fulkerson method

    Args:
        graph (DiGraph): Graph instance

    Returns:
        int: maximum flow calculated
    """


graph_name = sys.argv[1]
source, sink = int(sys.argv[2]), int(sys.argv[3])
graph = load_data(graph_name)

draw_graph(graph)
