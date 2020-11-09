from simulationDesignInperfection.deltaGlobalEquation import Delta
from Analysis import euclidienNorm

import numpy as np
import plotly.graph_objects as go
import plotly.io as pio

pio.templates.default = "plotly_white"


axisOne_ = dict(
    R=725,
    r=175.5,
    L=940,
    H=1820,
    phi=0.0349,
    theta=1.588,
)

axisTwo_ = dict(
    R=765,
    r=163.5,
    L=941,
    H=1820,
    phi=0.017,
    theta=1.605
)


axisThree_ = dict(
    R=700,
    r=174.5,
    L=940,
    H=1820,
    phi=-0.017,
    theta=1.588
)


axisOne = dict(
    R=730,
    r=170,
    L=940,
    H=1820,
    phi=0,
    theta=np.pi / 2,
)

axisTwo = dict(
    R=730,
    r=170,
    L=940,
    H=1820,
    phi=0,
    theta=np.pi / 2,
)

axisThree = dict(
    R=730,
    r=170,
    L=940,
    H=1820,
    phi=0,
    theta=np.pi / 2,
)

perfectDelta = Delta(arrAxis=[axisOne, axisTwo, axisThree])
imperfectDelta = Delta(arrAxis=[axisOne_, axisTwo_, axisThree_])


nbPoints = 20

X = np.linspace(-100, 100, nbPoints)
Y = np.linspace(-50, 50, nbPoints)
Z = 1000

arrError = []

z = Z
for y in Y:
    row = []

    for x in X:
        desiredPoint = np.array([x, y, z], dtype=float)
        arrLength = perfectDelta.inverseKinetic(x, y, z)
        reachedPoint = imperfectDelta.forwardKinetic(*arrLength)

        #row.append(euclidienNorm(desiredPoint - reachedPoint))
        row.append(abs(desiredPoint[2] - reachedPoint[2]))

    arrError.append(row)


fig = go.Figure(data=go.Contour(z=np.transpose(arrError), x=X, y=Y), layout=(dict(height=600, width=600)))

fig.update_layout(
    title="Error in Z axis",
    xaxis_title="X in mm",
    yaxis_title="Y in mm",
    font=dict(
        family="Courier New, monospace"
    )
)

fig.show()

# print(imperfectDelta.inverseKinetic(0, 0, 950))
# print(imperfectDelta.inverseKinetic(100, -200, 950))