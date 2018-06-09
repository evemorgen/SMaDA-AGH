import yaml

from layer import Layer, InputLayer, OutputLayer
from network import Network

inputs = InputLayer([1, 1])
middle = Layer(2)
middle2 = Layer(2)
output = OutputLayer([1])

network = Network([inputs, middle, middle2, output])
network.connect()

learning_data = [
    {"inputs": [0, 0], "outputs": [0]},
    {"inputs": [0, 1], "outputs": [1]},
    {"inputs": [1, 1], "outputs": [0]},
    {"inputs": [1, 0], "outputs": [1]}
]

network.load_learning_data(learning_data)
print("------- learn -------")
network.print_data()

network.learn(times=10000)


i = [[0, 0], [0, 1], [1, 1], [1, 0]]
o = [network.test(io) for io in i]


print("------- test -------")
network.print_io(i, o)

print("------ weights -----")
network.print_weights()

network.dump_network('data/trained_networks/xor-dump2.yaml', prompt=True)
