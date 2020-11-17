import plotly.graph_objects as go
import plotly.io as pio

import numpy as np

from simulationPlateau.equationMotionPlateau import Ry, Rz, axisLength
from simulationPlateauNacelle.inverseKinematicPlateau import L1, L2, L3

pio.templates.default = "plotly_white"


def inRangeLength(L):
    for length in L:
        if length < 0 or length > axisLength:
            return False

    return True


z = 500
point = [0, 0, z]

anglePhi = np.linspace(-180, 180, 500)
angleTheta = np.linspace(0, 90, 500)

reachablePhi = []
reachableTheta = []

for theta in angleTheta:
    for phi in anglePhi:
        angle = [phi, theta]

        l1 = L1(point, angle)
        L = [L1(point, angle), L2(angle, l1), L3(angle, l1)]

        if None in L:
            continue

        if not inRangeLength(L):
            continue

        if None in [Ry(L), Rz(L)]:
            continue
        else:
            reachablePhi.append(phi)
            reachableTheta.append(theta)


fig = go.Figure(
    data=[
        go.Scatter(
            x=reachablePhi, y=reachableTheta, mode="markers"
        )
    ]
)

fig.update_layout(
    title="Inclinaison atteignable pour (0, 0, {0:.2f})".format(z),
    font=dict(
        family="Courier New, monospace"
    ),
    xaxis_title="angle Phi en deg",
    yaxis_title="angle theta en deg",
    height=600,
    width=600
)


fig.show()
