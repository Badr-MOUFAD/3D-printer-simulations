import numpy as np
from Analysis import euclidienNorm, firstNorm, VectorFunction
from simulationNacelle.equationMotion import gen_dL

# constant
cosPi3 = np.cos(np.pi / 3)
sinPi3 = np.sin(np.pi / 3)

# chassis (mm)
R = 860

# axis
axisLength = 1000
limY = R

# plateau
# x = 50
# Rx = R - x
#a = np.sqrt(3) * Rx

# precision
dL = 1.8


# definition
# Ry = R - y
# Rz = R - z


# plateau
x0 = 10
y0 = 10
z0 = 10

Rx = R - x0
Ry0 = R - y0
Rz0 = R - z0

a = np.sqrt(Rx ** 2 + Rz0 ** 2 + Rx * Rz0)
b = np.sqrt(Rx ** 2 + Ry0 ** 2 + Rx * Ry0)


def Ry(L):  # L is a vector (L1, L2, L3)
    term = b ** 2 - (L[0] - L[1]) ** 2 - (sinPi3 * Rx) ** 2

    if term < 0:
        return None

    result = np.sqrt(term) - cosPi3 * Rx

    if result < 0 or result < R - limY:
        return None

    return result


def Rz(L):
    term = a ** 2 - (L[0] - L[2]) ** 2 - (sinPi3 * Rx) ** 2

    if term < 0:
        return None

    result = np.sqrt(term) - cosPi3 * Rx

    if result < 0 or result < R - limY:
        return None

    return result


def vecAC(L):
    if Rz(L) is None:
        return None

    return [Rx * sinPi3, Rz(L) + Rx * cosPi3, L[2] - L[0]]


def vecAB(L):
    if Ry(L) is None:
        return None

    return [Rx + Ry(L) * sinPi3, (Rx - Ry(L)) * cosPi3, L[1] - L[0]]


def computeNormal(L):
    if vecAB(L) is None or vecAC(L) is None:
        return None

    vecNormal = np.cross(vecAB(L), vecAC(L))
    norm = euclidienNorm(vecNormal)

    return vecNormal / norm


def computeAngles(L):
    if vecAB(L) is None or vecAC(L) is None:
        return None

    vecNormal = np.cross(vecAB(L), vecAC(L))
    norm = euclidienNorm(vecNormal)

    return [-90 + np.arccos(np.dot([1, 0, 0], vecNormal) / norm) * 180 / np.pi,
            -90 + np.arccos(np.dot([0, 1, 0], vecNormal) / norm) * 180 / np.pi,
            np.arccos(np.dot([0, 0, 1], vecNormal) / norm) * 180 / np.pi]


def computePhi(L):
    if vecAB(L) is None or vecAC(L) is None:
        return None

    vecNormal = np.cross(vecAB(L), vecAC(L))
    normal = vecNormal / euclidienNorm(vecNormal)

    nx = np.dot([1, 0, 0], normal)
    ny = np.dot([0, 1, 0], normal)

    if nx == 0 and ny == 0:
        return None

    sign = np.sign(ny) if ny != 0 else 1

    return np.arccos(nx / np.sqrt(nx ** 2 + ny ** 2)) * sign * 180 / np.pi


def computeTheta(L):
    if vecAB(L) is None or vecAC(L) is None:
        return None

    vecNormal = np.cross(vecAB(L), vecAC(L))
    normal = vecNormal / euclidienNorm(vecNormal)

    nz = np.dot([0, 0, 1], normal)

    return np.arccos(nz) * 180 / np.pi


def computeMaxMinAnlges(L1, nbPoints=10):
    L2 = np.linspace(0, axisLength, nbPoints)
    L3 = np.linspace(0, axisLength, nbPoints)

    arrAlpha = []
    arrBeta = []
    arrGamma = []

    for l2 in L2:
        for l3 in L3:
            if computeAngles([L1, l2, l3]) is None:
                continue

            alpha, beta, gamma = computeAngles([L1, l2, l3])

            arrAlpha.append(alpha)
            arrBeta.append(beta)
            arrGamma.append(gamma)

    return [[max(arrAlpha), max(arrBeta), max(arrGamma)], [min(arrAlpha), min(arrBeta), 0]]


def computeMaxY(L1, nbPoints=10):
    L2 = np.linspace(0, axisLength, nbPoints)
    y = []

    for l2 in L2:
        if Ry([L1, l2, 0]) is None:
            continue

        y.append(R - Ry([L1, l2, 0]))

    return max(y)


def alpha(L):
    vecNormal = np.cross(vecAB(L), vecAC(L))
    norm = euclidienNorm(vecNormal)

    return -90 + np.arccos(np.dot([1, 0, 0], vecNormal) / norm) * 180 / np.pi


def beta(L):
    vecNormal = np.cross(vecAB(L), vecAC(L))
    norm = euclidienNorm(vecNormal)

    return -90 + np.arccos(np.dot([0, 1, 0], vecNormal) / norm) * 180 / np.pi


def gamma(L):
    vecNormal = np.cross(vecAB(L), vecAC(L))
    norm = euclidienNorm(vecNormal)

    return np.arccos(np.dot([0, 0, 1], vecNormal) / norm) * 180 / np.pi


def precisionAngles(L):
    vecFunction = VectorFunction(coordinateFunctions=[alpha, beta, gamma])

    matrix = vecFunction.jacobienMatrix(L)
    maxPrecision = []

    for dl in gen_dL(dist=dL):
        maxPrecision.append(firstNorm(np.dot(matrix, dl)))

    return max(maxPrecision)


# print(computePhi([500, 500 + 106.70474612339999, 500 - 210.98253586532033]))
# print(computeTheta([500, 500 + 106.70474612339999, 500 - 210.98253586532033]))
# print(computePhi([500, 525.615374658196, 638.0329632014607]))
# print(computeTheta([500, 525.615374658196, 638.0329632014607]))
