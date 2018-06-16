import csv
from time import time
from collections import Counter
from random import uniform

from core.layer import Layer, InputLayer, OutputLayer
from core.network import Network, load_network, connect_om

LOAD_MLP_1 = True

# helper function
def connect(l1, n1, l2, n2):
    l1.neurons[n1].connect(l2.neurons[n2], 'right')

# define network
inputs = InputLayer([1, 1, 1, 1])
middle = Layer(5)
output = OutputLayer([1, 1, 1])


connect(inputs, 0, middle, 0)
connect(inputs, 0, middle, 1)
for n in range(1,4):
    [connect(inputs, n, middle, i) for i in range(n-1, n+2)]

for n in range(3):
    [connect(middle, i, output, n) for i in range(n, n+3)]

network = Network([inputs, middle, output])

# --------------

# load data
iris_map = {
    'Iris-setosa': [0, 0, 1],
    'Iris-versicolor': [0, 1, 0],
    'Iris-virginica': [1, 0, 0]
}

learning_data = []
with open('../data/training_data/iris.data', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        learning_data.append({
            'inputs': [float(x) for x in row[0:4]],
            'outputs': iris_map[row[4]]
        })

if LOAD_MLP_1:
    start_time = time()
    network1 = load_network('../data/trained_networks/mlp1.yaml')
    network2 = load_network('../data/trained_networks/mlp1.yaml')
    network3 = load_network('../data/trained_networks/mlp1.yaml')
    network4 = load_network('../data/trained_networks/mlp1.yaml')
    n12_connector = connect_om(network1, network2)
    n23_connector = connect_om(network2, network3)
    n34_connector = connect_om(network3, network4)

    k = 4
    i = 0
    while True:
        network1.learn_kfolds(k)
        n12_connector.pass_output([output.get_value() for output in network1.layers[-1].neurons])
        network2.learn_kfolds(k)
        n23_connector.pass_output([output.get_value() for output in network2.layers[-1].neurons])
        network3.learn_kfolds(k)
        n34_connector.pass_output([output.get_value() for output in network3.layers[-1].neurons])
        results = network4.learn_kfolds(k)

        scores = [(n, [round(x) for x in out] == check) for n, out, check in results]
        stuff = Counter(scores)
        folds = [stuff[(i, True)] / (stuff[(i,False)] + stuff[(i, True)]) * 100 for i in range(k)]
        print(folds)
        i = i + 1
        if i % 100 == 0:
            new_learning_rate = uniform(0.0, 1.0)
            for layer in network.layers:
                for neuron in layer.neurons:
                    neuron.learning_factor = new_learning_rate

        if all(fold > 90 for fold in folds):
            break

    end_time = time()
    print("start: %s, end %s, took %s", start_time, end_time, end_time - start_time)
    network1.dump_network('../data/trained_networks/deep_mlp1.yaml')
    network2.dump_network('../data/trained_networks/deep_mlp2.yaml')
    network3.dump_network('../data/trained_networks/deep_mlp3.yaml')
    network4.dump_network('../data/trained_networks/deep_mlp4.yaml')

else:
    network.load_learning_data(learning_data)
    network.normalize_learning_data()
    print("------- learn -------")
    network.print_data()

    # --------------

    # learn for 250 times
    network.learn(times=300)
    k = 4
    last_100 = []
    while True:
        results = network.learn_kfolds(k, times=1)
        scores = [(n, [round(x) for x in out] == check) for n, out, check in results]
        stuff = Counter(scores)
        folds = [stuff[(i, True)] / (stuff[(i,False)] + stuff[(i, True)]) * 100 for i in range(k)]
        last_100.append(folds)
        last_100 = last_100[-100:]
        if all(x == last_100[0] for x in last_100):
            new_learning_rate = uniform(0.0, 1.0)
            for layer in network.layers:
                for neuron in layer.neurons:
                    neuron.learning_factor = new_learning_rate

        print("folds results: ", folds)
        if all(fold > 70 for fold in folds):
            break


    network.dump_network('../data/trained_networks/mlp1.yaml', prompt=True)

