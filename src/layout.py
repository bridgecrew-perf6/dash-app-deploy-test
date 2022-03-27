
from click import style
import dash_bootstrap_components as dbc
from dash import Dash, Input, Output, State, dcc, html
from pages import *
from components import *

def app_layout(app):
    # Start dashboard rendering
    app.title = "Analytical Dashboard"


    app.layout = html.Div([
        dcc.Location(id='url', refresh=False),
        nav_bar,
        html.Div(id='page-content')
    ],
        style = {'font-family': 'Helvetica'}
        )
    
    # End dashboard rendering
    
    # Start dashboard callbacks
    @app.callback(Output('page-content', 'children'),
                [Input('url', 'pathname')])
    def display_page(pathname):
        if pathname == '/':
            return home_layout()
        elif pathname == '/Headcount':
            return headcount_layout(app)
        elif pathname == '/Summary':
            return summary_layout()
        
    @app.callback(
        Output("navbar-collapse", "is_open"),
        [Input("navbar-toggler", "n_clicks")],
        [State("navbar-collapse", "is_open")],
    )
    def toggle_navbar_collapse(n, is_open):
        if n:
            return not is_open
        return is_open

    @app.callback(
            Output(component_id="my-output", component_property="children"),
            Input(component_id="my-input", component_property="value"),
        )
    def update_output_div(input_value):
        return f"{input_value}"

    # end dashboard callbacks 