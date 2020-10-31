
def findRadius(R_, r_, L_, H_):
    import numpy as np
    from continuousBinarySearch import findSearchingInterval, ContinuousBinarySearch

    # -------- constant ------- #
    R = R_  # diameter of chassis
    r = r_  # diameter of nacelle
    H = H_  # height of robot
    L = L_  # length of arms

    cosPi3 = np.cos(np.pi / 3)
    sinPi3 = np.sin(np.pi / 3)

    DR = R - r

    # translation
    h = r * cosPi3
    u1 = (-h * sinPi3, h * cosPi3)
    u2 = (h * sinPi3, h * cosPi3)
    u3 = (0, -h)

    # --------- equation of motion ------- #
    def L1(x, y, z):
        term = ((DR) * sinPi3 + x) ** 2 + (DR * cosPi3 + y) ** 2

        if L ** 2 < term:
            return None

        result = z + np.sqrt(L ** 2 - term)

        if result > H:
            return None

        return result

    def L2(x, y, z):
        term = (-DR * sinPi3 + x) ** 2 + (DR * cosPi3 + y) ** 2

        if L ** 2 < term:
            return None

        result = z + np.sqrt(L ** 2 - term)

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

    # ----- constraint ------ #
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

    # ------- function: ------- #
    def inWorkspace(y, x=0, z=0):
        # checking the corners of the end effector are within the limits
        if not belowD1(x + u1[0], y + u1[1]):
            return False
        if not belowD2(x + u2[0], y + u2[1]):
            return False
        if not aboveD3(x + u3[0], y + u3[1]):
            return False
        # checking x, y are reachable
        valueL1 = L1(x, y, z)
        valueL2 = L2(x, y, z)
        valueL3 = L3(x, y, z)

        if None not in [valueL1, valueL2, valueL3]:
            return True

        return False

    # condition on parameters
    if r > R:
        return 0
    if L < R - r:
        return 0
    if H < L:
        return 0

    # find radius
    interval = findSearchingInterval(0, inWorkspace, direction="negative")
    radius = -ContinuousBinarySearch(interval=interval, func=inWorkspace)

    return radius


# example
# H__ = 1820
# R__ = 860
# r__ = 180
# L__ = 840
#
# print(findRadius(R__, r__, L__, H__))
