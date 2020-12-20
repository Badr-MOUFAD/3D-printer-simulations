from plateauNewSolution.newEquationMotion import findDistanceTranslation

import numpy as np

import plotly.graph_objects as go
import plotly.io as pio

pio.templates.default = "plotly_white"


nbPoints = 100
arrPhi = np.linspace(-180, 179, nbPoints)


arrDisAxisA = []
arrDisAxisB = []
arrDisAxisC = []

vec = [0, 0, 0]
theta = 16.5
for phi in arrPhi:
    disA, disB, disC = findDistanceTranslation(vec, [phi, theta])

    arrDisAxisA.append(disA)
    arrDisAxisB.append(disB)
    arrDisAxisC.append(disC)


fig = go.Figure(data=[
    go.Scatter(x=arrPhi, y=arrDisAxisA, name="AA'", marker=dict(color="#ffab40")),
    go.Scatter(x=arrPhi, y=arrDisAxisB, name="BB'", marker=dict(color="#85d5e6")),
    go.Scatter(x=arrPhi, y=arrDisAxisC, name="CC'", marker=dict(color="#001633")),
    go.Scatter(x=arrPhi, y=[0 for phi in arrPhi], marker=dict(color="gray"), showlegend=False)
                      ])

fig.update_layout(
    title="Distance de translation pour theta={0}".format(theta),
    xaxis_title="phi en deg",
    yaxis_title="distance en mm",
    font=dict(
        family="Courier New, monospace"
    )
)

fig.show()
