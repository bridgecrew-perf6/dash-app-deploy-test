from dash import html
import plotly.graph_objs as go
from utils import *


# Add dashboard specific methods here


def home_layout():

    # Call dashboard specific methods here

    return [
        html.Div(
            id="page1", children=[html.H6("Home Layout is Working!")], className="page1"
        ),
    ]
