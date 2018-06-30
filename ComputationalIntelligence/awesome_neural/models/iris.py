import csv
from collections import Counter

from core.layer import Layer, InputLayer, OutputLayer
from core.network import Network


iris_map = {
    'Iris-setosa': [0, 0, 1],
    'Iris-versicolor': [0, 1, 0],
    'Iris-virginica': [1, 0, 0]
}

learning_data = []

with open('data/training_data/iris.data', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        learning_data.append({
            'inputs': [float(x) for x in row[0:4]],
            'outputs': iris_map[row[4]]
        })

inputs = InputLayer([1, 1, 1, 1])
middle = Layer(5)
middle2 = Layer(3)
output = OutputLayer([1, 1, 1])

network = Network([inputs, middle, middle2, output])
network.connect()

network.load_learning_data(learning_data)
network.normalize_learning_data()
print("------- learn -------")
network.print_data()

#network.learn(times=1000)
folds = 4
results = network.learn_kfolds(folds, times=1000)
scores = [(n, [round(x) for x in out] == check) for n, out, check in results]
stuff = Counter(scores)
print("folds results: ", [stuff[(i, True)] / (stuff[(i,False)] + stuff[(i, True)]) * 100 for i in range(folds)])

i = [
    [6.9, 3.1, 5.1, 2.3],  # Iris-virginica
    [5.0, 2.0, 3.5, 1.0],  # Iris-versicolor
    [5.4, 3.7, 1.5, 0.2]   # Iris-setosa
]
o = [network.test(io) for io in i]
network.print_io(i, o, output_names=['Iris-virginica', 'Iris-versicolor', 'Iris-setosa'])

network.dump_network('data/trained_networks/iris.yaml', prompt=True)