import math
import matplotlib.pyplot as plt
import matplotlib

# matplotlib.use('TkAgg')
import numpy as np


def multiplic_gen_rand_nums(a, b, x, m) -> float:
    return (a * x + b) % m


def random_num_in_range(A, B, x):
    return A + (B - A) * x


def math_wait(X):
    res = 0
    for i in range(len(X)):
        res += X[i]
    return res / len(X)


def dispersion(X, M):
    res = 0
    N = len(X)
    for i in range(len(X)):
        res += X[i] ** 2
    return (res / N - M ** 2) * N / (N - 1)


def random_period(Y : np.ndarray):
    count = 0
    for i in range(1, len(Y)):
        count += 1
        if f"{Y[i]:.3f}" == f"{Y[0]:.3f}":
            return count


def pirson_func(Y, np):
    criterii = 0.0
    for j in range(len(Y)):
        n = Y[j] / np
        criterii += (n - np) ** 2 / np
    return criterii


def main():
    m = 2 ** 32
    b = 1
    a = 22695477
    A = 0
    B = 10
    Xrand_nums = np.empty(4, dtype=np.ndarray)
    Yrand_nums = np.empty(4, dtype=np.ndarray)

    for i in range(4):
        n = 10 ** (i + 2)
        Xi = np.empty(n, dtype=np.ndarray)
        x0 = 1
        for j in range(len(Xi)):
            Xi[j] = multiplic_gen_rand_nums(a, b, x0, m)
            x0 = Xi[j]
            Xi[j] /= m
        Xrand_nums[i] = Xi

    for i in range(4):
        Yi = np.empty(len(Xrand_nums[i]), dtype=np.ndarray)
        for j in range(len(Yi)):
            Yi[j] = random_num_in_range(A, B, Xrand_nums[i][j])
        Yrand_nums[i] = Yi

    M_array = np.empty(4, dtype=np.ndarray)
    D_array = np.empty(4, dtype=np.ndarray)
    My_Periods = np.empty(4, dtype=np.ndarray)

    Rnd_Periods = np.empty(4,dtype=np.ndarray)


    for i in range(4):
        M_array[i] = math_wait(Yrand_nums[i])
        D_array[i] = dispersion(Yrand_nums[i], M_array[i])
        My_Periods[i] = random_period(Yrand_nums[i])
        Rnd_Periods[i] = random_period(np.random.default_rng(12345).random(size=10 ** (i + 2)))
        # M = (A + B) / 2  M(0,10) = (0 + 10) / 2 = 5
        # D = (B - A) ^ 2 / 12 D(0,10) = (0 - 10) ^ 2 / 12 = 8.(3)

    for i in range(len(My_Periods)):
        print(f"Период своего алгоритма:{My_Periods[i]}")
        print(f"Период встроенного генератора:{Rnd_Periods[i]}")

    Pirsons = np.empty(4, dtype=np.ndarray)

    for i in range(len(Yrand_nums)):
        plt.title(f"Гистограмма при {i}")
        plt.hist(Yrand_nums[i], bins=10, density=True)
        if My_Periods[i] is not None:
            Pirsons[i] = pirson_func(Yrand_nums[i], My_Periods[i])
        plt.show()

    for p in Pirsons:
        print(f"Значение пирсона:{p}")


if __name__ == "__main__":
    main()
