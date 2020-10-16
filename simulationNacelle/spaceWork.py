import plotly.graph_objects as go
import plotly.io as pio

pio.templates.default = "plotly_white"

import numpy as np

from simulationNacelle.equationMotion import L1, L2, L3


xLim = 200
yLim = 200
nbPoints = 400

# simulation for z = 0
z = 0
workSpace = []

x = np.linspace(-xLim, xLim, nbPoints)
y = np.linspace(-yLim, yLim, nbPoints)

for i in range(nbPoints):
    row = []

    for j in range(nbPoints):
        valueL1 = L1(y[j], x[i], z)
        valueL2 = L2(y[j], x[i], z)
        valueL3 = L3(y[j], x[i], z)

        if None in [valueL1, valueL2, valueL3]:
            row.append(None)
        else:
            row.append(10)

    workSpace.append(row)


fig = go.Figure(data=go.Heatmap(
    z=workSpace,
    x=y,
    y=x
), layout=(dict(width=600, height=600)))


fig.show()
