from plateauNewSolution.newEquationMotion import L1, L2, L3, findDistanceTranslation, distTransMax, distTransMin

import numpy as np

import plotly.graph_objects as go
import plotly.io as pio

pio.templates.default = "plotly_white"


def mecaPossible1(vec, angles):
    if 0 <= L1(vec, [phi, theta]) <= 1000 and 0 <= L2(vec, [phi, theta]) <= 1000 and 0 <= L3(vec, [phi, theta]) <= 1000:
        return True

    return False


def mecaPossible2(vec, angles):
    for dist in findDistanceTranslation(vec, angles):
        if dist < distTransMin or dist > distTransMax:
            return False

    return True


vec = [0, 0, 100]
nbPoints = 500

arrPhi = np.linspace(-180, 179, nbPoints)
arrTheta = np.linspace(0, 90, nbPoints)

arrPossiblePhi = []
arrPossibleTheta = []


for theta in arrTheta:
    for phi in arrPhi:
        if mecaPossible1(vec, [phi, theta]) and mecaPossible2(vec, [phi, theta]):
            arrPossiblePhi.append(phi)
            arrPossibleTheta.append(theta)


# plot the graph
fig = go.Figure(data=[go.Scatter(x=arrPossiblePhi, y=arrPossibleTheta, mode="markers", marker=dict(color="#ffab40"))],
                layout=(dict(height=600, width=600)))

fig.update_layout(
    title="Configuration possible pour le point ({0}, {1}, {2}) ".format(*vec),
    xaxis_title="phi en deg",
    yaxis_title="theta en deg",
    font=dict(
        family="Courier New, monospace"
    )
)

fig.show()
