import numpy as np

from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly.io as pio

from simulationPlateau.equationMotionPlateau import axisLength, computeMaxMinAnlges, computeMaxY


pio.templates.default = "plotly_white"
nbPoints = 1000

arrAlpha = [2, 5.9, 12, 13.2, 17, 20, 23.1]
arrBeta = [3.8, 8.78, 19, 22.8, 28.35, 33, 35.7]
arrGamma = [4.4, 9.12, 21.5, 26, 34.34, 38.5, 39]

arrLongeurLiaison = [50, 60, 90, 100, 130, 160, 200]

fig = make_subplots(rows=1, cols=3,
                    subplot_titles=["angle entre x_axis / normale",
                                    "angle entre y_axis / normale",
                                    "angle entre z_axis / normale"])



fig.add_trace(
    go.Scatter(x=arrLongeurLiaison, y=arrAlpha,
               showlegend=False),
    row=1, col=1)

fig.add_trace(
    go.Scatter(x=arrLongeurLiaison, y=arrBeta,
               showlegend=False),
    row=1, col=2)

fig.add_trace(
    go.Scatter(x=arrLongeurLiaison, y=arrGamma,
               showlegend=False),
    row=1, col=3)


for i in range(3):
    fig.update_xaxes(title_text="longueur de liaison en mm", row=1, col=i + 1)
    fig.update_yaxes(title_text="angle en deg", range=[0, 40], constrain="domain", row=1, col=i + 1)


fig.update_layout(
    title="Relation entre inclinaison et longueur de la liaison",
    font=dict(
        family="Courier New, monospace"
    )
)


fig.show()
