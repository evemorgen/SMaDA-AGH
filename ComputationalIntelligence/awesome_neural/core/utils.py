from singleton_decorator import singleton
import yaml

@singleton
class NamePicker():
    def __init__(self):
        self.names = [
            "Aurora", "Bellatrix", "Cassiopeia", "Dalim", "Eartha", "Fulu", "Galaxy",
            "Helvetios", "Io", "Jupiter", "Kang", "Luna", "Mars", "Nova",
            "Orion", "Pluto", "Rocket", "Soleil", "Urania", "Vesper"
        ]
        self.i = -1

    def _inc_i(self):
        self.i = (self.i + 1) % len(self.names)

    def get_input_name(self):
        self._inc_i()
        return ("input%s" % self.i)

    def get_output_name(self):
        self._inc_i()
        return ("output%s" % self.i)

    def get_neuron_name(self):
        self._inc_i()
        return ("%s%s" % (self.names[self.i], self.i))

    def get_layer_name(self):
        self._inc_i();
        return ("%s%s" % (self.names[self.i], self.i))


with open("../constants.yaml", 'r') as file:
    constants = yaml.load(file)