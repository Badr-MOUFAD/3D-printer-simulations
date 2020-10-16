
import plotly.graph_objects as go

from simulationPlateau.equationMotionPlateau import Rx, Ry, Rz, cosPi3, sinPi3, axisLength

vec1 = [0, 0, 0]
vec2 = [0, 0, axisLength / 2]
vec3 = [0, 0, axisLength]

arrPoints = []

for vec in [vec1, vec2, vec3]:
    A = [-Rx * sinPi3, -Rx * cosPi3, vec[0]]
    B = [Ry(vec) * sinPi3, -Ry(vec) * cosPi3, vec[1]]
    C = [0, Rz(vec), vec[2]]

    arrPoints.append([A, B, C])


fig = go.Figure(data=[
        go.Mesh3d(x=[points[i][0] for i in range(3)], y=[points[i][1] for i in range(3)], z=[points[i][2] for i in range(3)])
        for points in arrPoints
    ]
)


fig.update_layout(
    title="Some positions of the chassis (L1 and L2 are fixed)",
    font=dict(
        family="Courier New, monospace"
    ),
    height=600,
    width=600
)

fig.show()
