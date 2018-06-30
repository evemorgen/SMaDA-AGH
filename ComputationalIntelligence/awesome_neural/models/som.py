import csv
from collections import Counter
from core.layer import Layer, InputLayer, OutputLayer
from core.network import Network
from models.som_np import load_som, best_match


class InputSom(InputLayer):
    def __init__(self, values, map):
        super().__init__(values, name='InputSom')
        self.map = map

    def set_input(self, input):
        for n, v in zip(self.neurons, best_match(self.map, input)):
            n.update_value(v)

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

map = load_som("../data/trained_networks/som.yaml")
inputs = InputLayer([1, 1, 1, 1], name='NormalInput')
inputs_som = InputSom([1, 1, 1, 1], map)
inputs_som.set_network_name('som')
middle = Layer(3)
output = OutputLayer([1, 1, 1])

network = Network([inputs, middle, output], 'som')
network.connect()
network.load_learning_data(learning_data)
middle.connect_layer(inputs_som, 'left')
network.dump_cypher('../data/cypher/som.cypher', additional_neurons=inputs_som.neurons)
"""
#network.learn(times=5000) #input_layers=[inputs_som])
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
"""