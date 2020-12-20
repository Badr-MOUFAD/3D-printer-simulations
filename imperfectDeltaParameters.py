from simulationNacelle.equationMotion import sinPi3, cosPi3
from simulationDesignInperfection.deltaGlobalEquation import Delta

import numpy as np


axisOne = dict(
    id=1,
    R=710.7,
    r=130,
    L=965,
    H=1995,
    phi=0.008726646,
    theta=1.558579022,
    angleBasisChange=np.pi - 1.049 / 2
)

axisTwo = dict(
    id=2,
    R=713.6,
    r=130,
    L=965,
    H=1995,
    phi=0.008726646,
    theta=1.58650429,
    angleBasisChange=1.042 / 2
)


axisThree = dict(
    id=3,
    R=710.7,
    r=130,
    L=965,
    H=1995,
    phi=-0.019198622,
    theta=1.574286985,
    angleBasisChange=-np.pi/2
)


def rotationZ(angle):
    return np.array([[np.cos(angle), -np.sin(angle), 0], [np.sin(angle), np.cos(angle), 0], [0, 0, 1]], dtype=float)


def rotationY(angle=None):
        return np.array([[0, 0, -1], [0, 1, 0], [1, 0, 0]], dtype=float)


def computeEquationCoef(axis):
    matrix = rotationZ(axis["angleBasisChange"]).dot(rotationY())
    Ix, Iy, Iz = matrix.dot(
        [np.cos(axis["phi"]) * np.sin(axis["theta"]), np.sin(axis["phi"]) * np.sin(axis["theta"]),
         np.cos(axis["theta"])])

    DR = axis["R"] - axis["r"]
    id = axis["id"]

    if id == 1:
        return Ix, Iy, Iz, sinPi3 * DR, cosPi3 * DR, 0
    elif id == 2:
        return Ix, Iy, Iz, - sinPi3 * DR, cosPi3 * DR, 0
    elif id == 3:
        return Ix, Iy, Iz, 0, - DR, 0


# robot = Delta(arrAxis=[axisOne, axisTwo, axisThree])
#
# point = [10, 20, 950]
#
# print(robot.inverseKinetic(*point))

print(computeEquationCoef(axisThree))
