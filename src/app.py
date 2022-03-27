import os
import dash_bootstrap_components as dbc
from dash import Dash, Input, Output, State, dcc, html
from flask import Flask
from pages import *
from components import *


ENV = os.getenv("FLASK_ENV")

external_stylesheets=[dbc.themes.BOOTSTRAP]

server = Flask(__name__)
app = Dash(
    __name__,
    external_stylesheets=external_stylesheets,
    server=server,
)

# Start dashboard rendering
app.title = "Analytical Dashboard"


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    nav_bar,
    html.Div(id='page-content'),
])
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


# this only runs if `$ python src/main.py` is executed
if __name__ == "__main__":
    PORT = int(os.environ.get("PORT", 3001))
    app.run(host="0.0.0.0", port=PORT, debug=True)
