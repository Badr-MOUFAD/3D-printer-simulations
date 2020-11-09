import numpy as np
from Analysis import VectorFunction, euclidienNorm, infinitNorm, algorithmNewtonRaphson

# constant
# H = 1200  # height of the robot
# L = 210  # 244  # arm length
#
# R = 225.61  # distance from a leg to the center
# r = 60  # radius of the end effector

H = 1820
R = 860
r = 180
L = 840

dR = 0
dl1 = 0
dl2 = 0

# precision
dL = 1.8
dx = 1

cosPi3 = np.cos(np.pi / 3)
sinPi3 = np.sin(np.pi / 3)

DR = R - r


def L1_(x):
    term = ((DR + dR) * sinPi3 + x[0]) ** 2 + ((DR + dR) * cosPi3 + x[1]) ** 2

    if L ** 2 < term:
        return None

    result = x[2] + np.sqrt((L + dl1) ** 2 - term)

    if result > H:
        return None

    return result


def L2_(x):
    term = (-DR * sinPi3 + x[0]) ** 2 + (DR * cosPi3 + x[1]) ** 2

    if L ** 2 < term:
        return None

    result = x[2] + np.sqrt((L + dl2) ** 2 - term)

    if result > H:
        return None

    return result


def L3_(x):
    term = x[0] ** 2 + (-DR + x[1]) ** 2

    if L ** 2 < term:
        return None

    result = x[2] + np.sqrt(L ** 2 - term)

    if result > H:
        return None

    return result


def findCoordinate(L1, L2, L3):
    def f1(x):
        term = (DR * sinPi3 + x[0]) ** 2 + (DR * cosPi3 + x[1]) ** 2

        result = x[2] + np.sqrt((L + dl1) ** 2 - term)

        return result - L1

    def f2(x):
        term = (-DR * sinPi3 + x[0]) ** 2 + (DR * cosPi3 + x[1]) ** 2

        result = x[2] + np.sqrt((L + dl2) ** 2 - term)

        return result - L2

    def f3(x):
        term = x[0] ** 2 + (-DR + x[1]) ** 2

        result = x[2] + np.sqrt(L ** 2 - term)

        return result - L3

    # resolution
    systemFunction = VectorFunction(coordinateFunctions=[f1, f2, f3])
    solution = algorithmNewtonRaphson(function=systemFunction, starting=np.array([0, 0, min(L1, L2, L3)]), precision=10**-2)

    #print(systemFunction.valueIn([90.59, 50.86,   10.87]))
    return solution


# x_ = [0, 0, 0]
# arrL = [L1_(x_), L2_(x_), L3_(x_)]
#
# print("the inputs coordinate: {0}".format(x_))
# print("numeric solution: {0}".format(findCoordinate(*arrL)))


print(findCoordinate(*[450.153, 493.153, 493.15]))
#[493.15312024 493.15312024 493.15312024]
