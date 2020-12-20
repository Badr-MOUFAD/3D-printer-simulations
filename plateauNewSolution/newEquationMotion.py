from Analysis import euclidienNorm, VectorFunction, algorithmNewtonRaphson
from simulationNacelle.equationMotion import sinPi3, cosPi3

import numpy as np

# constant
#a = 1371  # length triangle corner
e = 0   # distance slider - plan
R = 792  # distance axis / robot center
d = 20  # distance axis / joint
a = (R - d) * np.sqrt(3)

xA = -(R - d) * sinPi3
yA = -(R - d) * cosPi3

xB = (R - d) * sinPi3
yB = -(R - d) * cosPi3

xC = 0
yC = R - d

distTransMax = 50
distTransMin = -16


# angle of the form (phi, theta)
# angle in deg
def normal(angles):
    phi = angles[0] * np.pi / 180
    theta = angles[1] * np.pi / 180

    nx = np.cos(phi) * np.sin(theta)
    ny = np.sin(phi) * np.sin(theta)
    nz = np.cos(theta)

    return np.array([nx, ny, nz], dtype=float)


def L1(vec, angles):
    n = normal(angles)
    x, y, z = np.array(vec, dtype=float) - e * n

    return z + (n[0] * (x - xA) + n[1] * (y - yA)) / n[2]


def L2(vec, angles):
    n = normal(angles)
    x, y, z = np.array(vec, dtype=float) - e * n

    return z + (n[0] * (x - xB) + n[1] * (y - yB)) / n[2]


def L3(vec, angles):
    n = normal(angles)
    x, y, z = np.array(vec, dtype=float) - e * n

    return z + (n[0] * (x - xC) + n[1] * (y - yC)) / n[2]


def computeLo(vec, angles):
    nx, ny, nz = normal(angles)
    x, y, z = vec

    return np.abs(z + (nx * x + ny * y) / nz)


def findDistanceTranslation(vec, angles):

    # params = [RA, RB, RC, LA, LB, LC]
    # index =   0   1   2   3   4   5
    def A(params):
        return np.array([-params[0] * sinPi3, -params[0] * cosPi3, params[3]], dtype=float)

    def B(params):
        return np.array([params[1] * sinPi3, -params[1] * cosPi3, params[4]], dtype=float)

    def C(params):
        return np.array([0, params[2], params[5]], dtype=float)

    n = normal(angles)
    vec = np.array(vec, dtype=float)

    arrCoordinateFunctions = [
        lambda params: n.dot(A(params) - vec),
        lambda params: n.dot(B(params) - vec),
        lambda params: n.dot(C(params) - vec),
        lambda params: euclidienNorm(B(params) - A(params)) - a,
        lambda params: euclidienNorm(C(params) - A(params)) - a,
        lambda params: euclidienNorm(C(params) - B(params)) - a
    ]

    systemFunction = VectorFunction(coordinateFunctions=arrCoordinateFunctions)
    startingPoint = np.array([R, R, R, L1(vec, angles), L2(vec, angles), L3(vec, angles)], dtype=float)

    solution = algorithmNewtonRaphson(systemFunction, starting=startingPoint, precision=10**-4)

    return euclidienNorm(A(solution) - np.array([xA, yA, L1(vec, angles)], dtype=float)) * np.sign(R - d - solution[0]), \
           euclidienNorm(B(solution) - np.array([xB, yB, L2(vec, angles)], dtype=float)) * np.sign(R - d - solution[1]), \
           euclidienNorm(C(solution) - np.array([xC, yC, L3(vec, angles)], dtype=float)) * np.sign(R - d - solution[2])


def computeThinkness(vec):
    nbPoints = 100

    arrPhi = np.linspace(-180, 179, nbPoints)
    arrTheta = np.linspace(0, 90, nbPoints)

    for theta in arrTheta:
        for phi in arrPhi:
            angles = [phi, theta]

            for dist in findDistanceTranslation(vec, angles):
                if dist < distTransMin or dist > distTransMax:
                    return theta

            if 0 <= L1(vec, angles) <= 1000 and 0 <= L2(vec, angles) <= 1000 and 0 <= L3(vec, angles) <= 1000:
                continue
            else:
                return theta
    return
# angle = 30 / 180 * np.pi
# # print(computeThinkness([400 * np.cos(angle), 400 * np.sin(angle), 500]))