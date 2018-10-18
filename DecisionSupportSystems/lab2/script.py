import pygraphviz as pgv

from opyenxes.data_in.XUniversalParser import XUniversalParser

path = 'repairexample.xes'

# open file within context manager
with open(path) as log_file:
    # parse the log
    log = XUniversalParser().parse(log_file)[0]

    event = log[0][0]

    # parse worklog
    workflow_log = []
    for trace in log:
        workflow_trace = []
        for event in trace[0::2]:
            # get the event name from the event in the log
            event_name = event.get_attributes()['Activity'].get_value()
            workflow_trace.append(event_name)
        workflow_log.append(workflow_trace)

    # transofrm workflow_log to list of lists containing tasks
    w_net = dict()
    for w_trace in workflow_log:
        for i in range(0, len(w_trace) - 1):
            ev_i, ev_j = w_trace[i], w_trace[i + 1]
            if ev_i not in w_net.keys():
                w_net[ev_i] = set()
            w_net[ev_i].add(ev_j)

    # count events
    ev_counter = dict()
    for w_trace in workflow_log:
        for ev in w_trace:
            ev_counter[ev] = ev_counter.get(ev, 0) + 1

    # count edges occurance
    edge_count = dict()
    for w_trace in workflow_log:
        for i in range(0, len(w_trace) - 1):
            edge_tuple = (w_trace[i], w_trace[i + 1])
            edge_count[edge_tuple] = edge_count.get(edge_tuple, 0) + 1

    # scale edges from 0 to 5
    edge_max = max(edge_count.values())
    for edge in edge_count:
        edge_count[edge] = edge_count[edge] * 5 / edge_max

    # calculate color shades
    color_min = min(ev_counter.values())
    color_max = max(ev_counter.values())

    # draw graph with calculated values
    G = pgv.AGraph(strict=False, directed=True)
    G.graph_attr['rankdir'] = 'LR'
    G.node_attr['shape'] = 'Mrecord'
    for event in w_net:
        value = ev_counter[event]
        color = int(float(color_max - value) / float(color_max - color_min) * 100.00)
        my_color = "#ff9933" + str(hex(color))[2:]
        text = event + ' (' + str(ev_counter[event]) + ")"
        G.add_node(event, label=text, style="rounded,filled", fillcolor=my_color)
        for preceding in w_net[event]:
            G.add_edge(
                event, preceding, penwidth=edge_count[(event, preceding)],
                label=edge_count[(event, preceding)] * edge_max / 5)

    G.draw('simple_heuristic_net.png', prog='dot')
