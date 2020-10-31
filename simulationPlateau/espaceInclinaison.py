from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly.io as pio

import numpy as np

from simulationPlateau.equationMotionPlateau import R, axisLength, computeAngles, Ry, Rz

pio.templates.default = "plotly_white"


nbPoints = 1000

L1 = np.linspace(0, axisLength)
L2 = np.linspace(0, axisLength)
L3 = np.linspace(0, axisLength)

alpha = []
beta = []
gamma = []

l1 = 0

for l2 in L2:
    rowAlpha = []
    rowBeta = []
    rowGamma = []

    for l3 in L3:
        if Ry([l1, l2, l3]) is None or Rz([l1, l2, l3]) is None:
            angles = [None, None, None]
        else:
            angles = computeAngles([l1, l2, l3])

        rowAlpha.append(angles[0])
        rowBeta.append((angles[1]))
        rowGamma.append(angles[2])

    alpha.append(rowAlpha)
    beta.append(rowBeta)
    gamma.append(rowGamma)


fig = make_subplots(rows=1, cols=3,
                    subplot_titles=["Tilting between x_axis / normal",
                                    "Tilting between y_axis / normal",
                                    "Tilting between z_axis / normal"])

fig.add_trace(
    go.Contour(z=np.transpose(alpha), x=L2, y=L3, showscale=False,
               contours=dict(showlabels=True, labelfont=dict(size=12, color='white'))
    ),
    row=1, col=1
)

fig.add_trace(
    go.Contour(z=np.transpose(beta), x=L2, y=L3, showscale=False,
               contours=dict(showlabels=True, labelfont=dict(size=12, color='white'))
    ),
    row=1, col=2
)

fig.add_trace(
    go.Contour(z=np.transpose(gamma), x=L2, y=L3, showscale=False,
               contours=dict(showlabels=True, labelfont=dict(size=12, color='white'))
    ),
    row=1, col=3
)

fig.update_xaxes(title_text="L2 in mm", row=1, col=1)
fig.update_xaxes(title_text="L2 in mm", row=1, col=2)
fig.update_xaxes(title_text="L2 in mm", row=1, col=3)

fig.update_yaxes(title_text="L3 in mm", row=1, col=1)
fig.update_yaxes(title_text="L3 in mm", row=1, col=2)
fig.update_yaxes(title_text="L3 in mm", row=1, col=3)


fig.update_layout(
    title="Space of tilt (in deg°)",
    font=dict(
        family="Courier New, monospace"
    )
)

fig.show()
