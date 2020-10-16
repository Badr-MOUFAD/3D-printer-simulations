import plotly.graph_objects as go
import plotly.io as pio

import numpy as np

from simulationPlateau.equationMotionPlateau import R, axisLength, computeNormal

pio.templates.default = "plotly_white"


nbPoints = 10

L1 = np.linspace(0, axisLength, nbPoints)
L2 = np.linspace(0, axisLength, nbPoints)
L3 = np.linspace(0, axisLength, nbPoints)

x = [0]
y = [0]
z = [0]

for l2 in L2:
    for l3 in L3:
        normal = computeNormal([500, l2, l3])

        x.append(normal[0]); x.append(0)
        y.append(normal[1]); y.append(0)
        z.append(normal[2]); z.append(0)


fig = go.Figure(
    data=[
        go.Scatter3d(
            x=x, y=y, z=z,
            line=dict(
                width=1,
            ),
            surfaceaxis=0
        )
    ]
)

fig.update_layout(
    title="Different position of the normal vector for L1 = 500mm",
    font=dict(
        family="Courier New, monospace"
    ),
    height=600,
    width=600
)


fig.show()
