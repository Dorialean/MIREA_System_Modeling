import math

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


def random_period(Y):
    count = 0
    for i in range(1, len(Y)):
        count += 1
        if Y[i] == 1:
            return count

def pirson_val(Y):
    pass


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
    Periods = np.empty(4, dtype=np.ndarray)

    for i in range(4):
        M_array[i] = math_wait(Yrand_nums[i])
        D_array[i] = dispersion(Yrand_nums[i], M_array[i])
        #Вот тут не понятно то ли считать каждый , то ли нет
        Periods[i] = random_period(Yrand_nums[i])
        # M = (A + B) / 2  M(0,10) = (0 + 10) / 2 = 5
        # D = (B - A) ^ 2 / 12 D(0,10) = (0 - 10) ^ 2 / 12 = 8.(3)



if __name__ == "__main__":
    main()
