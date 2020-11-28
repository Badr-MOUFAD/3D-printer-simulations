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
    go.Scatter(x=arrPhi, y=arrDisAxisA, name="axis 1"),
    go.Scatter(x=arrPhi, y=arrDisAxisB, name="axis 2"),
    go.Scatter(x=arrPhi, y=arrDisAxisC, name="axis 3"),
    go.Scatter(x=arrPhi, y=[0 for phi in arrPhi], marker=dict(color="gray"), showlegend=False)
                      ])

fig.update_layout(
    title="translation distance for theta={0}".format(theta),
    xaxis_title="phi in deg",
    yaxis_title="distance trans in mm",
    font=dict(
        family="Courier New, monospace"
    )
)

fig.show()
