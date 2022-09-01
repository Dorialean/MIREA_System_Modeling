import math
import random


# s_square = 4 * r0 ** 2
# s_round = s_square * (m / exp_nmb)


def calc_pi(x0, y0, r0, exp_nmb):
    m = 0
    x_min = x0 - r0
    x_max = x0 + r0
    y_min = y0 - r0
    y_max = y0 + r0
    for exp in range(exp_nmb):
        p = random.random()
        xp = (x_max - x_min) * p + x_min
        p = random.random()
        yp = (y_max - y_min) * p + y_min
        if (xp - x0) ** 2 + (yp - y0) ** 2 < r0 ** 2:
            m += 1
    calculated_pi = 4 * m / exp_nmb
    return calculated_pi


def main():
    x0 = 1
    y0 = 2
    r0 = 5
    series = list()
    for power, i in range(4, 9), range(5):
        exp_nmb = 10 ** power
        series[i] = calc_pi(x0, y0, r0, exp_nmb)


if __name__ == "__main__":
    main()
