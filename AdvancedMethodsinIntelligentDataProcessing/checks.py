import numpy
import pandas
import logging
import time

from scipy import stats
from sklearn.cluster import DBSCAN
from sklearn.ensemble import IsolationForest


def same_values(data, filename):
    counts = data['value'].value_counts()
    if numpy.any(counts > 0.5 * len(data['value'])):
        logging.warning(
            f"[over 50% same values] {filename} contained {len(counts)} different values, "
            f"{round((counts.values[0] / len(data)) * 100, 2)}% of them was {counts.index[0]}"
        )
        return False
    return True


def z_score(data, filename):
    z = numpy.abs(stats.zscore(data))
    threshold = 3
    outliers = numpy.where(z > threshold)
    if (len(outliers) / len(data)) * 100 > 10:
        logging.warning(
            f"[over z-score threshold] {filename} contained {len(outliers)} outliers, "
            f"above z-score threshold={threshold}"
        )


def irq(data, filename):
    Q1 = data.quantile(0.25)
    Q3 = data.quantile(0.75)
    IQR = Q3 - Q1
    left = (data < (Q1 - 1.5 * IQR))
    right = (data > (Q3 + 1.5 * IQR))
    result = pandas.merge(left, right, on=['timestamp'])
    fauly_values = result[result.value_x | result.value_y]
    if (len(fauly_values) / len(data)) * 100 > 10:
        logging.warning(
            f"[over irq threshold] {filename} contained {len(fauly_values)} values outside IRQ, "
            f"which is {round((len(fauly_values) / len(data)) * 100)}% of values"
        )
        return False
    return True


def two_sigma(data, filename):
    mean = data.value.mean()
    std = data.value.std()
    left = (data.value < mean - 2 * std)
    right = (data.value > mean + 2 * std)
    result = pandas.merge(left, right, on=['timestamp'])
    fauly_values = result[result.value_x | result.value_y]
    if (len(fauly_values) / len(data)) * 100 > 10:
        logging.warning(
            f"[over two sigma threshold] {filename} contained {len(fauly_values)} values outside two-sigma, "
            f"which is {round((len(fauly_values) / len(data)) * 100)}% of values"
        )
        return False
    return True


def dbscan(data, filename):
    print("starting db scan")
    outlier_detection = DBSCAN(min_samples=1000, eps=50)
    start = time.time()
    clusters = outlier_detection.fit_predict(data)
    stop = time.time()
    print(list(clusters).count(-1))
    print("took %s" % (stop - start))


def isolation_forest(data, filename):
    clf = IsolationForest(behaviour='new', max_samples=500, random_state=1, contamination='auto')
    start = time.time()
    preds = clf.fit_predict(data)
    end = time.time()
    outliers = numpy.unique(preds, return_counts=True)[1][0]
    print(outliers)
    print("done, took %s" % (end - start))
    if (outliers / len(data)) * 100 > 35:
        logging.warning(
            f"[isolation forest] {filename} contained {outliers} values outside clusters in isolation forest, "
            f"which is {round((outliers / len(data)) * 100)}% of values"
        )
