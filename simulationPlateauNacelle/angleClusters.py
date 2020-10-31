import numpy as np
import plotly.graph_objects as go
import plotly.io as pio

from simulationPlateau.equationMotionPlateau import computePhi

pio.templates.default = "plotly_white"

nbPoints = 400

L1 = 500
L2 = np.linspace(0, 1000, nbPoints)
L3 = np.linspace(0, 1000, nbPoints)

arrAngles = []

for l2 in L2:
    row = []

    for l3 in L3:
        row.append(computePhi([L1, l2, l3]))

    arrAngles.append(row)


fig = go.Figure(data=[
    go.Contour(z=np.transpose(arrAngles), x=L1 - L2, y=L1 - L3),
    go.Scatter(x=L1 - L2, y=[0 for element in L2], marker_color="white"),
    go.Scatter(x=[0 for element in L3], y=L1 - L3, marker_color="white")
])


fig.update_layout(
    title="angle clusters",
    font=dict(
        family="Courier New, monospace"
    ),
    height=600,
    width=600
)

fig.show()
