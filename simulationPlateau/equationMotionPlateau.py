import numpy as np
from Analysis import euclidienNorm

# constant
cosPi3 = np.cos(np.pi / 3)
sinPi3 = np.sin(np.pi / 3)

# chassis (mm)
R = 860

# axis
axisLength = 1000

# plateau
x = 0
Rx = R - x
a = np.sqrt(3) * Rx

# precision
dL = 1.8


# definition
# Ry = R - y
# Rz = R - z


def Ry(L):  # L is a vector (L1, L2, L3)
    term = a ** 2 - (L[0] - L[1]) ** 2 - (sinPi3 * Rx) ** 2

    if term < 0:
        return None

    result = np.sqrt(term) - cosPi3 * Rx

    if result < 0:
        return None

    return result


def Rz(L):
    term = a ** 2 - (L[0] - L[2]) ** 2 - (sinPi3 * Rx) ** 2

    if term < 0:
        return None

    result = np.sqrt(term) - cosPi3 * Rx

    if result < 0:
        return None

    return result


def vecAC(L):
    return [Rx * sinPi3, Rz(L) + Rx * cosPi3, L[2] - L[0]]


def vecAB(L):
    return [Rx + Ry(L) * sinPi3, (Rx - Ry(L)) * cosPi3, L[1] - L[0]]


def computeNormal(L):
    vecNormal = np.cross(vecAB(L), vecAC(L))
    norm = euclidienNorm(vecNormal)

    return vecNormal / norm


def computeAngles(L):
    vecNormal = np.cross(vecAB(L), vecAC(L))
    norm = euclidienNorm(vecNormal)

    return [-90 + np.arccos(np.dot([1, 0, 0], vecNormal) / norm) * 180 / np.pi,
            -90 + np.arccos(np.dot([0, 1, 0], vecNormal) / norm) * 180 / np.pi,
            np.arccos(np.dot([0, 0, 1], vecNormal) / norm) * 180 / np.pi]


def computeMaxMinAnlges(L1, nbPoints=10):
    L2 = np.linspace(0, axisLength, nbPoints)
    L3 = np.linspace(0, axisLength, nbPoints)

    arrAlpha = []
    arrBeta = []
    arrGamma = []

    for l2 in L2:
        for l3 in L3:
            alpha, beta, gamma = computeAngles([L1, l2, l3])

            arrAlpha.append(alpha)
            arrBeta.append(beta)
            arrGamma.append(gamma)

    return [[max(arrAlpha), max(arrBeta), max(arrGamma)], [min(arrAlpha), min(arrBeta), 0]]

