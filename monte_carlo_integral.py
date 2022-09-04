import math
import random as rnd

import numpy as np


def f(x):
    return x ** 3 + 1


def calc_integ(f, a, b, exp_nmb):
    xmin = a
    xmax = b
    ymin = 0
    ymax = f(b)
    m = 0

    for i in range(exp_nmb):
        p = rnd.random()
        xp = (xmax - xmin) * p + xmin
        p = rnd.random()
        yp = (ymax - ymin) * p + ymin
        if f(xp) > yp:
            m += 1
    return m * (b - a) * f(b) / exp_nmb


def create_series() -> np.ndarray:
    series = np.empty(5)
    i = 0
    for power in range(3, 8):
        series[i] = calc_integ(f, 0, 2, 10 ** power)
        i += 1
    return series


def calc_eps(seria) -> float:
    return math.fabs((seria - 6) / 6)


def create_eps(series):
    eps = np.empty(5, dtype=np.ndarray)
    ind = 0
    for s in series:
        cur_eps = calc_eps(s)
        eps[ind] = np.array(cur_eps)
        ind += 1
    return eps


def main():
    series = create_series()
    eps = create_eps(series)
    sums = np.empty(5)
    eps_sums = np.empty(5)

    for i in range(len(series)):
        sums[i] = sum(series) / len(series)
        eps_sums[i] = math.fabs((sums[i] - 6) / 6)

    for i in range(5):
        print(f"series{i}:{series[i]}")
        for e in eps:
            print(f"eps{i}:{e}")
        for s in sums:
            print(f"sums {i}:{s}")
        for e in eps_sums:
            print(f"eps sums{i}:{e}")


if __name__ == "__main__":
    main()
