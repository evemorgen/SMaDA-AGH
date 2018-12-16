import yaml


def load_config(filename):
    with open(filename, 'r') as yml_file:
        return yaml.load(yml_file)
