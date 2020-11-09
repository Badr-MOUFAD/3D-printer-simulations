import numpy as np

from Analysis import VectorFunction, algorithmNewtonRaphson

cosPi3 = np.cos(np.pi / 3)
sinPi3 = np.sin(np.pi / 3)


axisOne = dict(
    R=860 + 1,
    r=180 + 0,
    L=840 + 0,
    H=1820,
    phi=0,
    theta=0,
)

axisTwo = dict(
    R=860 + 0,
    r=180 + 0,
    L=840 + 0,
    H=1820,
    phi=0,
    theta=0
)


axisThree = dict(
    R=860 + 0,
    r=180 + 0,
    L=840 + 0,
    H=1820,
    phi=0,
    theta=0
)


def inverseKinetic(x, y, z):
    def equaGenerator(axis, var):
        DR = axis["R"] - axis["r"]
        Ix, Iy, Iz = [np.cos(axis["phi"]) * np.sin(axis["theta"]), np.sin(axis["phi"]) * np.sin(axis["theta"]), np.cos(axis["theta"])]

        Ex, Ey, Ez = [0, 0, 0]
        if var == 0:
            Ex, Ey, Ez = [x + sinPi3 * DR, y + cosPi3 * DR, z]
        elif var == 1:
            Ex, Ey, Ez = [x - sinPi3 * DR, y + cosPi3 * DR, z]
        elif var == 2:
            Ex, Ey, Ez = [x, y - DR, z]

        def equation(vec):
            return (Ix * vec[var] - Ex) ** 2 + (Iy * vec[var] - Ey) ** 2 + (Iz * vec[var] - Ez) ** 2 - axis["L"] ** 2

        return equation

    systemFunction = VectorFunction(
        coordinateFunctions=[equaGenerator(axisOne, 0), equaGenerator(axisTwo, 1), equaGenerator(axisThree, 2)])
    sol = algorithmNewtonRaphson(function=systemFunction, starting=np.array([axisOne["H"], axisOne["H"], axisOne["H"]]),
                                 precision=10**-2)

    return sol


def forwardKinetic(L1, L2, L3):
    if L1 == L2 and L2 == L3:  # this situation cause a singular matrix in algo Newton-Raphson
        L1 += 0.1

    def equaGenerator(axis, var):
        DR = axis["R"] - axis["r"]
        Ix, Iy, Iz = [np.cos(axis["phi"]) * np.sin(axis["theta"]), np.sin(axis["phi"]) * np.sin(axis["theta"]), np.cos(axis["theta"])]

        Ex, Ey, Ez = [0, 0, 0]
        if var == 0:
            Ex, Ey, Ez = [sinPi3 * DR - Ix * L1, cosPi3 * DR - Iy * L1, -Iz * L1]
        elif var == 1:
            Ex, Ey, Ez = [- sinPi3 * DR - Ix * L2, cosPi3 * DR - Iy * L2, - Iz * L2]
        elif var == 2:
            Ex, Ey, Ez = [-Ix * L3, - DR - Iy * L3, -Iz * L3]

        def equation(vec):
            return (vec[0] + Ex) ** 2 + (vec[1] + Ey) ** 2 + (vec[2] + Ez) ** 2 - axis["L"] ** 2

        return equation

    systemFunction = VectorFunction(
        coordinateFunctions=[equaGenerator(axisOne, 0), equaGenerator(axisTwo, 1), equaGenerator(axisThree, 2)])
    sol = algorithmNewtonRaphson(function=systemFunction, starting=np.array([0, 0, min(L1, L2, L3)]),
                                 precision=10 ** -2)

    return sol


# input = [0, 0, 0]
#
# command = inverseKinetic(*input)
# print(command)

# point = inverseKinetic(*[0, 0, 0])

#
# print(point)

# [-0.04187231 -0.02417499  6.88021772] ideal
# [4.35385078 2.51369692 3.41833187] déformé


#[-0.61900116 -0.35738049  7.34043026]
