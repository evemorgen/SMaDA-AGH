import yaml
from time import time
from distutils.dist import strtobool

from texttable import Texttable

from core.layer import OutputLayer, BiasLayer
from core.neuron import BiasNeuron
from core.utils import constants

def connect_om(n1, n2):
    b1 = BiasLayer([BiasNeuron(n1.layers[-1].neurons[i].get_value()) for i in range(len(n1.layers[-1].neurons))])
    for bias in b1.neurons:
        for neuron in n2.layers[1].neurons:
            neuron.connect(bias, 'left')
    return b1

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

    def normalize_learning_data(self):
        stats = []
        new_data = []
        for i in range(len(self.data[0]['inputs'])):
            data = [x['inputs'][i] for x in self.data]
            stats.append({'min': min(data), 'max': max(data)})
        for features in self.data:
            new_inputs = []
            for i in range(len(features['inputs'])):
                new_inputs.append(
                    (features['inputs'][i] - stats[i]['min'])/(stats[i]['max'] - stats[i]['min'])
                )
            new_data.append({
                'inputs': new_inputs,
                'outputs': features['outputs']
            })
        self.data = new_data
        self.constants['normalised'] = True

    def print_data(self):
        self.print_io(
            [input['inputs'] for input in self.data],
            [output['outputs'] for output in self.data]
        )

    def print_io(self, inputs, outputs, input_names=None, output_names=None):
        input_names = input_names or ["In%s" % n for n in range(len(inputs[0]))]
        output_names = output_names or ["Out%s" % n for n in range(len(outputs[0]))]
        number_of_columns = len(inputs[0]) + len(outputs[0])
        table = Texttable()
        table.set_cols_align(["l" for _ in range(number_of_columns)])
        table.set_cols_valign(["m" for _ in range(number_of_columns)])
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

    def learn_kfolds(self, k, times=1):
        all = []
        start_time = time()
        for n in range(times):
            for i in range(k):
                sector_len = round(len(self.data) / k)
                test_data = [x for x in self.data[i*sector_len:(i+1)*sector_len]]
                train_data = [x for x in self.data[0:i*sector_len] + self.data[(i+i)*sector_len:]]
                for data in train_data:
                    self.next_dataset(data['inputs'], data['outputs'])
                    self.stimulate()
                    self.backpropagate()

                results = [(i, self.test(test['inputs']), test['outputs']) for test in test_data]
                all += results
#            if n % (times/10) == 0:
#                print("done course no #{} in {}s".format(n, time() - start_time))
        return all

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

