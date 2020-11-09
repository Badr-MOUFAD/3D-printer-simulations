import numpy as np


class VectorFunction:
    def __init__(self, coordinateFunctions):
        self.y = coordinateFunctions
        return

    def __getitem__(self, coordinate):
        return self.y[coordinate]

    def __len__(self):
        return len(self.y)

    # def valueIn(self, x0):
    #     result = np.zeros(shape=(len(x0), 1))
    #     x = np.zeros(shape=(len(x0), 1))
    #
    #     for i in range(len(x0)):
    #         x[i] = x0[i]
    #
    #     for i in range(len(self)):
    #         result[i] = self.y[i](x)
    #
    #     return result

    def valueIn(self, x0):
        result = np.array([0 for i in range(len(x0))], dtype=float)
        x = np.array([0 for i in range(len(x0))], dtype=float)

        for i in range(len(x0)):
            x[i] = x0[i]

        for i in range(len(self)):
            result[i] = self.y[i](x)

        return result

    def partialDerivateIn(self, coordinate, variable, x0):
        f = self[coordinate]

        h = 10 ** -5

        # create an instance of x0
        vector = [*x0]
        vector[variable] += h

        return (f(vector) - f(x0)) / h

    def jacobienMatrix(self, x0):
        jacobien = np.zeros(shape=(len(self), len(x0)), dtype=float)

        for i in range(len(self)):
            for j in range(len(x0)):
                jacobien[i][j] = self.partialDerivateIn(i, j, x0)

        return jacobien


def algorithmNewtonRaphson(function, starting, precision):
    x0 = starting

    while True:
        if infinitNorm(function.valueIn(x0)) < precision:
            return x0
        else:
            Df = function.jacobienMatrix(x0)
            #print(infinitNorm(function.valueIn(x0)))
            #print(function.jacobienMatrix(x0))
            x1 = x0 - np.linalg.inv(Df).dot(function.valueIn(x0))

            x0 = np.array(x1)

    return


def euclidienNorm(vector):
    result = 0

    for coordinate in vector:
        result += coordinate ** 2

    return np.sqrt(result)


def infinitNorm(vector):
    return max(abs(vector))


def firstNorm(vector):
    sum = 0

    for coordinate in vector:
        sum += abs(coordinate)

    return sum
