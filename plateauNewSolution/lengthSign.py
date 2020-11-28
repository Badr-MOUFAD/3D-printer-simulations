from plateauNewSolution.newEquationMotion import L1, L2, L3, computeLo

import numpy as np

import plotly.graph_objects as go
import plotly.io as pio

pio.templates.default = "plotly_white"


vec = [100, 200, 500]
nbPoints = 100

arrPhi = np.linspace(-180, 179, nbPoints)
#arrTheta = np.linspace(0, 90, nbPoints)

arrPositives = []
arrPhiPositives = []

arrNegatives = []
arrPhiNegatives = []


theta = 10
for phi in arrPhi:
    if 0 <= L1(vec, [phi, theta]) <= 1000 and 0 <= L2(vec, [phi, theta]) <= 1000 and 0 <= L3(vec, [phi, theta]) <= 1000:
        #arrDifferences.append(np.sign(L1(vec, [phi, theta]) - computeLo(vec, [phi, theta])) + 2)
        #arrDifferences.append(np.sign(L1(vec, [phi, theta]) - computeLo(vec, [phi, theta])))
        if L3(vec, [phi, theta]) - computeLo(vec, [phi, theta]) > 0:
            arrPositives.append(1)
            arrPhiPositives.append(phi)
        else:
            arrNegatives.append(1)
            arrPhiNegatives.append(phi)


# plot the graph
fig = go.Figure(data=[go.Scatterpolar(theta=arrPhiPositives, r=arrPositives, name="Positive", fill="toself"),
                      go.Scatterpolar(theta=arrPhiNegatives, r=arrNegatives, name="Negative", fill="toself",)],
                layout=(dict(height=600, width=600)))

fig.update_layout(
    title="sign of L1 - L0".format(*vec),
    xaxis_title="phi in deg",
    yaxis_title="theta in deg",
    font=dict(
        family="Courier New, monospace"
    )
)

fig.show()