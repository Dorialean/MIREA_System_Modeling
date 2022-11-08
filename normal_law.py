import math
import random
from scipy import integrate
import numpy as np
import matplotlib.pyplot as plt


def rapsredelenie_plotnosti_veroyatnosti(x, sigma, M):
    px = (1 / (sigma * math.sqrt(2 * math.pi))) * math.exp(-(x - M) ** 2 / (2 * (sigma ** 2)))
    return px


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

    plt.show()

if __name__ == '__main__':
    main()
