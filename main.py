import plotly
import plotly.graph_objs as go
from plotly.subplots import make_subplots

import numpy as np
import pandas as pd

# from scipy import signal # для savgol_filter, если понадобится сглаживание

def main():
    with open('C:/Users/user/source/repos/KursachChM/KursachChM/points.txt', 'r') as f:
        xn = int(f.readline())
        x = f.readline().split()
        x = list(map(lambda el: float(el), x))
        tn = int(f.readline())
        t = f.readline().split()
        t = list(map(lambda el: float(el), t))
        xt = []
        for i in range(tn):
            xi = f.readline().split()
            xi = list(map(lambda el: float(el), xi))
            xt.append(xi)

        num_steps = tn
        fig = go.Figure(data=[go.Scatter(x=x, y=xt[0], mode='lines', name='u(x,t)')])

        frames = []
        for i in range(num_steps):
            frames.append(go.Frame(name=str(t[i]),
                                   data=[go.Scatter(x=x, y=xt[i], mode='lines', name='u(x,t)')]))

        steps = []
        for i in range(num_steps):
            step = dict(
                label=str(t[i]),
                method='animate',
                args=[[str(t[i])]],
            )
            steps.append(step)

        sliders = [dict(
            currentvalue={"prefix": "t = ", "font": {"size": 20}},
            len=0.9,
            x=0.1,
            pad={"b": 10, "t": 50},
            steps=steps,
        )]

        fig.update_yaxes(zeroline=True, zerolinewidth=1, zerolinecolor='Black')
        fig.update_xaxes(range=[x[0], x[xn-1]], zeroline=True, zerolinewidth=1, zerolinecolor='Black')
        fig.update_layout(legend_orientation="h",
                          legend=dict(x=.5, xanchor="center"),
                          updatemenus=[dict(direction="left",
                                            pad={"r": 10, "t": 80},
                                            x=0.1,
                                            xanchor="right",
                                            y=0,
                                            yanchor="top",
                                            showactive=False,
                                            type="buttons",
                                            buttons=[dict(label="►", method="animate", args=[None, {"fromcurrent": True,
                                                                                                    "frame": {"duration": 30},
                                                                                                    "transition": {"duration": 0}}]),
                                                     dict(label="❚❚", method="animate", args=[[None], {"frame": {"duration": 0, "redraw": False},
                                                                                                       "mode": "immediate",
                                                                                                       "transition": {"duration": 0}}])])],
                          title='Колебание струны',
                          xaxis_title="x",
                          yaxis_title="u(x)",
                          yaxis_range=[-2,2])
        fig.update_traces(hoverinfo="x+y")
        fig.layout.sliders = sliders
        fig.frames = frames
        fig.show()


if __name__ == '__main__':
    main()