import numpy as np

import plotly.graph_objects as go
import plotly.io as pio

from simulationPlateau.equationMotionPlateau import axisLength, precisionAngles


pio.templates.default = "plotly_white"
nbPoints = 100

L1 = np.linspace(0, axisLength, nbPoints)
L2 = np.linspace(0, axisLength, nbPoints)
L3 = np.linspace(0, axisLength, nbPoints)

arrPrecision = []


for l1 in [500]:
    for l2 in L2:
        row = []
        for l3 in L3:
            row.append(precisionAngles([l1, l2, l3]))

        arrPrecision.append(row)

fig = go.Figure(data=[
    go.Contour(x=L2, y=L3, z=np.transpose(arrPrecision))
])

fig.update_layout(
    title="Evolution of Y for different values of L1",
    xaxis_title="L2 in mm",
    yaxis_title="L3 in mm",
    font=dict(
        family="Courier New, monospace"
    ),
    height=600,
    width=600
)

fig.show()
