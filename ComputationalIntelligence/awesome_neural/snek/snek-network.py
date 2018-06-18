import yaml
from collections import Counter
from pprint import pprint
from random import uniform
from time import time

from core.layer import Layer, InputLayer, OutputLayer
from core.network import Network


with open('snek-learning.yaml', 'r') as file:
    data = yaml.load(file)
    #data = data[:1000]

learning_data = [{'inputs': list(row[:5]), 'outputs': [row[5]]} for row in data]


inputs = InputLayer([1, 1, 1, 1, 1])
middle = Layer(5)
middle3 = Layer(3)
output = OutputLayer([1])

network = Network([inputs, middle, middle3, output], 'snek')
network.connect()
network.load_learning_data(learning_data)

network.print_data()
folds = 4
result = [0]
i = 0
start_time = time()
while sum(result) / folds < 90:
    results = network.learn_kfolds(folds, times=1)
    scores = [(n, [round(x) for x in out] == check) for n, out, check in results]
    stuff = Counter(scores)
    result = [stuff[(i, True)] / (stuff[(i, False)] + stuff[(i, True)]) * 100 for i in range(folds)]
    print("folds results: ", result)
    i += 1
    if i % 10 == 0:
        print("saving dump")
        network.dump_network('snek-play-7-new1.yaml')
        new_learning_rate = uniform(0.0, 1.0)
        for layer in network.layers:
            for neuron in layer.neurons:
                neuron.learning_factor = new_learning_rate
    print("learning for: %s" % (time() - start_time))

end_time = time()
print("learning time: %s" % (end_time - start_time))

try:
    network.dump_cypher('snek2.cypher')
except:
    pass

network.dump_network('snek-play-awesome.yaml')