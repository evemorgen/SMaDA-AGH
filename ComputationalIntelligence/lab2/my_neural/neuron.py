from random import random
from collections import namedtuple
from utils import NamePicker

Connection = namedtuple('Connection', ['neuron', 'weight', 'sums'])


class Neuron:

    def __init__(self, delta=None, inputs=None, outputs=None):
        self.inputs = inputs or []
        self.outputs = outputs or []
        self.weighted_sum = 0
        self.delta = delta or 0
        self.output_value = 0
        self.name = NamePicker().get_neuron_name()

    def connect_input(self, another_neuron, weight=None):
        # fixme not self but Connection with neuron=self
        if self not in another_neuron.outputs:
            another_neuron.connect_output(self)
        if another_neuron not in self.inputs:
            self.inputs.append(Connection(neuron=another_neuron, weight=weight or random(), sums=0))

    def connect_output(self, another_neuron, weight=None):
        if self not in another_neuron.inputs:
            another_neuron.connect_input(self)
        if another_neuron not in self.outputs:
            self.outputs.append(Connection(neuron=another_neuron, weight=weight or random(), sums=0))

    def __repr__(self):
        return "Neuron({} - inputs: {}, outputs: {}, delta: {}, output value: {})".format(
            self.name,
            [(inp.neuron.name, round(inp.weight)) for inp in self.inputs],
            [(out.neuron.name, round(out.weight, 2)) for out in self.outputs],
            self.delta,
            self.output_value
        )
