import os
import subprocess

command = 'cat {} | grep {} | grep -o "value=\d\+\.\d\+" | sed -e "s/value=//g"'

def parse_outputs(directory):
    experiments = dict()
    for file in os.listdir(path=directory):
        experiment_name = file.split('.')[0]
        if experiment_name not in experiments:
            experiments[experiment_name] = dict()

        output = subprocess.check_output(
            ['bash', '-c', command.format(directory + "/" + file, 'Best')]
        )
        print(output)


parse_outputs('results')
