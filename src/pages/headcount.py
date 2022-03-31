from dash import html
import plotly.graph_objs as go
from utils import *



# Add dashboard specific methods here

def headcount_layout(app):

    # Call dashboard specific methods here

    return [
        html.Div(id='page2', children=[], className='page2'),
        html.H6("Headcount Layout is Working!"),
    ]