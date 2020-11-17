import plotly.graph_objects as go
import plotly.io as pio

import numpy as np

pio.templates.default = "plotly_white"


fig = go.Figure(
    data=[
        go.Scatter(
            x=[l for l in range(0, 1100, 100)], y=[0, 6, 13, 17, 17, 17, 17, 17, 13, 6, 0], mode="markers + lines"
        ),
        go.Scatter(x=[300, 300], y=[0, 18], mode="lines", line=dict(dash="dashdot", color="red")),
        go.Scatter(x=[700, 700], y=[0, 18], mode="lines", line=dict(dash="dashdot", color="red"))
    ]
)


fig.update_layout(
    title="Borne de la bande en fonction de z",
    font=dict(
        family="Courier New, monospace"
    ),
    xaxis_title="z en mm",
    yaxis_title="angle theta en deg",
    showlegend=False,
    height=600,
    width=600
)


fig.show()
