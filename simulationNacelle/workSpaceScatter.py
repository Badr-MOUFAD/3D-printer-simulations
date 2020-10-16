import plotly.graph_objects as go
import plotly.io as pio

import numpy as np

from simulationNacelle.equationMotion import L1, L2, L3, belowD1, belowD2, aboveD3, u1, u2, u3

pio.templates.default = "plotly_white"


xLim = 300
yLim = 300
nbPoints = 400

# simulation for z = 0
z = 0# H - (np.sqrt(L ** 2 - DR ** 2) + 100)
xWorkSpace = []
yWorkSpace = []

x = np.linspace(-xLim, xLim, nbPoints)
y = np.linspace(-yLim, yLim, nbPoints)

for i in range(nbPoints):
    for j in range(nbPoints):
        # checking the corners of the end effector are within the limits
        if not belowD1(x[i] + u1[0], y[j] + u1[1]):
            continue

        if not belowD2(x[i] + u2[0], y[j] + u2[1]):
            continue

        if not aboveD3(x[i] + u3[0], y[j] + u3[1]):
            continue

        # checking x, y are reachable
        valueL1 = L1(x[i], y[j], z)
        valueL2 = L2(x[i], y[j], z)
        valueL3 = L3(x[i], y[j], z)

        if None not in [valueL1, valueL2, valueL3]:
            xWorkSpace.append(x[i])
            yWorkSpace.append(y[j])


fig = go.Figure(data=go.Scatter(x=xWorkSpace, y=yWorkSpace, mode='markers'), layout=(dict(height=600, width=600)))

fig.update_layout(
    title="Delta Robot Working Space",
    xaxis_title="X in mm",
    yaxis_title="Y in mm",
    font=dict(
        family="Courier New, monospace"
    )
)

fig.show()
