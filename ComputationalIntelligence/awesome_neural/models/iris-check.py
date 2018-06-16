import csv

from core.network import load_network

iris_map = {
    'Iris-setosa': [0, 0, 1],
    'Iris-versicolor': [0, 1, 0],
    'Iris-virginica': [1, 0, 0]
}

reverse_map = {
    (0, 0, 0): "wtf",
    (0, 0, 1): 'Iris-setosa',
    (0, 1, 0): 'Iris-versicolor',
    (1, 0, 0): 'Iris-virginica'
}

network = load_network('data/trained_networks/iris.yaml')

i = []
diagnosis = []
with open('data/training_data/iris.data', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for n, row in enumerate(reader):
        i.append([float(x) for x in row[0:4]])
        diagnosis.append((n, row[4]))
o = [network.test(io) for io in i]

# network.print_io(i, o, output_names=['Iris-virginica', 'Iris-versicolor', 'Iris-setosa'])
good = 0
bad = 0
for tup, out in zip(diagnosis, o):
    _, name = tup
    outtup = (round(x) for x in out)
    if name == reverse_map[tuple(outtup)]:
        good += 1
    else:
        bad += 1

print("good: %s, bad: %s, all: %s" % (good, bad, good + bad))
print("accuracy: %s" % (good / (good + bad) * 100))
