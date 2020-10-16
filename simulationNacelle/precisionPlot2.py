import plotly.graph_objects as go
import plotly.io as pio

import numpy as np

from simulationNacelle.equationMotion import L1, L2, L3, belowD1, belowD2, aboveD3, u1, u2, u3, calculatePrecision

pio.templates.default = "plotly_white"


xLim = 200
yLim = 200
nbPoints = 200

# simulation for z = 0
z = 0
precisionArr = []

x = np.linspace(-xLim, xLim, nbPoints)
y = np.linspace(-yLim, yLim, nbPoints)

for i in range(nbPoints):
    row = []

    for j in range(nbPoints):
        # checking the corners of the end effector are within the limits
        if not belowD1(x[j] + u1[0], y[i] + u1[1]):
            row.append(None)
            continue

        if not belowD2(x[j] + u2[0], y[i] + u2[1]):
            row.append(None)
            continue

        if not aboveD3(x[j] + u3[0], y[i] + u3[1]):
            row.append(None)
            continue

        # checking x, y are reachable
        valueL1 = L1(x[j], y[i], z)
        valueL2 = L2(x[j], y[i], z)
        valueL3 = L3(x[j], y[i], z)

        if None not in [valueL1, valueL2, valueL3]:
            row.append(calculatePrecision(x[j], y[i], z))
        else:
            row.append(None)

    precisionArr.append(row)


fig = go.Figure(data=go.Contour(z=precisionArr, x=x, y=y), layout=(dict(height=600, width=600)))

fig.update_layout(
    title="Delta Robot precision",
    xaxis_title="X in mm",
    yaxis_title="Y in mm",
    font=dict(
        family="Courier New, monospace"
    )
)

fig.show()
