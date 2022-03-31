from dash import html
import plotly.graph_objs as go
from utils import *



# Add dashboard specific methods here

def attrition_layout(app):

    # Call dashboard specific methods here

    return [
        html.Div(id='page6', children=[], className='page6'),
        html.H6("Attrition Layout is Working!"),
    ]