from core.neuron import Neuron, InputNeuron, OutputNeuron


class Layer:
    def __init__(self, num_of_neurons=0, name='layer'):
        self.neurons = [Neuron() for _ in range(num_of_neurons)]
        self.name = name
        for n in self.neurons:
            n.set_layer_name(self.name)

    def set_network_name(self, net_name):
        self.network_name = net_name
        for n in self.neurons:
            n.set_network_name(net_name)
            n.set_layer_name(self.name)

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

    def generate_cypher(self):
        query = []
        for n in self.neurons:
            n.set_layer_name(self.name)
            query.append(n.generate_cypher())
        return query

    def __repr__(self):
        return str(self.neurons)

class InputLayer(Layer):
    def __init__(self, values, name='InputLayer'):
        super().__init__(name=name)
        self.neurons = [InputNeuron(value) for value in values]

    def set_input(self, input):
        for n, v in zip(self.neurons, input):
            n.update_value(v)


class OutputLayer(Layer):
    def __init__(self, values, name='OutputLayer'):
        super().__init__(name=name)
        self.neurons = [OutputNeuron(value) for value in values]

    def calculate_delta(self):
        for neuron in self.neurons:
            neuron.stimulate_delta(None)

    def set_output(self, output):
        for n, v in zip(self.neurons, output):
            n.set_desired(v)


class BiasLayer(Layer):
    def __init__(self, neurons, name='BiasLayer'):
        super().__init__(name=name)
        self.neurons = neurons

    def pass_output(self, outputs):
        for neuron, value in zip(self.neurons, outputs):
            neuron.set_bias(value)