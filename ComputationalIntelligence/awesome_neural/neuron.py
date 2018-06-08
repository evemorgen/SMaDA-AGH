from math import exp

from utils import NamePicker, constants
from math import tanh
from random import uniform


#def activation(value):
#    beta = constants['beta']
#    return 1.0 / (1 + exp(-1 * beta * value))


#def activation(value):
#    beta = constants['beta']
#    return 2.0 / (1.0 + exp(-1.0 * beta * value))

def activation(value):
    return tanh(constants['beta'] * value)


class Connection:
    def __init__(self, one, another, weight=constants['weight']):
        self.one = one
        self.another = another
        #self.weight = weight
        self.weight = uniform(constants['weight'], 0)

    def exist(self, one, another):
        return (self.one == one and self.another == another) or \
               (self.one == another and self.another == one)

    def get_other(self, me):
        return self.one if me == self.another else self.another

    def update_weight(self, new_weight):
        self.weight = new_weight

    def __repr__(self):
        return "{one} -- {weight} -- {another}".format(
            one=self.one,
            another=self.another,
            weight=round(self.weight, 2)
        )

class Neuron:
    def __init__(self):
        self.inputs = []
        self.outputs = []
        self.stimulations = set()
        self.deltas = set()
        self.name = NamePicker().get_neuron_name()

        self.value = 0
        self.delta = 0
        self.sum = 0

        self.learning_factor = constants['learning_factor']


    def connect(self, another, side):
        sides = {
            'left': {'me': self.inputs, 'another': another.outputs },
            'right': {'me': self.outputs, 'another': another.inputs }
        }
        for connection in sides[side]['me']:
            if connection.exist(self, another):
                break
        else:
            conn = Connection(self, another)
            sides[side]['me'].append(conn)
            sides[side]['another'].append(conn)

    def stimulate_me(self, another, value):
        weight = list(filter(lambda input: input.exist(self, another), self.inputs))[0].weight
        self.stimulations.add(
            (another, weight, value)
        )

        if len(self.stimulations) == len(self.inputs):
            self.value = activation(
                sum([weight * value for another, weight, value in self.stimulations])
            )
            self.stimulations = set()

    def stimulate_delta(self, another, value=None, delta=None):
        weight = list(filter(lambda output: output.exist(self, another), self.outputs))[0].weight
        self.deltas.add(
            (another, weight, value, delta)
        )

        if len(self.deltas) == len(self.outputs):
            self.delta = sum([weight * delta * (1 - value) * value for _, weight, value, delta in self.deltas])
            self.deltas = set()

    def stimulate_outputs(self):
        for output in self.outputs:
            output.get_other(self).stimulate_me(self, self.value)

    def stimulate_inputs(self):
        for input in self.inputs:
            input.get_other(self).stimulate_delta(
                self,
                value=self.value,
                delta=self.delta
            )

    def calculate_weight(self, side='from_right'):
        sides = {
            'from_left': None, # placeholder
            'from_right': self.inputs
        }

        for connection in sides[side]:
            other_value = connection.get_other(self).value
            new_weight = - self.learning_factor * self.delta * (1 - self.value) * self.value * other_value
            connection.update_weight(connection.weight - new_weight)

    def __repr__(self):
        return "({}: val={}, del={})".format(
            self.name,
            round(self.value, 2),
            round(self.delta, 2)
        )


class InputNeuron(Neuron):
    def __init__(self, value):
        super().__init__()
        self.inputs = None
        self.value = value
        self.name = NamePicker().get_input_name()

    def update_value(self, value):
        self.value = value


class OutputNeuron(Neuron):
    def __init__(self, desired):
        super().__init__()
        self.outputs = None
        self.name = NamePicker().get_output_name()
        self.desired = desired

    def get_value(self):
        return self.value

    def set_desired(self, desired):
        self.desired = desired

    def stimulate_delta(self, another, value=None, delta=None):
        self.delta = self.desired - self.value