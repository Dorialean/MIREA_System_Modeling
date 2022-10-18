import math
import random
from scipy import integrate
import numpy as np

import matplotlib.pyplot as plt


def probability_density_distribution(x, M, st_deviation):
    return math.e ** (-((x - M) ** 2) / (2 * st_deviation ** 2)) / (st_deviation * math.sqrt(2 * math.pi))


def normal_law(x, f):
    v, err = integrate.quad(f, -math.inf, x)
    return v


def main():
    M_1 = 10
    st_deviation_1 = 2
    x_1 = random.random()
    res_1 = probability_density_distribution(x_1, M_1, st_deviation_1)

    M_2 = 10
    st_deviation_2 = 1
    x_2 = random.random()
    res_2 = probability_density_distribution(x_2, M_2, st_deviation_2)

    M_3 = 10
    st_deviation_3 = 1 / 2
    x_3 = random.random()
    res_3 = probability_density_distribution(x_3, M_3, st_deviation_3)

    M_4 = 12
    st_deviation_4 = 1
    x_4 = random.random()
    res_4 = probability_density_distribution(x_4, M_4, st_deviation_4)

    # Нужно построить графики (1 задание)


if __name__ == '__main__':
    main()
