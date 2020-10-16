import numpy as np


# constant
H = 1200  # height of the robot
L = 244  # arm length

R = 225.61  # distance from a leg to the center
r = 60  # radius of the end effector

# precision
dL = 1.8

cosPi3 = np.cos(np.pi / 3)
sinPi3 = np.sin(np.pi / 3)

DR = R - r


def calculatePrecision(x, y, z):
    term1 = np.sqrt(L ** 2 - (DR * sinPi3 + x) ** 2 - (DR * cosPi3 + y) ** 2)
    term2 = np.sqrt(L ** 2 - (-DR * sinPi3 + x) ** 2 - (DR * cosPi3 + y) ** 2)
    term3 = np.sqrt(L ** 2 - x ** 2 - (-DR + y) ** 2)

    matrix = np.array([[1, -(DR * sinPi3 + x) / term1, -(DR * cosPi3 + y) / term1],
                       [1, (DR * sinPi3 + x) / term2, -(DR * cosPi3 + y) / term2],
                       [1, -x / term3, (DR + y) / term3]],
                      dtype=float)

    try:
        subPrecisions = np.dot(np.linalg.inv(matrix), np.array([dL, dL, dL], dtype=float))

        return np.sqrt(subPrecisions[0] ** 2 + subPrecisions[1] ** 2 + subPrecisions[2] ** 2)
    except:
        return None


print(calculatePrecision(0, 0, 0))
