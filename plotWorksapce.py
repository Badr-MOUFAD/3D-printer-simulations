
def simulateWorkspace(R_, r_, L_, H_, nbPoints_=400, z_=0):
    import numpy as np
    from algoParameters import findRadius
    import plotly.graph_objects as go
    import plotly.io as pio

    pio.templates.default = "plotly_white"

    # -------- constant ------- #
    R = R_  # diameter of chassis
    r = r_  # diameter of nacelle
    H = H_  # height of robot
    L = L_  # length of arms

    cosPi3 = np.cos(np.pi / 3)
    sinPi3 = np.sin(np.pi / 3)

    DR = R - r
    dR = 70 + 30

    # translation
    h = r * cosPi3
    u1 = (-h * sinPi3, h * cosPi3)
    u2 = (h * sinPi3, h * cosPi3)
    u3 = (0, -h)

    # --------- equation of motion ------- #
    def L1(x, y, z):
        term = (DR * sinPi3 + x) ** 2 + (DR * cosPi3 + y) ** 2

        if L ** 2 < term:
            return None

        result = z + np.sqrt(L ** 2 - term)

        if result > H:
            return None

        return result

    def L2(x, y, z):
        term = (-DR * sinPi3 + x) ** 2 + (DR * cosPi3 + y) ** 2

        if L ** 2 < term:
            return None

        result = z + np.sqrt(L ** 2 - term)

        if result > H:
            return None

        return result

    def L3(x, y, z):
        term = x ** 2 + (-DR + y) ** 2

        if L ** 2 < term:
            return None

        result = z + np.sqrt(L ** 2 - term)

        if result > H:
            return None

        return result

    def belowD1(x, y):
        if (cosPi3 + 1) / sinPi3 * x + (R + dR) > y:
            return True

        return False

    def belowD2(x, y):
        if -(cosPi3 + 1) / sinPi3 * x + (R + dR) > y:
            return True

        return False

    def aboveD3(x, y):
        if y > - (R + dR) * cosPi3:
            return True

        return False

    # ------- algorithm of simulation ------- #
    xLim = int(R + dR)
    yLim = int(R + dR)
    nbPoints = nbPoints_

    # plan of simulation
    z = z_

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

    # effective working space
    radius = findRadius([R, r, L, H])

    t = np.linspace(0, 2 * np.pi, 200)
    cercleX = radius * np.cos(t)
    cercleY = radius * np.sin(t)

    # plot the graph
    fig = go.Figure(data=[go.Scatter(x=xWorkSpace, y=yWorkSpace, mode='markers', name="Workspace"),
                          go.Scatter(x=cercleX, y=cercleY, mode='markers', name="target")],
                    layout=(dict(height=600, width=600)))

    fig.update_layout(
        title="Delta Robot Working Space for z={0:.2f} radius={1:.2f}".format(z, radius),
        xaxis_title="X in mm",
        yaxis_title="Y in mm",
        font=dict(
            family="Courier New, monospace"
        )
    )

    fig.show()
    return




# example
simulateWorkspace(720, 170, 940, 1820, 400, z_=0)
