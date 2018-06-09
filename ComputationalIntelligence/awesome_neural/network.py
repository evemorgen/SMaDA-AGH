import yaml
from time import time
from distutils.dist import strtobool

from texttable import Texttable

from layer import OutputLayer
from utils import constants



def load_network(filename):
    with open(filename, 'r') as file:
        network = yaml.load(file, yaml.Loader)
    return network


class Network:
    def __init__(self, layers):
        self.layers = layers
        self.data = None
        self.constants = constants

    def connect(self):
        for idx in range(len(self.layers) - 1):
            self.layers[idx].connect_layer(self.layers[idx + 1], 'right')

    def load_learning_data(self, data):
        self.data = data

    def print_data(self):
        self.print_io(
            [input['inputs'] for input in self.data],
            [output['outputs'] for output in self.data]
        )

    def print_io(self, inputs, outputs, input_names=None, output_names=None):
        number_of_columns = len(inputs[0]) + len(outputs[0])
        table = Texttable()
        table.set_cols_align(["l" for _ in range(number_of_columns)])
        table.set_cols_valign(["m" for _ in range(number_of_columns)])
        input_names = input_names or ["In%s" % n for n in range(len(inputs[0]))]
        output_names = output_names or ["Out%s" % n for n in range(len(outputs[0]))]
        table.add_row(input_names + output_names)
        for i, o in zip(inputs, outputs):
            table.add_row(i + o)

        print(table.draw())

    def print_weights(self):
        for layer in self.layers[:-1]:
            for neuron in layer.neurons:
                for output in neuron.outputs:
                    print(output)

    def stimulate(self):
        for layer in self.layers[:-1]:
            layer.stimulate_next()

    def backpropagate(self, online=False):
        for layer in list(reversed(self.layers))[:-1]:
            if isinstance(layer, OutputLayer):
                layer.calculate_delta()
            layer.stimulate_delta()
            if online:
                layer.calculate_weight()
        if not online:
            for layer in list(reversed(self.layers))[:-1]:
                layer.calculate_weight()

    def next_dataset(self, inputs, outputs):
        self.layers[0].set_input(inputs)
        self.layers[-1].set_output(outputs)

    def learn(self, times=1):
        start_time = time()
        for n in range(times):
            for data in self.data:
                self.next_dataset(data['inputs'], data['outputs'])
                self.stimulate()
                self.backpropagate()
            if n % (times/10) == 0:
                print("done course no #{} in {}s".format(n, time() - start_time))

    def test(self, input):
        self.next_dataset(input, [])
        self.stimulate()
        return [output.get_value() for output in self.layers[-1].neurons]

    def dump_network(self, filename, prompt=False):
        if prompt and not strtobool(input("Do you want to save network? [y/n]\n")):
            return
        with open(filename, 'w') as file:
            yaml.dump(
                self,
                file,
                width=80,
                default_flow_style=False
            )

