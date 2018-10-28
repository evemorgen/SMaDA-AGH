import graphviz


class MyGraph(graphviz.Digraph):

    def __init__(self, *args):
        super(MyGraph, self).__init__(*args)
        self.graph_attr['rankdir'] = 'LR'
        self.node_attr['shape'] = 'Mrecord'
        self.graph_attr['splines'] = 'ortho'
        self.graph_attr['nodesep'] = '0.8'
        self.edge_attr.update(penwidth='2')

    def add_event(self, name):
        super(MyGraph, self).node(name, shape="circle", label="")

    def add_and_gateway(self, *args):
        super(MyGraph, self).node(*args, shape="diamond",
                                  width=".6", height=".6",
                                  fixedsize="true",
                                  fontsize="40", label="+")

    def add_xor_gateway(self, *args, **kwargs):
        super(MyGraph, self).node(*args, shape="diamond",
                                  width=".6", height=".6",
                                  fixedsize="true",
                                  fontsize="35", label="×")

    def add_and_split_gateway(self, source, targets, *args):
        gateway = 'ANDs ' + str(source) + '->' + str(targets)
        self.add_and_gateway(gateway, *args)
        super(MyGraph, self).edge(source, gateway)
        for target in targets:
            super(MyGraph, self).edge(gateway, target)

    def add_xor_split_gateway(self, source, targets, *args):
        gateway = 'XORs ' + str(source) + '->' + str(targets)
        self.add_xor_gateway(gateway, *args)
        super(MyGraph, self).edge(source, gateway)
        for target in targets:
            super(MyGraph, self).edge(gateway, target)

    def add_and_merge_gateway(self, sources, target, *args):
        gateway = 'ANDm ' + str(sources) + '->' + str(target)
        self.add_and_gateway(gateway, *args)
        super(MyGraph, self).edge(gateway, target)
        for source in sources:
            super(MyGraph, self).edge(source, gateway)

    def add_xor_merge_gateway(self, sources, target, *args):
        gateway = 'XORm ' + str(sources) + '->' + str(target)
        self.add_xor_gateway(gateway, *args)
        super(MyGraph, self).edge(gateway, target)
        for source in sources:
            super(MyGraph, self).edge(source, gateway)

"""
direct_succession = {
    'a': {'b', 'c'},
    'b': {'c', 'd'},
    'c': {'b', 'd'},
    'd': {'e', 'f'},
    'e': {'g'},
    'f': {'g'}
}

causality = {
    'a': {'b', 'c'},
    'b': {'d'},
    'c': {'d'},
    'd': {'e', 'f'},
    'e': {'g'},
    'f': {'g'}
}

parallel_events = {('b', 'c'), ('c', 'b')}
"""

direct_succession = {
    'a': {'b', 'f'},
    'b': {'c', 'd'},
    'c': {'d', 'e'},
    'd': {'c', 'e'},
    'e': {'h'},
    'f': {'g'},
    'g': {'h'},
    'h': {'i', 'j'},
    'i': {'k'},
    'j': {'k'}
}

casuality = {key: set([succ for succ in direct_succession[key] if key not in direct_succession.get(succ, set())]) for key in direct_succession}
parallel_events = {(key, another) for key in direct_succession for another in direct_succession[key] if key not in direct_succession.get(another, set())}

#print(sum(list(direct_succession.values())))
final_set = set()

for s in direct_succession.values():
    final_set |= s

print(final_set)

start_set_events = {'a'}
end_set_events = {'g'}
inv_causality = {
    'd': {'b', 'c'},
    'g': {'e', 'f'}
}


G = MyGraph()

# adding split gateways based on causality
for event in causality:
    if len(causality[event]) > 1:
        if tuple(causality[event]) in parallel_events:
            G.add_and_split_gateway(event, causality[event])
        else:
            G.add_xor_split_gateway(event, causality[event])

# adding merge gateways based on inverted causality
for event in inv_causality:
    if len(inv_causality[event]) > 1:
        if tuple(inv_causality[event]) in parallel_events:
            G.add_and_merge_gateway(inv_causality[event], event)
        else:
            G.add_xor_merge_gateway(inv_causality[event], event)
    elif len(inv_causality[event]) == 1:
        source = list(inv_causality[event])[0]
        G.edge(source, event)

# adding start event
G.add_event("start")
if len(start_set_events) > 1:
    if tuple(start_set_events) in parallel_events:
        G.add_and_split_gateway(event, start_set_events)
    else:
        G.add_xor_split_gateway(event, start_set_events)
else:
    G.edge("start", list(start_set_events)[0])

# adding end event
G.add_event("end")
if len(end_set_events) > 1:
    if tuple(end_set_events) in parallel_events:
        G.add_and_merge_gateway(end_set_events, event)
    else:
        G.add_xor_merge_gateway(end_set_events, event)
else:
    G.edge(list(end_set_events)[0], "end")


G.render('simple_graphviz_graph')
G.view('simple_graphviz_graph')
