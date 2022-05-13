import numpy
import numpy as np


def fill_with_mean(a: numpy.ndarray) -> numpy.ndarray:
    for i in range(a.shape[1]):
        column = a[:, i]
        average = np.mean(column[column == column])
        column[np.isnan(column)] = average
    return a


def fill_with_min(a: numpy.ndarray) -> numpy.ndarray:
    for i in range(a.shape[1]):
        column = a[:, i]
        minimum = np.min(column[column == column])
        column[np.isnan(column)] = minimum
    return a


def fill_with_max(a: numpy.ndarray) -> numpy.ndarray:
    for i in range(a.shape[1]):
        column = a[:, i]
        maximum = np.max(column[column == column])
        column[np.isnan(column)] = maximum
    return a


def fill_with_median(a: numpy.ndarray) -> numpy.ndarray:
    for i in range(a.shape[1]):
        column = a[:, i]
        median_num = np.median(column[column == column])
        column[np.isnan(column)] = median_num
    return a
