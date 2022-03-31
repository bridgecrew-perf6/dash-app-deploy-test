from dash import html
import plotly.graph_objs as go
from utils import *



# Add dashboard specific methods here

def targets_layout(app):

    # Call dashboard specific methods here

    return [
        html.Div(id='page4', children=[], className='page4'),
        html.H6("Targes Layout is Working!"),
    ]