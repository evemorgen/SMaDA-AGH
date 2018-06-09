import csv
from pprint import pprint

from layer import Layer, InputLayer, OutputLayer
from network import Network

learning_data = []

tic_tac_map = {
    'positive': 1,
    'negative': 0,
    'x': 1,
    'o': 2,
    'b': 3
}

with open('data/training_data/tic-tac-toe.data', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        learning_data.append({
            'inputs': [tic_tac_map[x] for x in row[0:9]],
            'outputs': [tic_tac_map[row[9]]]
        })


inputs = InputLayer([1] * 9)
middle = Layer(5)
middle2 = Layer(7)
middle3 = Layer(5)
middle4 = Layer(2)
output = OutputLayer([1])

network = Network([
    inputs,
    middle,
    middle2,
#    middle3,
#    middle4,
    output
])

network.connect()

network.load_learning_data(learning_data)
print("------- learn -------")
network.print_data()

network.learn(times=30)

i = [
    [tic_tac_map[x] for x in ['x', 'x', 'x', 'o', 'b', 'x', 'b', 'o', 'o']],  # positive
    [tic_tac_map[x] for x in ['x', 'o', 'o', 'x', 'x', 'o', 'b', 'x', 'o']]  # negative
]
o = [network.test(io) for io in i]

network.print_io(i, o, output_names=['positive/negative'])

print("------ weights -----")
network.print_weights()

network.dump_network('data/trained_networks/tictactoe.yaml', prompt=True)