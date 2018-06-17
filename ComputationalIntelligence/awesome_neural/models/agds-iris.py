import csv
from pprint import pprint
from copy import deepcopy

iris_map = {
    'Iris-setosa': 1,
    'Iris-versicolor': 2,
    'Iris-virginica': 3
}

class Iris:
    def __init__(self, class_name, petal_length, sepal_length, petal_width, sepal_width):
        self.class_name = class_name
        self.petal_length = petal_length
        self.petal_width = petal_width
        self.sepal_length = sepal_length
        self.sepal_width = sepal_width

        self.weight = 0.2

        self.params = {
            'class': iris_map[self.class_name],
            'petal_length': self.petal_length,
            'petal_width': self.petal_width,
            'sepal_length': self.sepal_length,
            'sepal_width': self.sepal_width
        }

    def __repr__(self):
        return "(id: {}, class: {}, {}-{}-{}-{})".format(
            id(self),
            self.class_name,
            self.petal_length,
            self.petal_width,
            self.sepal_length,
            self.sepal_width
        )

def load_data(filename):
    params = {}
    irises = []
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            iris = Iris(
                row['class'],
                row['petal_length'],
                row['sepal_length'],
                row['petal_width'],
                row['sepal_width']
            )
            irises.append(iris)
            for key in row.keys():
                if key not in params:
                    params[key] = {}
            for key, val in row.items():
                if val not in params[key] and val.startswith('Iris'):
                    params[key][iris_map[val]] = []
                elif val not in params[key]:
                    params[key][val] = []
                if val.startswith('Iris'):
                    params[key][iris_map[val]].append(iris)
                else:
                    params[key][val].append(iris)
    return params, irises

def calculate_weights(params, iris):
    weights = deepcopy(params)
    iris.weight = 1.0
    #find me
    iri_value = {'class': iris_map[iris.class_name]}
    for param in params:
        for value in params[param]:
            if iris in params[param][value]:
                try:
                    iri_value[param] = float(value)
                except ValueError:
                    iri_value[param] = iris_map[value]
                weights[param][value] = 1.0

    for param in params:
        mx = max([float(x) for x in params[param].keys()])
        mn = min([float(x) for x in params[param].keys()])
        print(mx, mn)
        for value in params[param]:
            if float(value) != iri_value[param]:
                weights[param][value] = 1 - abs(float(value) - iri_value[param]) / (mx - mn)

    return weights


def get_similarities(weights, irises):
    similarities = []


    for iris in irises:
        tmp = []
        for param in weights:
            if isinstance(weights[param][iris.params[param]], float):
                tmp.append(iris.weight * weights[param][iris.params[param]])

        similarities.append(
            (iris, round(sum(tmp)*100, 2))
        )

    return similarities



params, irises = load_data('../data/training_data/iris-with-header.data')

looking_for = irises[92]

weights = calculate_weights(params, looking_for)
similar = sorted(get_similarities(weights, irises), key=lambda x: x[1])

pprint(similar)


