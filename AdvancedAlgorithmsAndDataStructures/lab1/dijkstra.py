import sys
from typing import Tuple, List

import networkx as nx
from networkx import DiGraph
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.use('TkAgg')


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
        node1, node2, weight = line.replace("\n", "").split(";")
        node1 = node1.replace(" ", "")
        node2 = node2.replace(" ", "")
        if node1 not in graph.nodes():
            graph.add_node(node1)
        if node2 not in graph.nodes():
            graph.add_node(node2)
        graph.add_weighted_edges_from([(node1, node2, float(weight))])
    return graph


def mark_as_unvidited(graph: DiGraph, start_node: int) -> Tuple[DiGraph, int]:
    """Function initializing nodes as unvisited

    Args:
        graph (DiGraph): Graph instance that will be mutated
        start_node (int): node label where search starts

    Returns:
        Tuple[DiGraph, int]: returns tuple with graph object and set marking unvisited nodes
    """
    nx.set_node_attributes(graph, False, 'visited')
    nx.set_node_attributes(graph, {str(start_node): True}, 'visited')
    unvisited = {node for node in graph.nodes()}
    return (graph, unvisited)


def set_initial_tenantive_distance(graph: DiGraph, start_node: int) -> None:
    """Function initializing tenantive distance on nodes

    Args:
        graph (DiGraph): Graph instance that will be mutated
        start_node (int): node label where search starts

    Returns:
        None: It returns None, however, mark that graph object has been mutated

    """
    nx.set_node_attributes(graph, float('inf'), 'tentative_distance')
    nx.set_node_attributes(graph, None, 'previous')
    nx.set_node_attributes(graph, False, 'current')
    nx.set_node_attributes(graph, {str(start_node): 0}, 'tentative_distance')
    nx.set_node_attributes(graph, {str(start_node): True}, 'current')


def draw_graph(graph: DiGraph) -> None:
    """Helper function for automagicaly drawing graph object

    Args:
        graph (DiGraph): Graph instance that will be mutated

    Returns:
        None
    """
    pos = nx.layout.spring_layout(graph)
    nx.draw_networkx_nodes(graph, pos)
    nx.draw_networkx_labels(graph, pos)
    nx.draw_networkx_edges(graph, pos, arrowstyle='->')
    nx.draw_networkx_edge_labels(graph, pos, alpha=0.5, font_size=9)
    plt.show()


def get_current_node(graph: DiGraph) -> str:
    """Helper function for finding node marked as current

    Args:
        graph (DiGraph): Graph instance being searched

    Returns:
        str: node label marked as current
    """
    return [node for node, value in graph.nodes(data='current') if value is True][0]


def not_visited(graph: DiGraph, node: int) -> bool:
    """Helper function for checking if node is unvisited

    Args:
        graph (DiGraph): Graph instance being searched
        node (int): node label being checked

    Returns:
        bool: True if not visited, False otherwise
    """
    return str(node) in [node for node, value in graph.nodes(data='visited') if value is False]


def get_shortest_path(graph: DiGraph, start_node: int, end_node: int) -> List[str]:
    """Function for finding shortest path in graph based on 'previous' attribute

    Args:
        graph (DiGraph): Graph instance being searched
        start_node (int): node label where search starts from
        end_node (int): node label where path ends with

    Returns:
        List[str]: list containing shortest path in the graph
    """
    path = []
    current = end_node
    while current != str(start_node):
        path.append(str(current))
        current = nx.get_node_attributes(graph, 'previous')[str(current)]
    return list(reversed(path + [str(start_node)]))


def dijkstra(graph: DiGraph, start_node: int, end_node: int) -> Tuple[float, List[str]]:
    """Function calculating shortest path in the graph with Dijkstra method

    Args:
        graph (DiGraph): Graph instance being searched
        start_node (int): node label where search starts from
        end_node (int): node label where path ends with

    Returns:
        Tuple[float, List[str]]: tuple containing shortest distance and path for that distance
    """
    unvisited_set = set(graph.nodes)
    mark_as_unvidited(graph, start_node)
    set_initial_tenantive_distance(graph, start_node)
    while unvisited_set:
        current = get_current_node(graph)
        current_distance = nx.get_node_attributes(graph, 'tentative_distance')[current]
        for node in [node for node in graph.neighbors(current) if not_visited(graph, node)]:
            prev_distance = nx.get_node_attributes(graph, 'tentative_distance')[node]
            weight = graph.edges[current, node]['weight']
            if current_distance + weight < prev_distance:
                nx.set_node_attributes(graph, {str(node): current_distance + weight}, 'tentative_distance')
                nx.set_node_attributes(graph, {str(node): current}, 'previous')
        nx.set_node_attributes(graph, {str(current): True}, 'visited')
        unvisited_set.remove(current)

        distances = [(node, nx.get_node_attributes(graph, 'tentative_distance')[node]) for node in unvisited_set]
        if not not_visited(graph, end_node) or min([dist for node, dist in distances]) is float('inf'):
            break
        else:
            next_node, _ = min(distances, key=lambda x: x[1])
            nx.set_node_attributes(graph, {str(next_node): True}, 'current')
            nx.set_node_attributes(graph, {str(current): False}, 'current')

    distance = nx.get_node_attributes(graph, 'tentative_distance')[str(end_node)]
    path = get_shortest_path(graph, start_node, end_node)

    return distance, path


graph_name = sys.argv[1]
start_node, end_node = int(sys.argv[2]), int(sys.argv[3])
graph = load_data(graph_name)

my_distance, my_path = dijkstra(graph, start_node, end_node)
lib_distance = nx.shortest_path_length(graph, source=str(start_node), target=str(end_node), weight='weight')
assert my_distance == lib_distance

lib_path = nx.dijkstra_path(graph, source=str(start_node), target=str(end_node), weight='weight')
assert my_path == lib_path

print(my_distance, my_path)
draw_graph(graph)
