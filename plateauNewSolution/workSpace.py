from plateauNewSolution.newEquationMotion import computeThinkness
from simulationNacelle.equationMotion import inWorkspace

import numpy as np

import plotly.graph_objects as go
import plotly.io as pio

pio.templates.default = "plotly_white"


nbPoints = 10

arrX = np.linspace(-400, 400, nbPoints)
arrY = np.linspace(-400, 400, nbPoints)

arrThinkness = []

z = 100
for y in arrY:
    row = []
    for x in arrX:
        row.append(computeThinkness([x, y, z]))

        print([x, y, z])
    arrThinkness.append(row)


# plot the graph
fig = go.Figure(data=[go.Contour(z=arrThinkness, x=arrX, y=arrY)],
                layout=(dict(height=600, width=600)))

fig.update_layout(
    title="largeur de la bande pour le plan z={0}".format(z),
    xaxis_title="X en mm",
    yaxis_title="Y en mm",
    font=dict(
        family="Courier New, monospace"
    )
)

fig.show()
