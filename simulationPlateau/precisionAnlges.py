import numpy as np

import plotly.graph_objects as go
import plotly.io as pio

from simulationPlateau.equationMotionPlateau import axisLength, precisionAngles


pio.templates.default = "plotly_white"
nbPoints = 50

L1 = np.linspace(0, axisLength, nbPoints)
L2 = np.linspace(0, axisLength, nbPoints)
L3 = np.linspace(0, axisLength, nbPoints)

arrPrecision = []
X = []
Y = []
Z = []

for l1 in L1:
    for l2 in L2:
        for l3 in L3:
            X.append(l1)
            Y.append(l2)
            Z.append(l3)

            arrPrecision.append(precisionAngles([l1, l2, l3]))


fig = go.Figure(data=go.Volume(
    x=X,
    y=Y,
    z=Z,
    value=arrPrecision,
    opacity=0.3,
    surface_count=18,
    ))

# fig.update_layout(
#     title="Evolution of max distance Y",
#     xaxis_title="L1 in mm",
#     yaxis_title="L2 in mm",
#     zaxis_title="L3 in mm",
#     font=dict(
#         family="Courier New, monospace"
#     ),
#     height=600,
#     width=600
# )

fig.show()
