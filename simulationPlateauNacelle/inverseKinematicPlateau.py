import numpy as np

from simulationPlateau.equationMotionPlateau import sinPi3, cosPi3
from simulationPlateau.equationMotionPlateau import computePhi, computeTheta

# ----- note: all input angles are in degree ----- #

# constant
R = 860
x = 50
Rx = R - x

a = np.sqrt(3) * Rx


# angle of the form (phi, theta)
def normal(angle):
    phi = angle[0] * np.pi / 180
    theta = angle[1] * np.pi / 180

    nx = np.cos(phi) * np.sin(theta)
    ny = np.sin(phi) * np.sin(theta)
    nz = np.cos(theta)

    return [nx, ny, nz]


def clusterX2(phi, sol1, sol2):
    if -90 < phi <= -30:
        return sol1 if sol1 >= 0 else sol2

    if -30 <= phi <= 30:
        return sol1 if sol1 >= 0 else sol2

    if 30 < phi <= 60:
        return max(sol1, sol2)

    if 60 <= phi <= 90:
        return min(sol1, sol2)

    if 90 <= phi <= 150:
        return sol1 if sol1 <= 0 else sol2

    if 150 <= phi <= 180:
        return sol1 if sol1 <= 0 else sol2

    if -180 <= phi < -150:
        return sol1 if sol1 <= 0 else sol2

    if -150 <= phi < -120:
        return min(sol1, sol2)

    if -120 <= phi <= -90:
        return max(sol1, sol2)


def clusterX3(phi, sol1, sol2):
    if -90 <= phi <= -30:
        return sol1 if sol1 <= 0 else sol2

    if -30 <= phi <= 0:
        return min(sol1, sol2)

    if 0 <= phi <= 30:
        return max(sol1, sol2)

    if 30 <= phi <= 90:
        return sol1 if sol1 >= 0 else sol2

    if 90 <= phi < 150:
        return sol1 if sol1 >= 0 else sol2

    if 150 <= phi <= 180:
        return max(sol1, sol2)

    if -180 <= phi <= -150:
        return min(sol1, sol2)

    if -150 < phi <= -90:
        return sol1 if sol1 <= 0 else sol2


def x2(angle):
    nx, ny, nz = normal(angle)
    nw = nx * sinPi3 - ny * cosPi3

    c1 = nw ** 2 + nz ** 2
    c2 = nz * (nx * sinPi3 + ny * cosPi3 - nw * cosPi3) * Rx
    c3 = ((nx * sinPi3 + ny * cosPi3 - nw * cosPi3) * Rx) ** 2 + (nw * sinPi3 * Rx) ** 2 - (nw * a) ** 2

    sol1 = (c2 + np.sqrt(c2 ** 2 - c1 * c3)) / c1
    sol2 = (c2 - np.sqrt(c2 ** 2 - c1 * c3)) / c1

    return sol1, sol2


def x3(angle):
    nx, ny, nz = normal(angle)

    c1 = ny ** 2 + nz ** 2
    c2 = nx * nz * sinPi3 * Rx
    c3 = (nx ** 2 + ny ** 2) * (Rx * sinPi3) ** 2 - ny ** 2 * a ** 2

    sol1 = (c2 + np.sqrt(c2 ** 2 - c1 * c3)) / c1
    sol2 = (c2 - np.sqrt(c2 ** 2 - c1 * c3)) / c1

    return sol1, sol2


# x is a vector of position (x, y, z)
def L1(x, angle):
    nx, ny, nz = normal(angle)

    xa = -Rx * sinPi3
    ya = -Rx * cosPi3

    return x[2] + (nx * (x[0] - xa) + ny * (x[1] - ya)) / nz


def L2(angle, L1):
    sol1, sol2 = x2(angle)

    return L1 - clusterX2(angle[0], sol1, sol2)


def L3(angle, L1):
    sol1, sol2 = x3(angle)

    return L1 - clusterX3(angle[0], sol1, sol2)


# example
# angle_ = [50, 5]
#
# # print('********')
# print(x2(angle_))
# print(x3(angle_))
# # print('********')
#
# print("L2 = {0}".format(L2(angle_, 500)))
# print("L3 = {0}".format(L3(angle_, 500)))
#
# print("phi = {0}".format(computePhi([500, L2(angle_, 500), L3(angle_, 500)])))
# print("theta = {0}".format(computeTheta([500, L2(angle_, 500), L3(angle_, 500)])))