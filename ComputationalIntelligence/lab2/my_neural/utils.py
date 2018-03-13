import json
from pandas import read_excel
from singleton_decorator import singleton


def load_xls(filename):
    xls = read_excel(open(filename, 'rb'), sheet_name=0)


def load_json(filename):
    with open(filename) as json_data:
        dataset = json.load(json_data)

    assert isinstance(dataset, list), "input must be formed as array or tuples"
    return dataset


@singleton
class NamePicker():
    def __init__(self):
        self.names = [
            "Aero", "Aurora", "Bellatrix", "Cassiopeia", "Celeste", "Cosima",
            "Cosmo", "Eartha", "Galaxy", "Gemini", "Io", "Izar", "Izarra",
            "Jupiter", "Luna", "Mars", "Mercury", "Moon", "Neptune", "Nova",
            "Orion", "Pluto", "Rocket", "Soleil", "Star", "Starla", "Sunny",
            "Urania", "Vega", "Venus", "Vesper"
        ]
        self.i = 0
        self.j = 0

    def get_neuron_name(self):
        self.i = (self.i + 1) % len(self.names)
        return ("%s%s" % (self.names[self.i], self.i))

    def get_layer_name(self):
        self.i = (self.i + 1) % len(self.names)
        return ("%s%s" % (self.names[self.i], self.i))
