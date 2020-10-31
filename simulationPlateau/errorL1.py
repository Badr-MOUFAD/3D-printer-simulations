import numpy as np

import plotly.graph_objects as go
import plotly.io as pio

from simulationPlateau.equationMotionPlateau import axisLength, precisionAngles


pio.templates.default = "plotly_white"
nbPoints = 100

L1 = np.linspace(0, axisLength, nbPoints)
L2 = np.linspace(0, axisLength, 20)
L3 = np.linspace(0, axisLength, 20)

arrError = []

for l1 in L1:
    error = []

    for l2 in L2:
        for l3 in L3:
            error.append(precisionAngles([l1, l2, l3]))

    arrError.append(max(error))


fig = go.Figure(data=[
    go.Scatter(x=L1, y=arrError)
])


fig.update_layout(
    title="max error for each L1",
    xaxis_title="L1 in mm",
    yaxis_title="Error in deg",
    font=dict(
        family="Courier New, monospace"
    ),
    height=600,
    width=600
)


fig.show()