import dash_bootstrap_components as dbc
import datetime as dt
from dash import html
from dash_bootstrap_components._components.Container import Container

current_year = dt.datetime.now().year

FOOTER_HEIGHT = "6rem", "10rem"

FOOTER_STYLE = {
    "position": "absolute",
    "textAlign": "center",
    "color": "gray",
    "left": 0,
    "right": 0,
    "height": FOOTER_HEIGHT,
    "marginTop": "8.5rem",
    "padding": "2rem 1rem",
    "background-color": "#f6f6f6",
}
app_footer = html.Footer(html.H6(f"©Copyright {current_year} HP Inc. | HP Restricted"), style=FOOTER_STYLE,)