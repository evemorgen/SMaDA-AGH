from core.layer import Layer, InputLayer, OutputLayer
from core.network import Network, connect_om

inputs_som = InputLayer([1, 1, 1])
middle_som = Layer(9)
output_som = OutputLayer([1, 1, 1, 1])

som = Network([inputs_som, middle_som, output_som])
som.connect()

inputs_mlp = InputLayer([1, 1, 1, 1])
middle_mlp = Layer(3)
output_mlp = OutputLayer([1, 1, 1])

mlp = Network([inputs_mlp, middle_mlp, output_mlp])
mlp.connect()

connect_om(som, mlp)