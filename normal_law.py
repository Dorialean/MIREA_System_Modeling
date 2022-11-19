import math
import random
from collections import OrderedDict

from scipy import integrate
import numpy as np
import matplotlib.pyplot as plt


class Ziggurat:
    def __init__(self, sample, regions, nbins, mu, sigma, max_i=10):
        self.sample = sample
        self.regions = regions
        self.nbins = nbins
        self.max_i = max_i

        self.mu = mu
        self.sigma = sigma

    def ziggurat(self):

        X_0 = 0
        limit = 20
        rectangle_size = 1 / (self.regions)
        X = np.array([])
        dX = 0.01
        current_x = X_0
        current_area, rectangle_length = 0, 0
        Z = np.ones(self.sample)

        while current_x < limit:
            rectangle_length = rectangle_length + dX
            current_area = (
                                   (1 / np.sqrt(2 * np.pi)) * np.exp(-0.5 * (current_x ** 2))
                                   - (1 / np.sqrt(2 * np.pi)) * np.exp(-0.5 * (rectangle_length ** 2))
                           ) * rectangle_length

            if current_area > rectangle_size:
                X = np.append(X, rectangle_length)
                current_x = rectangle_length

        Y = 1 / np.sqrt(2 * np.pi) * np.exp(-0.5 * (X ** 2))

        for j in range(self.sample):
            num = 0
            while (Z[j] == 1) and num < self.max_i:
                i = np.random.randint(0, len(X))
                u0 = np.random.uniform(-1, 1)
                u1 = np.random.uniform(0, 1)
                x = u0 * X[i]
                if abs(x) < X[i - 1]:
                    Z[j] = x
                else:
                    y = Y[i] + u1 * (Y[i - 1] - Y[i])
                    point = 1 / np.sqrt(2 * np.pi) * np.exp(-0.5 * (x ** 2))
                    if y < point:
                        Z[j] = x
                num = num + 1

        return Z

    def plot_matplotlib(self):
        data = self.ziggurat()
        data = data * self.sigma + self.mu
        plt.hist(data, bins=self.nbins, density=True)
        plt.grid(True)

        plt.title("Функция плотности вероятности")

    def plot_matplotlib_in_range(self, start, end):
        data = self.ziggurat()
        data = data * self.sigma + self.mu
        plt.hist(data, bins=self.nbins, density=True)
        plt.grid(True)
        plt.xlim(start, end)
        plt.title("Функция плотности вероятности")


def plot_normal_distribution(mu, sigma):
    x = np.linspace(mu - 3 * sigma, mu + 3 * sigma, 100)
    plt.plot(
        x,
        1 / (sigma * np.sqrt(2 * np.pi)) * np.exp(-((x - mu) ** 2) / (2 * sigma ** 2)),
        linewidth=2,
        label=f"{mu = }; {sigma = }",
    )
    plt.grid(True)
    plt.legend()
    plt.title("Нормальное распределение")


def raspredelenie_normalnogo_zakona(f, x):
    Fx = integrate.quad(f, -math.inf, x)
    return Fx


def root_mean_square_deviation(data, mu):
    return np.sqrt(np.sum((data - mu) ** 2) / len(data))


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

        plt.plot(X, y, linewidth=2, label=f'Мат ожидание={M}, Сигма = {sigma}')
    plt.title("Распределение плотности вероятности")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.legend()
    plt.show()

    N = [10 ** 3, 10 ** 4, 10 ** 5, 10 ** 6]

    for i in range(len(N)):
        mu, sigma = 10, 2

        z = Ziggurat(N[i], regions=100, nbins=100, mu=mu, sigma=sigma)
        z.plot_matplotlib()
        plot_normal_distribution(mu, sigma)
        print(f"N = {N[i]:.0e}")
        plt.show()


    res = []
    for x in X:
        res.append(raspredelenie_normalnogo_zakona(rapsredelenie_plotnosti_veroyatnosti_normalni_zakon, x))
    plt.plot(res)
    plt.title("Обратная функция")
    plt.show()

    N = [10 ** 3, 10 ** 4, 10 ** 5, 10 ** 6]

    rmsd = []
    for i in range(len(N)):
        mu, sigma = 10, 2

        z = Ziggurat(N[i], regions=100, nbins=100, mu=mu, sigma=sigma)
        data = z.ziggurat()
        data = data * sigma + mu

        rmsd.append(root_mean_square_deviation(data, mu))
        print(f'N = {N[i]}, среднеквадратичное отклонение = {rmsd[-1]}')

    plt.plot(rmsd, N)
    plt.grid(True)
    plt.title("среднеквадратичное отклонение")
    plt.show()



if __name__ == '__main__':
    main()


