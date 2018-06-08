from texttable import Texttable

from layer import OutputLayer


class Network:
    def __init__(self, layers):
        self.layers = layers
        self.data = None

    def connect(self):
        for idx in range(len(self.layers) - 1):
            self.layers[idx].connect_layer(self.layers[idx + 1], 'right')

    def load_learning_data(self, data):
        self.data = data

    def print_data(self):
        table = Texttable()
        table.set_cols_align(["l", "l", "l"])
        table.set_cols_valign(["m", "m", "m"])
        table.add_row(
            ["In%s" % n for n in range(len(self.data[0]['inputs']))] +
            ["Out%s" % n for n in range(len(self.data[0]['outputs']))]
        )
        for row in self.data:
            table.add_row(row['inputs'] + row['outputs'])

        print(table.draw())

    def print_io(self, inputs, outputs):
        table = Texttable()
        table.set_cols_align(["l", "l", "l"])
        table.set_cols_valign(["m", "m", "m"])
        table.add_row(
            ["In%s" % n for n in range(len(inputs[0]))] +
            ["Out%s" % n for n in range(len(outputs[0]))]
        )
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
        for _ in range(times):
            for data in self.data:
                self.next_dataset(data['inputs'], data['outputs'])
                self.stimulate()
                self.backpropagate()

    def test(self, input):
        self.next_dataset(input, [])
        self.stimulate()
        return [output.get_value() for output in self.layers[-1].neurons]

