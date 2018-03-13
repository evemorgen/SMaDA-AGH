from neuron import Neuron
from layer import Layer
from utils import load_json, load_xls


if __name__ == '__main__':
    data = load_json("data/mock_data.json")
    input_layer = Layer(name='input')
    input_layer.add_neuron(Neuron())
    input_layer.add_neuron(Neuron())
    random_layer = Layer()
    neurons = [Neuron() for i in range(3)]
    for neuron in neurons:
        random_layer.add_neuron(neuron)

    input_neurons = input_layer.get_neurons()
    deep = random_layer.get_neurons()
    for neuron in input_neurons:
        for another_neuron in deep:
            neuron.connect_output(another_neuron)
            print(neuron)

    print(" ============= ")
    for another_neuron in deep:
        print(another_neuron)

    print(random_layer)
    print(input_layer)
