import networkx as nx
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.use('TkAgg')


def load_data(filename):
    graph = nx.DiGraph()
    lines = open(filename, 'r').readlines()
    for line in lines:
        node1, node2, weight = line.replace("\n", "").split(";")
        node1 = node1.replace(" ", "")
        node2 = node2.replace(" ", "")
        if node1 not in graph.nodes():
            graph.add_node(node1)
        if node2 not in graph.nodes():
            graph.add_node(node2)
        graph.add_weighted_edges_from([(node1, node2, float(weight))])
    return graph


def mark_as_unvidited(graph):
    nx.set_node_attributes(graph, 'visited', False)
    unvisited = {node for node in graph.nodes()}
    return (graph, unvisited)


def set_initial_tenantive_distance(graph, start_node):
    nx.set_node_attributes(graph, float('inf'), 'tentative_distance')
    nx.set_node_attributes(graph, False, 'current')
    nx.set_node_attributes(graph, {start_node: 0}, 'tentative_distance')
    nx.set_node_attributes(graph, {start_node: True}, 'current')


def draw_graph(graph):
    pos = nx.layout.spring_layout(graph)
    nx.draw_networkx_nodes(graph, pos)
    nx.draw_networkx_labels(graph, pos)
    nx.draw_networkx_edges(graph, pos, arrowstyle='->')
    nx.draw_networkx_edge_labels(graph, pos, alpha=0.5, font_size=9)
    plt.show()


# graph = load_data("graf.txt")
graph = load_data("test_graph.txt")

mark_as_unvidited(graph)
set_initial_tenantive_distance(graph, '1')

draw_graph(graph)
