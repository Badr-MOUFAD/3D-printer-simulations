from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly.io as pio

import numpy as np

from simulationPlateau.equationMotionPlateau import R, Ry, Rz, axisLength

pio.templates.default = "plotly_white"


nbPoints = 1000

L1 = np.linspace(0, axisLength, 3)
L2 = np.linspace(0, axisLength, nbPoints)

arrY = []

for l1 in L1:
    y = []
    for l2 in L2:
        value = Ry([l1, l2, None])

        if value is None:
            break
        else:
            y.append(R - value)

    arrY.append(y)


fig = go.Figure(
    data=[
        go.Scatter(
            x=L2,
            y=arrY[i],
            name="pour L1 = {0:.2f}".format(L1[i])
        )
    for i in range(len(L1))]
)

fig.update_layout(
    title="Evolution of Y for different values of L1",
    xaxis_title="L2 in mm",
    yaxis_title="Y distance in mm",
    font=dict(
        family="Courier New, monospace"
    ),
    height=600,
    width=600
)


fig.show()

