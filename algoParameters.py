import numpy as np
from continuousBinarySearch import findSearchingInterval, ContinuousBinarySearch
from Analysis import VectorFunction

import plotly.graph_objects as go
import plotly.io as pio

pio.templates.default = "plotly_white"

from scipy.optimize import minimize


def findRadius(vec):

    # -------- constant ------- #
    R = vec[0]  # R_  # diameter of chassis
    r = vec[1]  # r_  # diameter of nacelle
    L = vec[2]  # L_  # length of arms
    H = vec[3]  # H_  # height of robot

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
    if r < 0 or R < 0 or L < 0 or H < 0:
        return 0
    if r > R:
        return 0
    if L < R - r:
        return 0
    if H < np.sqrt(L ** 2 - DR ** 2):
        return 0

    # find radius
    intervalMinus = findSearchingInterval(0, inWorkspace, direction="negative")
    radiusMinus = -ContinuousBinarySearch(interval=intervalMinus, func=inWorkspace)

    intervalPlus = findSearchingInterval(0, inWorkspace, direction="positive")
    radiusPlus = ContinuousBinarySearch(interval=intervalPlus, func=inWorkspace, direction="positive")

    return min(radiusPlus, radiusMinus)


def gradientFindRadius(vec):
    scalerFunction = VectorFunction(coordinateFunctions=[findRadius])

    return scalerFunction.jacobienMatrix(vec)[0]


def hessFindRadius(vec):
    scalerFunction = VectorFunction(coordinateFunctions=[findRadius])

    def partialDerivative(variable):
        def f(x):
            return scalerFunction.partialDerivateIn(0, variable, x)
        return f

    coordinateFunctions = [partialDerivative(i) for i in range(len(vec))]

    gradientFunction = VectorFunction(coordinateFunctions=coordinateFunctions)

    return gradientFunction.jacobienMatrix(vec)


# example
# H__ = 1820
# R__ = 860
# r__ = 180
# L__ = 840
#

# dim = [860, 180, 860, 1820]
#
# #print(findRadius(dim))  # [860, 180, 840, 1820]
# print(gradientFindRadius(dim))
# print("*****")
# print(hessFindRadius(dim))


# R__ = np.linspace(180, 840 + 180, 400)
# workspaceRadius = []
#
# for rad in R__:
#     workspaceRadius.append(findRadius([rad, 180, 840, 1820]))
#
# fig = go.Figure(data=[
#     go.Scatter(x=R__, y=workspaceRadius)
# ])
#
# fig.update_layout(
#     title="radius of working space",
#     font=dict(
#         family="Courier New, monospace"
#     ),
#     height=600,
#     width=600
# )
#


# L__ = np.linspace(860 - 180, 1820, 400)
# workspaceRadius = []
#
# for armLength in L__:
#     workspaceRadius.append(findRadius([860, 180, armLength, 1500]))
#
# fig = go.Figure(data=[
#     go.Scatter(x=L__, y=workspaceRadius)
# ])
#
# fig.update_layout(
#     title="radius of working space",
#     font=dict(
#         family="Courier New, monospace"
#     ),
#     height=600,
#     width=600
# )
#
# fig.show()


# H__ = np.linspace(0, 2000, 400)
# workspaceRadius = []
#
# for height in H__:
#     workspaceRadius.append(findRadius([860, 180, 840, height]))
#
# fig = go.Figure(data=[
#     go.Scatter(x=H__, y=workspaceRadius)
# ])
#
# fig.update_layout(
#     title="radius of working space",
#     font=dict(
#         family="Courier New, monospace"
#     ),
#     height=600,
#     width=600
# )

#fig.show()

#
# r__ = np.linspace(0, 860, 400)
# workspaceRadius = []
#
# for small_r in r__:
#     workspaceRadius.append(findRadius([860, small_r, 840, 1850]))
#
# fig = go.Figure(data=[
#     go.Scatter(x=r__, y=workspaceRadius)
# ])
#
# fig.update_layout(
#     title="radius of working space",
#     font=dict(
#         family="Courier New, monospace"
#     ),
#     height=600,
#     width=600
# )
#
# fig.show()

#
# import time
#
# target = 400
#
#
# def funcToMinimize(vec):
#     return (findRadius(vec) - target) ** 2
#
#
# startMoment = time.time()
#
# res = minimize(funcToMinimize, np.array([target, target / 3, target, 5 * target]), method='nelder-mead',
#                options={'xatol': 1e-8, 'disp': True})
#
# endMoment = time.time()
#
# print("dimensions   : {0}".format(res.x))
# print("actual error : {0}".format(abs(target - findRadius(res.x))))
# print("running time : {0}".format(endMoment - startMoment))
