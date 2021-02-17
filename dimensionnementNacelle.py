from algoParameters import findRadius, findUsefulHeight
from Analysis import VectorFunction

import numpy as np
from scipy.optimize import minimize

import plotly.graph_objects as go
import plotly.io as pio

pio.templates.default = "plotly_white"

# R = 790
# H = 1820
#
# targetR = 400
# targetH = 1200
#
# vecFunction = VectorFunction(coordinateFunctions=[lambda vec: -findRadius([R, vec[0], vec[1], H]) / targetR,
#                                                   lambda vec: -findUsefulHeight([R, vec[0], vec[1], H]) / targetH])
#
# nbPoints = 200
# arr_r = np.linspace(0, R, nbPoints)
# arr_L = np.linspace(0, H, nbPoints)
#
# arrRadius = []
#
# for L in arr_L:
#     row = []
#     for r in arr_r:
#         #row.append(findUsefulHeight([R, r, L, H]))
#         #row.append(findRadius([R, r, L, H]))
#         row.append((findRadius([R, r, L, H]) / targetR + findUsefulHeight([R, r, L, H]) / targetH) / 2)
#     arrRadius.append(row)
#
# fig = go.Figure(data=[go.Contour(x=arr_r, y=arr_L, z=arrRadius)])
#
# fig.update_layout(
#         title="Objectif exprimer en pourcentage",
#         xaxis_title="r en mm",
#         yaxis_title="L en mm",
#         font=dict(
#             family="Courier New, monospace"
#         )
#     )
#
# fig.show()


arrNacelleRadius = np.linspace(50, 250, 100)
arrWorkspaceRadius = []

for r in arrNacelleRadius:
    arrWorkspaceRadius.append(findRadius([720, r, 940, 1850]))


fig = go.Figure(data=[
    go.Scatter(x=arrNacelleRadius, y=arrWorkspaceRadius, marker=dict(color="#289C6F"))
])

fig.update_layout(
        title="Evolution du rayon de l'espace de travail",
        xaxis_title="r de la nacelle en mm",
        yaxis_title="r de l'espace de travail mm",
        font=dict(
            family="Courier New, monospace"
        )
    )

fig.show()


# def funcToMinimize(vec):
#     r = vec[0]
#     L = vec[1]
#
#     return -findRadius([R, r, L, H])
#
#
# res = minimize(funcToMinimize, np.array([170, 940]), method='nelder-mead',
#                options={'xatol': 1e-8, 'disp': True})
#
# print(res.x)

