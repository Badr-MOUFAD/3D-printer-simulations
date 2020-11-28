from plateauNewSolution.newEquationMotion import computeThinkness

import numpy as np

import plotly.graph_objects as go
import plotly.io as pio

pio.templates.default = "plotly_white"


workSpaceRadius = 310
angle = 30 / 180 * np.pi  # particular direction

nbPoints = 30
arrZ = np.linspace(0, 1000, nbPoints)

arrMinThickness = []

for z in arrZ:
    vec = [workSpaceRadius * np.cos(angle), workSpaceRadius * np.sin(angle), z]

    arrMinThickness.append(computeThinkness(vec))


fig = go.Figure(data=[
    go.Scatter(x=arrZ, y=arrMinThickness, mode="markers + lines")
])

fig.update_layout(
    title="Evolution of min thickness",
    xaxis_title="Z in mm",
    yaxis_title="thickness in deg",
    font=dict(
        family="Courier New, monospace"
    )
)

fig.show()

