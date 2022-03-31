from dash import html
import plotly.graph_objs as go
from utils import *



# Add dashboard specific methods here

def hires_layout(app):

    # Call dashboard specific methods here

    return [
        html.Div(id='page5', children=[], className='page5'),
        html.H6("Hires Layout is Working!"),
    ]