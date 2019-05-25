import logging
import coloredlogs
import pandas

from multiprocessing import cpu_count
from joblib import Parallel
from joblib import delayed
from argparse import ArgumentParser
from glob import glob

from checks import z_score, irq, same_values, two_sigma, isolation_forest


CHECKS = [
    same_values,
    z_score,
    irq,
    two_sigma,
    isolation_forest
]


def find_csvs(directory):
    return glob(directory, recursive=True)


def sanitize_input(dataframe):
    dataframe.set_index('timestamp', inplace=True)
    dataframe.rename(columns=lambda x: x.strip(), inplace=True)
    return dataframe


def check(i, file, files_to_process):
    logging.info("[%s/%s] processing %s", i, len(files_to_process), file)
    try:
        logging.debug("loading file contents")
        csv = sanitize_input(pandas.read_csv(file))

    except Exception as e:
        logging.warning("something is wrong with %s", file)
        logging.error(e)

    for check in CHECKS:
        check(csv, file)


if __name__ == '__main__':
    coloredlogs.install()
    parser = ArgumentParser(description='Script for filtering faulty records in provided dataset')
    parser.add_argument(
        '-d', '--directory',
        help="Directory containing csv files. Script searches for csv's recursively",
        default="**/BITalino/*.csv"
    )
    args = parser.parse_args()
    files_to_process = find_csvs(args.directory)
    executor = Parallel(n_jobs=cpu_count(), backend='multiprocessing')
    tasks = [delayed(check)(i, file, files_to_process) for i, file in enumerate(files_to_process, 1)]
    scores = executor(tasks)
