from neuron import Neuron, InputNeuron, OutputNeuron


class Layer:
    def __init__(self, num_of_neurons=0):
        self.neurons = [Neuron() for _ in range(num_of_neurons)]

    def connect_layer(self, another, side):
        for n in self.neurons:
            for m in another.neurons:
                n.connect(m, side)

    def stimulate_next(self):
        for n in self.neurons:
            n.stimulate_outputs()

    def stimulate_delta(self):
        for n in self.neurons:
            n.stimulate_inputs()

    def calculate_weight(self):
        for n in self.neurons:
            n.calculate_weight()

    def __repr__(self):
        return str(self.neurons)

class InputLayer(Layer):
    def __init__(self, values):
        super().__init__()
        self.neurons = [InputNeuron(value) for value in values]

    def set_input(self, input):
        for n, v in zip(self.neurons, input):
            n.update_value(v)


class OutputLayer(Layer):
    def __init__(self, values):
        super().__init__()
        self.neurons = [OutputNeuron(value) for value in values]

    def calculate_delta(self):
        for neuron in self.neurons:
            neuron.stimulate_delta(None)

    def set_output(self, output):
        for n, v in zip(self.neurons, output):
            n.set_desired(v)