from dash import html, dcc
import plotly.graph_objs as go
from utils import *


# Add dashboard specific methods here

df = get_csv_data(
    "https://gist.githubusercontent.com/chriddyp/"
    + "5d1ea79569ed194d432e56108a04d188/raw/"
    + "a9f9e8076b837d541398e999dcbac2b2826a81f8/"
    + "gdp-life-exp-2007.csv",
)


def headcount_layout(app):

    # Call dashboard specific methods here

    return [
        dcc.Graph(
            id="life-exp-vs-gdp",
            figure={
                "data": [
                    go.Scatter(
                        x=df[df["continent"] == i]["gdp per capita"],
                        y=df[df["continent"] == i]["life expectancy"],
                        text=df[df["continent"] == i]["country"],
                        mode="markers",
                        opacity=0.7,
                        marker={"size": 15, "line": {"width": 0.5, "color": "white"}},
                        name=i,
                    )
                    for i in df.continent.unique()
                ],
                "layout": go.Layout(
                    xaxis={"type": "log", "title": "GDP Per Capita"},
                    yaxis={"title": "Life Expectancy"},
                    margin={"l": 40, "b": 40, "t": 10, "r": 10},
                    legend={"x": 0, "y": 1},
                    hovermode="closest",
                ),
                
            },
        ),
        html.H6("Change the value in the text box to see callbacks in action!"),
        html.Div(
            ["Input: ", dcc.Input(id="my-input", value="Write here!", type="text")],
        ),
        html.Br(),
        html.Div(id="my-output"),
    ]
