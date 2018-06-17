0.5::edge(mall,gasStation).
0.7::edge(gasStation,nearCar).
0.4::edge(gasStation,farCar).
0.5::edge(nearCar,farCar).
0.3::edge(nearCar,workingCar).
0.7::edge(farCar,workingCar).
0.8::edge(workingCar,highway).

0.6::edge(mall,radio).
0.4::edge(radio,roof).
0.2::edge(roof,helicopter).
0.99::edge(helicopter,military).

path(A,B) :- edge(A,B).
% there is a indirect path between the nodes, if there is an intermediate node
% that can be reached directly from the first node, and from which you can reach the second node
path(A,C) :- edge(A,B),
             B \= C,
             path(B,C).
query(path(mall,highway)).
query(path(mall,military)).