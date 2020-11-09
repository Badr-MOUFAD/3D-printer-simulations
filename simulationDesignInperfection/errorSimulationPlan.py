from simulationDesignInperfection.deltaGlobalEquation import Delta
from Analysis import euclidienNorm

import numpy as np
import plotly.graph_objects as go
import plotly.figure_factory as ff
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
Z = 0

vecX = []
vecY = []

z = Z
for y in Y:
    rowVecX = []
    rowVecY = []

    for x in X:
        desiredPoint = np.array([x, y, z], dtype=float)
        arrLength = perfectDelta.inverseKinetic(x, y, z)
        reachedPoint = imperfectDelta.forwardKinetic(*arrLength)

        rowVecX.append(reachedPoint[0] - desiredPoint[0])
        rowVecY.append(reachedPoint[1] - desiredPoint[1])

    vecX.append(rowVecX)
    vecY.append(rowVecY)


arrX, arrY = np.meshgrid(X, Y)

fig = ff.create_quiver(x=arrX, y=arrY, u=vecX, v=vecY, scale=0.1,
                       arrow_scale=.4,
                       name='quiver',
                       line_width=1)

fig.update_layout(
    title="Error in plan Z = 0",
    xaxis_title="X in mm",
    yaxis_title="Y in mm",
    font=dict(
        family="Courier New, monospace"
    )
)

fig.show()
