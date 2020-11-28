from plateauNewSolution.newEquationMotion import computeThinkness
from simulationNacelle.equationMotion import inWorkspace

import numpy as np

import plotly.graph_objects as go
import plotly.io as pio

pio.templates.default = "plotly_white"


nbPoints = 30

arrX = np.linspace(-500, 500, nbPoints)
arrY = np.linspace(-380, 530, nbPoints)

arrPossiblePhi = []
arrPossibleTheta = []

arrThinkness = []

z = 500
for y in arrY:
    row = []
    for x in arrX:
        row.append(computeThinkness([x, y, z]))
    arrThinkness.append(row)


# plot the graph
fig = go.Figure(data=[go.Contour(z=arrThinkness, x=arrX, y=arrY)],
                layout=(dict(height=600, width=600)))

fig.update_layout(
    title="bar thikness for points in z={0}".format(z),
    xaxis_title="X in mm",
    yaxis_title="Y in mm",
    font=dict(
        family="Courier New, monospace"
    )
)

fig.show()
