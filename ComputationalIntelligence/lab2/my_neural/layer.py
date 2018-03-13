
from textwrap import dedent

from utils import NamePicker


class Layer:

    def __init__(self, neurons=None, name=None):
        self.neurons = neurons or []
        self.name = name or NamePicker().get_layer_name()

    def add_neuron(self, neuron):
        self.neurons.append(neuron)

    def get_neurons(self):
        return self.neurons

    def __repr__(self):
        to_print = "Layer %s [\n" % self.name
        for i, neuron in enumerate(self.neurons):
            to_print = to_print + "    neuron %s - %s\n" % (i, neuron.name)
        return dedent(to_print + "]")
