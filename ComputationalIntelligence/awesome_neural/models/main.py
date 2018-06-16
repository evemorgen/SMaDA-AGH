from core.layer import Layer, InputLayer, OutputLayer
from core.network import Network

inputs = InputLayer([1, 1, 1])

middle1 = Layer(4)
middle2 = Layer(3)
output = OutputLayer([1,1])

network = Network([inputs, middle1, middle2, output])
network.connect()

#print("changing weight of {} to 0.3".format(middle1.neurons[0]))
#middle1.neurons[0].outputs[0].update_weight(0.3)

for _ in range(100):
    print("-----middle1-------")
    [print(x.inputs) for x in middle1.neurons]
    [print(x.outputs) for x in middle1.neurons]
    print("-----middle2-------")
    [print(x.inputs) for x in middle2.neurons]
    [print(x.outputs) for x in middle2.neurons]

    network.stimulate()
    network.backpropagate()


    print("-----middle1-------")
    [print(x.inputs) for x in middle1.neurons]
    [print(x.outputs) for x in middle1.neurons]
    print("-----middle2-------")
    [print(x.inputs) for x in middle2.neurons]
    [print(x.outputs) for x in middle2.neurons]


    [print(n.get_value()) for n in output.neurons]
