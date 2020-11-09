import numpy as np

from Analysis import VectorFunction, algorithmNewtonRaphson


cosPi3 = np.cos(np.pi / 3)
sinPi3 = np.sin(np.pi / 3)


class Delta:
    def __init__(self, arrAxis):
        self.axisOne, self.axisTwo, self.axisThree = arrAxis
        return

    def inverseKinetic(self, x, y, z):
        def equaGenerator(axis, var):
            DR = axis["R"] - axis["r"]
            Ix, Iy, Iz = [0, 0, 0]

            Ex, Ey, Ez = [0, 0, 0]
            if var == 0:
                matrix = Delta.rotationZ(5 * np.pi / 6).dot(Delta.rotationY())
                Ix, Iy, Iz = matrix.dot(
                    [np.cos(axis["phi"]) * np.sin(axis["theta"]), np.sin(axis["phi"]) * np.sin(axis["theta"]),
                     np.cos(axis["theta"])])

                Ex, Ey, Ez = [x + sinPi3 * DR, y + cosPi3 * DR, z]
            elif var == 1:
                matrix = Delta.rotationZ(np.pi / 6).dot(Delta.rotationY())
                Ix, Iy, Iz = matrix.dot(
                    [np.cos(axis["phi"]) * np.sin(axis["theta"]), np.sin(axis["phi"]) * np.sin(axis["theta"]),
                     np.cos(axis["theta"])])

                Ex, Ey, Ez = [x - sinPi3 * DR, y + cosPi3 * DR, z]
            elif var == 2:
                matrix = Delta.rotationZ(-np.pi / 2).dot(Delta.rotationY())
                Ix, Iy, Iz = matrix.dot(
                    [np.cos(axis["phi"]) * np.sin(axis["theta"]), np.sin(axis["phi"]) * np.sin(axis["theta"]),
                     np.cos(axis["theta"])])

                Ex, Ey, Ez = [x, y - DR, z]

            def equation(vec):
                return (Ix * vec[var] - Ex) ** 2 + (Iy * vec[var] - Ey) ** 2 + (Iz * vec[var] - Ez) ** 2 - axis[
                    "L"] ** 2

            return equation

        systemFunction = VectorFunction(
            coordinateFunctions=[equaGenerator(self.axisOne, 0), equaGenerator(self.axisTwo, 1), equaGenerator(self.axisThree, 2)])
        sol = algorithmNewtonRaphson(function=systemFunction,
                                     starting=np.array([self.axisOne["H"], self.axisOne["H"], self.axisOne["H"]]),
                                     precision=10 ** -2)

        return sol

    def forwardKinetic(self, L1, L2, L3):
        if L1 == L2 and L2 == L3:  # this situation cause a singular matrix in algo Newton-Raphson
            L1 += 0.1

        def equaGenerator(axis, var):
            DR = axis["R"] - axis["r"]
            Ix, Iy, Iz = [0, 0, 0]

            Ex, Ey, Ez = [0, 0, 0]

            if var == 0:
                matrix = Delta.rotationZ(5 * np.pi / 6).dot(Delta.rotationY())
                Ix, Iy, Iz = matrix.dot([np.cos(axis["phi"]) * np.sin(axis["theta"]), np.sin(axis["phi"]) * np.sin(axis["theta"]),
                                         np.cos(axis["theta"])])

                Ex, Ey, Ez = [sinPi3 * DR - Ix * L1, cosPi3 * DR - Iy * L1, -Iz * L1]
            elif var == 1:
                matrix = Delta.rotationZ(np.pi / 6).dot(Delta.rotationY())
                Ix, Iy, Iz = matrix.dot(
                    [np.cos(axis["phi"]) * np.sin(axis["theta"]), np.sin(axis["phi"]) * np.sin(axis["theta"]),
                     np.cos(axis["theta"])])

                Ex, Ey, Ez = [- sinPi3 * DR - Ix * L2, cosPi3 * DR - Iy * L2, - Iz * L2]
            elif var == 2:
                matrix = Delta.rotationZ(-np.pi / 2).dot(Delta.rotationY())
                Ix, Iy, Iz = matrix.dot(
                    [np.cos(axis["phi"]) * np.sin(axis["theta"]), np.sin(axis["phi"]) * np.sin(axis["theta"]),
                     np.cos(axis["theta"])])

                Ex, Ey, Ez = [-Ix * L3, - DR - Iy * L3, -Iz * L3]

            def equation(vec):
                return (vec[0] + Ex) ** 2 + (vec[1] + Ey) ** 2 + (vec[2] + Ez) ** 2 - axis["L"] ** 2

            return equation

        systemFunction = VectorFunction(
            coordinateFunctions=[equaGenerator(self.axisOne, 0), equaGenerator(self.axisTwo, 1), equaGenerator(self.axisThree, 2)])
        sol = algorithmNewtonRaphson(function=systemFunction, starting=np.array([0, 0, min(L1, L2, L3)]),
                                     precision=10 ** -2)

        return sol

    @staticmethod
    def rotationZ(angle):
        return np.array([[np.cos(angle), -np.sin(angle), 0], [np.sin(angle), np.cos(angle), 0], [0, 0, 1]], dtype=float)

    @staticmethod
    def rotationY(angle=None):
        return np.array([[0, 0, -1], [0, 1, 0], [1, 0, 0]], dtype=float)


# # example
# axisOne_ = dict(
#     R=860 + 0,
#     r=180 + 0,
#     L=840 + 0,
#     H=1820,
#     phi=0,
#     theta=0,
# )
#
# axisTwo_ = dict(
#     R=860 + 0,
#     r=180 + 0,
#     L=840 + 0,
#     H=1820,
#     phi=0,
#     theta=0
# )
#
#
# axisThree_ = dict(
#     R=860 + 0,
#     r=180 + 0,
#     L=840 + 0,
#     H=1820,
#     phi=0,
#     theta=0
# )
#
#
# perfectDelta = Delta(arrAxis=[axisOne_, axisTwo_, axisThree_])
#
# command = [10, 20, 0]  # coordinate of a point
#
# arrLength = perfectDelta.inverseKinetic(*command)
# point = perfectDelta.forwardKinetic(*arrLength)
#
#
# print(point - command)  # error between forward and inverse kinetics
