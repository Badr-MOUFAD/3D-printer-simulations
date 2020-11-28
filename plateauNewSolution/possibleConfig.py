from plateauNewSolution.newEquationMotion import L1, L2, L3

import numpy as np

import plotly.graph_objects as go
import plotly.io as pio

pio.templates.default = "plotly_white"


vec = [0, 0, 100]
nbPoints = 100

arrPhi = np.linspace(-180, 179, nbPoints)
arrTheta = np.linspace(0, 90, nbPoints)

arrPossiblePhi = []
arrPossibleTheta = []


for theta in arrTheta:
    for phi in arrPhi:
        if 0 <= L1(vec, [phi, theta]) <= 1000 and 0 <= L2(vec, [phi, theta]) <= 1000 and 0 <= L3(vec, [phi, theta]) <= 1000:
            arrPossiblePhi.append(phi)
            arrPossibleTheta.append(theta)


# plot the graph
fig = go.Figure(data=[go.Scatter(x=arrPossiblePhi, y=arrPossibleTheta, mode="markers")],
                layout=(dict(height=600, width=600)))

fig.update_layout(
    title="possible configurations for ({0}, {1}, {2}) ".format(*vec),
    xaxis_title="phi in deg",
    yaxis_title="theta in deg",
    font=dict(
        family="Courier New, monospace"
    )
)

fig.show()
