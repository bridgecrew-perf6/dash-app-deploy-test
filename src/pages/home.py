from dash import html
import plotly.graph_objs as go
from utils import *
from components import *


# Add dashboard specific methods here


def home_layout(app):

    return [
        html.Div(app_cards,),
    ]
