from random import choice
from gvanim import Animation, gif, render
from opyenxes.data_in.XUniversalParser import XUniversalParser

path = 'repairexample.xes'

colors = [line.replace("\n", "") for line in open('colors.txt').readlines()]

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

    # draw graph with calculated values
    ga = Animation()
    for event in w_net:
        text = event + ' (' + str(ev_counter[event]) + ")"
        ga.label_node(event, text)
        for preceding in w_net[event]:
            ga.add_edge(event, preceding)

    ga.next_step()
    a = 0
    for w_trace in workflow_log:
        color = choice(colors)
        for i in range(0, len(w_trace) - 1):
#            cols = [choice(colors) for _ in range(len(w_trace))]
            for j in range(0, i+1):
                ga.highlight_node(w_trace[j], color=color)
                ga.highlight_edge(w_trace[j], w_trace[j + 1], color=color)
            ga.next_step()
        a += 1
        print(a)
        if a > 30:
            break

    graphs = ga.graphs()
    files = render(graphs, 'dfv', 'png', size=640)
    gif(files, 'dfv', 10)
