from math import *


def coseno(x):
    if x == pi/2 or x == -pi/2:
        return 0.0
    else:
        return cos(x)


def seno(x):
    if x == pi:
        return 0.0
    else:
        return sin(x)


def add(c1, c2):
    return c1[0] + c2[0], c1[1] + c2[1]


def dif(c1, c2):
    return c1[0] - c2[0], c1[1] - c2[1]


def modulus(c1):
    return sqrt((c1[0] ** 2) + (c1[1] ** 2))


def conjugate(c1):
    return c1[0], -c1[1]


def cartesian_polar(c1):
    p = modulus(c1)
    if c1[0] != 0:
        theta = atan2(c1[1]/c1[0])
    else:
        if c1[1] > 0:
            theta = pi/2
        else:
            theta = 3 * pi / 2
    return p, theta


def polar_cartesian(c1):
    a = c1[0] * coseno(c1[1])
    b = c1[0] * seno(c1[1])
    return a, b


def phase(c1):
    c1 = cartesian_polar(c1)
    return c1[1]


def multiplication(c1, c2):
    c1 = cartesian_polar(c1)
    c2 = cartesian_polar(c2)
    b = (c1[0] * c2[0], c1[1] + c2[1])
    return polar_cartesian(b)


def division(c1, c2):
    c1 = cartesian_polar(c1)
    c2 = cartesian_polar(c2)
    b = (c1[0] / c2[0], c1[1] - c2[1])
    return polar_cartesian(b)


def cToThePowerOf(c, n):
    c = cartesian_polar(c)
    b = (c[0] ** n, n * c[1])
    d = list(polar_cartesian(b))
    if 2e-16 > d[0] > -2e-16 and 2e-16 > d[1] > -2e-16:
        d[0], d[1] = int(d[0]), int(d[1])
    elif 2e-16 > d[0] > -2e-16:
        d[0] = int(d[0])
    elif 2e-16 > d[1] > -2e-16:
        d[1] = int(d[1])
    return tuple(d)


print(cToThePowerOf((0, 1), 3))