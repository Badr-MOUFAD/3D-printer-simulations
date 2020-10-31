import numpy as np

import plotly.graph_objects as go
import plotly.io as pio

from simulationPlateau.equationMotionPlateau import axisLength, computeMaxY


pio.templates.default = "plotly_white"
nbPoints = 1000

L1 = np.linspace(0, axisLength, nbPoints)
maxY = []

for l1 in L1:
    maxY.append(computeMaxY(l1))


fig = go.Figure(data=[
    go.Scatter(x=L1, y=maxY)
])

fig.update_layout(
    title="Evolution of max distance Y",
    xaxis_title="L1 in mm",
    yaxis_title="max Y in mm",
    font=dict(
        family="Courier New, monospace"
    ),
    height=600,
    width=600
)

fig.show()
