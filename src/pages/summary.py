from dash import html
import plotly.graph_objs as go
from utils import *



# Add dashboard specific methods here

def summary_layout():

    # Call dashboard specific methods here

    return [
        html.Div(id='page3', children=[], className='page3'),
        html.H6("Summary Layout is Working!"),
    ]