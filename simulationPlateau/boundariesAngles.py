import numpy as np

from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly.io as pio

from simulationPlateau.equationMotionPlateau import axisLength, computeMaxMinAnlges


pio.templates.default = "plotly_white"
nbPoints = 1000

L1 = np.linspace(0, axisLength, nbPoints)

arrAlpha = [[], []]
arrBeta = [[], []]
arrGamma = [[], []]

arr = [arrAlpha, arrBeta, arrGamma]

for l1 in L1:
    maxMinAngles = computeMaxMinAnlges(l1)

    for i in range(3):
        arr[i][0].append(maxMinAngles[0][i])
        arr[i][1].append(maxMinAngles[1][i])


fig = make_subplots(rows=1, cols=3,
                    subplot_titles=["Tilting between x_axis / normal",
                                    "Tilting between y_axis / normal",
                                    "Tilting between z_axis / normal"])

col = 1
for angle in arr:
    fig.add_trace(
        go.Scatter(x=L1, y=angle[0], name="max", marker=dict(color='#d62728'), showlegend=True if col == 1 else False),
    row=1, col=col)

    fig.add_trace(
        go.Scatter(x=L1, y=angle[1], name="min", marker=dict(color="#1f77b4"), showlegend=True if col == 1 else False),
    row=1, col=col)

    col += 1

fig.update_xaxes(title_text="L1 in mm", row=1, col=1)
fig.update_xaxes(title_text="L1 in mm", row=1, col=2)
fig.update_xaxes(title_text="L1 in mm", row=1, col=3)

fig.update_yaxes(title_text="angle in deg", row=1, col=1)
fig.update_yaxes(title_text="angle in deg", row=1, col=2)
fig.update_yaxes(title_text="angle in deg", row=1, col=3)


fig.update_layout(
    title="Max and Min angles for different L1",
    font=dict(
        family="Courier New, monospace"
    )
)


fig.show()
