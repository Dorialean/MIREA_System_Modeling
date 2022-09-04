import math
import random
import numpy as np


# s_square = 4 * r0 ** 2
# s_round = s_square * (m / exp_nmb)


def calc_pi(x0, y0, r0, exp_nmb) -> float:
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


def calc_eps(seria) -> float:
    return math.fabs((seria - math.pi) / math.pi)


def main():
    x0 = 1
    y0 = 2
    r0 = 5
    series = np.empty(5, dtype=np.ndarray)
    eps = np.empty(5, dtype=np.ndarray)
    sums = np.empty(5)
    eps_sums = np.empty(5)
    # Создание 5 массивов серий с 5 примерными значениями числа пи в каждом
    for seria_num in range(5):
        seria = np.empty(5)
        i = 0
        for power in range(4, 9):
            exp_nmb = 10 ** power
            seria[i] = calc_pi(x0, y0, r0, exp_nmb)
            i += 1
        series[seria_num] = np.array(seria)
    # Создание 5 массивов отклонений с 5 значениями отклонения в каждом
    ind = 0
    for s in series:
        cur_eps = np.empty(5)
        for calced_pi in s:
            cur_eps = calc_eps(calced_pi)
        eps[ind] = np.array(cur_eps)
        ind += 1
    # Получение среднего результата и создание массива отклонений этих результатов
    for i in range(len(series)):
        sums[i] = (series[0][i] + series[1][i] + series[2][i] + series[3][i] + series[4][i]) / len(series)
        eps_sums[i] = math.fabs((sums[i] - math.pi) / math.pi)
    # Вывод
    for i in range(5):
        for j in range(5):
            print(f"series{i},{j}:{series[i][j]}")
        for e in eps:
            print(f"eps{i}:{e}")
        for s in sums:
            print(f"sums {i}:{s}")
        for e in eps_sums:
            print(f"eps sums{i}:{e}")


if __name__ == "__main__":
    main()
