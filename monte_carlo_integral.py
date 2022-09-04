import random as rnd


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
        x = (xmax - xmin) * p + xmin
        p = rnd.random()
        y = (ymax - ymin) * p + ymin
        if f(x) > y:
            m += 1
    return m * (b - a) * f(b) / exp_nmb


def main():
    print(calc_integ(f, 2, 0, 10 ** 2))


if __name__ == "__main__":
    main()
