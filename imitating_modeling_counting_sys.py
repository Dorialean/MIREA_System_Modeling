import numpy as np


def multiplicating_rand_method(a, b, m, x):
    return (a * x + b) % m


def get_tc(TZ):
    max_time = 3584
    TC = np.zeros(len(TZ))
    TC[0] = TZ[0]
    j = 1
    while TC[j - 1] < max_time:
        TC[j] = TC[j - 1] + TZ[j]
        j += 1
    return TC


def get_time_in_buffer(TC, TS, i):
    if TC[i - 1] + TS[i - 1] >= TC[i]:
        Tb = TC[i - 1] + TS[i - 1] - TC[i]
    else:
        Tb = 0
    return Tb


def get_buffer_time(TC, TS, n: int):
    time = 0
    for i in range(len(TC) - n - 1):
        time_works = TC[i] + TS[i]
        count = 0
        k = 1
        while TC[i + k] < time_works:
            count += 1
            k += 1
        if count == n:
            time += time_works - TC[i + k - 1]
    return time


def main():
    a = 39
    b = 1
    M = 1000
    x = 1
    p = []

    for i in range(1001):
        p.append(x / M)
        x = multiplicating_rand_method(a, b, M, x)

    p = np.array(p)
    TZ = np.zeros(len(p), dtype=np.ndarray)
    TS = np.zeros(len(p), dtype=np.ndarray)

    TZmax = 12
    TZmin = 4
    TSmax = 8
    TSmin = 2

    for i in range(1001):
        TZ[i] = (TZmax - TZmin) * p[i] + TZmin
        print(f'TZ {i + 1} : {TZ[i]}')
        TS[i] = (TSmax - TSmin) * p[i] + TSmin
        print(f'TS {i + 1} : {TS[i]}')

    Tc = get_tc(TZ)
    for t in Tc:
        print(f'Tc : {t}')
    P = np.zeros(5, dtype=np.ndarray)
    Times = np.zeros(5, dtype=np.ndarray)
    for i in range(5):
        Times[i] = get_buffer_time(Tc, TS, i + 1)
        P[i] = Times[i] / 3600
        print(f'time{i+1} : {Times[i]}')
        print(f'P{i+1}: {P[i]}')


if __name__ == "__main__":
    main()
