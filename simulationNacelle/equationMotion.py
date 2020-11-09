import numpy as np
from Analysis import VectorFunction, euclidienNorm, infinitNorm

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

# translation
h = r * cosPi3
u1 = (-h * sinPi3, h * cosPi3)
u2 = (h * sinPi3, h * cosPi3)
u3 = (0, -h)


def L1(x, y, z):
    term = ((DR + dR) * sinPi3 + x) ** 2 + ((DR + dR) * cosPi3 + y) ** 2

    if L ** 2 < term:
        return None

    result = z + np.sqrt((L + dl1) ** 2 - term)

    if result > H:
        return None

    return result


def L2(x, y, z):
    term = (-DR * sinPi3 + x) ** 2 + (DR * cosPi3 + y) ** 2

    if L ** 2 < term:
        return None

    result = z + np.sqrt((L + dl2) ** 2 - term)

    if result > H:
        return None

    return result


def L3(x, y, z):
    term = x ** 2 + (-DR + y) ** 2

    if L ** 2 < term:
        return None

    result = z + np.sqrt(L ** 2 - term)

    if result > H:
        return None

    return result


def belowD1(x, y):
    if (cosPi3 + 1) / sinPi3 * x + R > y:
        return True

    return False


def belowD2(x, y):
    if -(cosPi3 + 1) / sinPi3 * x + R > y:
        return True

    return False


def aboveD3(x, y):
    if y > - R * cosPi3:
        return True

    return False


def calculatePrecision(x, y, z):
    # term1 = np.sqrt(L ** 2 - (DR * sinPi3 + x) ** 2 - (DR * cosPi3 + y) ** 2)
    # term2 = np.sqrt(L ** 2 - (-DR * sinPi3 + x) ** 2 - (DR * cosPi3 + y) ** 2)
    # term3 = np.sqrt(L ** 2 - x ** 2 - (-DR + y) ** 2)

    matrix = np.array([[-(DR * sinPi3 + x) / np.sqrt(L ** 2 - (DR * sinPi3 + x) ** 2 - (DR * cosPi3 + y) ** 2), -(DR * cosPi3 + y) / np.sqrt(L ** 2 - (DR * sinPi3 + x) ** 2 - (DR * cosPi3 + y) ** 2), 1],
                       [(DR * sinPi3 + x) / np.sqrt(L ** 2 - (-DR * sinPi3 + x) ** 2 - (DR * cosPi3 + y) ** 2), -(DR * cosPi3 + y) / np.sqrt(L ** 2 - (-DR * sinPi3 + x) ** 2 - (DR * cosPi3 + y) ** 2), 1],
                       [-x / np.sqrt(L ** 2 - x ** 2 - (-DR + y) ** 2), (DR + y) / np.sqrt(L ** 2 - x ** 2 - (-DR + y) ** 2), 1]],
                      dtype=float)

    try:
        # vec = np.array([0, dL, dL])
        #
        # return euclidienNorm(np.dot(np.linalg.inv(matrix), vec))

        # checking all the possibilities
        maxPrecsion = []

        for dl in gen_dL():
            precision = infinitNorm(np.dot(np.linalg.inv(matrix), dl))

            maxPrecsion.append(precision)

        return max(maxPrecsion)
    except:
        return None


def calcultePrecision2(x, y):
    term1 = np.sqrt(L ** 2 - (DR * sinPi3 + x) ** 2 - (DR * cosPi3 + y) ** 2)
    term2 = np.sqrt(L ** 2 - (-DR * sinPi3 + x) ** 2 - (DR * cosPi3 + y) ** 2)
    term3 = np.sqrt(L ** 2 - x ** 2 - (-DR + y) ** 2)

    matrix = np.array([[-(DR * sinPi3 + x) / term1, -(DR * cosPi3 + y) / term1, 1],
                       [(DR * sinPi3 + x) / term2, -(DR * cosPi3 + y) / term2, 1],
                       [-x / term3, (DR + y) / term3, 1]],
                      dtype=float)

    arrLength = []

    for dl in gen_dL(dx):
        arrLength.append(min(abs(np.dot(matrix, dl))))

    return min(arrLength)


def gen_dL(dist=dL):
    result = []

    for i in [-1, 1, 0]:
        for j in [-1, 1, 0]:
            for k in [-1, 1, 0]:
                result.append(np.array([i * dist, j * dist, k * dist], dtype=float))

    # excluding the last element [0, 0, 0]
    result.pop()
    return result


def calculatePrecision3(x, y, z):
    vectorFunction = VectorFunction([L1_, L2_, L3_])

    x0 = [x, y, z]
    matrix = np.linalg.inv(vectorFunction.jacobienMatrix(x0))

    arrPrecision = []

    for dl in gen_dL():
        precision = euclidienNorm(np.dot(matrix, dl))

        arrPrecision.append(precision)

    return max(arrPrecision)


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


# point = [10, 20, 50]
# print([L1(*point), L2(*point), L3(*point)])
