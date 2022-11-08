import math
import random
from collections import OrderedDict

from scipy import integrate
import numpy as np
import matplotlib.pyplot as plt


def raspredelenie_normalnogo_zakona(f, x):
    Fx = integrate.quad(f, -math.inf, x)
    return Fx


def rapsredelenie_plotnosti_veroyatnosti_normalni_zakon(x):
    sigma = 2
    M = 10
    px = (1 / (sigma * math.sqrt(2 * math.pi))) * math.exp(-(x - M) ** 2 / (2 * (sigma ** 2)))
    return px


def rapsredelenie_plotnosti_veroyatnosti(x, sigma, M):
    px = (1 / (sigma * math.sqrt(2 * math.pi))) * math.exp(-(x - M) ** 2 / (2 * (sigma ** 2)))
    return px


def get_arguments(fmax, fmin, val, f, e):
    min_val = f(fmin)
    max_val = f(fmax)
    while (max_val - min_val) / max_val > e:
        fmid = (min_val + max_val) / 2
        mid_val = f(fmid)
        if mid_val > val:
            fmax = fmid
        else:
            fmin = fmid
        min_val = f(mid_val)
    return (min_val + max_val) / 2


def get_table_f(fmin, fmax, f, segments_amount):
    table_x_to_y = OrderedDict()
    min_val = f(fmin)
    max_val = f(fmax)
    for segment in range(1, segments_amount + 1):
        yi = min_val + (max_val - min_val) * segment / segments_amount
        table_x_to_y[segment] = yi
    return table_x_to_y


def model_n(p, table_x_to_y):
    y = 0
    if 0 >= p >= 1:
        raise Exception("wrong p")
    for curr_x in table_x_to_y.keys():
        if curr_x == 1:
            continue
        prev_y = table_x_to_y[curr_x - 1]
        y += ((p - table_x_to_y[curr_x]) / (prev_y - table_x_to_y[curr_x]) * (curr_x - 1)) + (
                (p - prev_y) / (table_x_to_y[curr_x] - prev_y)) * curr_x
    return y


def main():
    X = range(0, 21, 2)
    y1 = []
    y2 = []
    y3 = []
    y4 = []
    Y = [y1, y2, y3, y4]
    sigma = 0

    for y in Y:
        M = 10
        if y == y1:
            sigma = 2
        elif y == y2:
            sigma = 1
        elif y == y3:
            sigma = 0.5
        elif y == y4:
            M = 12
            sigma = 1

        for i in range(len(X)):
            y.append(rapsredelenie_plotnosti_veroyatnosti(X[i], sigma, M))

        plt.plot(X, y)
    plt.title("Распределение плотности вероятности")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()

    for y in Y:
        M = 10
        sigma = 2
        y.clear()
        for i in range(len(X)):
            y.append(raspredelenie_normalnogo_zakona(rapsredelenie_plotnosti_veroyatnosti_normalni_zakon, X[i]))
        plt.plot(X, y)
    plt.title("Распределение плотности вероятности для нормального закона")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()

    #Здесь что-то не так т.к. таблица в итоге содержит одинаковые значения
    plt.plot(get_table_f(min(X), max(X), rapsredelenie_plotnosti_veroyatnosti_normalni_zakon, 100).keys(),
             get_table_f(min(X), max(X), rapsredelenie_plotnosti_veroyatnosti_normalni_zakon, 100).values())
    plt.title("Кусочно линейная функция при n = 100")
    plt.show()

    models = []
    N = []
    for i in range(3, 7):
        n = 10 ** i
        N.append(n)
        p = random.random()
        models.append(model_n(p, get_table_f(min(X), max(X), rapsredelenie_plotnosti_veroyatnosti_normalni_zakon, n)))
        plt.plot(p, models[i - 3])
        plt.title(f"График кусочно-линейной аппроксимации функции распределения при n = {n}")
        plt.show()

    plt.hist(N, models, bins=100)


if __name__ == '__main__':
    main()
