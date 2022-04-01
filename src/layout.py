import dash_bootstrap_components as dbc
from dash import Dash, Input, Output, State, dcc, html
from pages import *
from components import *

def app_layout(app):
    # Start dashboard rendering
    app.title = "Diversity, Equity, & Inclusion Dashboard"
    
    app.layout = html.Div([
        dcc.Location(id='url', refresh=False),
        app_navbar,
        html.Div(id='page-content', className="container-fluid"),
        app_footer
    ],
        )
    
    # End dashboard rendering
    
    # Start dashboard callbacks
    @app.callback(Output('page-content', 'children'),
                [Input('url', 'pathname')])
    def display_page(pathname):
        if pathname == '/' or pathname == '/Home':
            return home_layout(app)
        elif pathname == '/Headcount':
            return headcount_layout(app)
        elif pathname == '/Diversity%20Summary':
            return summary_layout(app)
        elif pathname == '/Diversity%20Targets':
            return targets_layout(app)
        elif pathname == '/Fiscal%20Year%20Hires':
            return hires_layout(app)
        elif pathname == '/Voluntary%20Attrition':
            return attrition_layout(app)
        
    @app.callback(
        Output("navbar-collapse", "is_open"),
        [Input("navbar-toggler", "n_clicks")],
        [State("navbar-collapse", "is_open")],
    )
    def toggle_navbar_collapse(n, is_open):
        if n:
            return not is_open
        return is_open

    # end dashboard callbacks 