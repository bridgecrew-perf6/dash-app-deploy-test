import dash_bootstrap_components as dbc
from dash import html
from dash_bootstrap_components._components.Container import Container

PLOTLY_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"

# make a reuseable navitem for the different examples
dsh_sections = ["Headcount", "Summary", "Hires", "Attrition"]

# make a reuseable dropdown for the different examples
dropdown = dbc.DropdownMenu(
    children=[dbc.DropdownMenuItem(f"{section}", href=f"{section}") for section in dsh_sections],
    nav=True,
    in_navbar=True,
    label="Dashboard Sections",
    direction="down",
)

nav_bar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(html.Img(src=PLOTLY_LOGO, height="30px")),
                        dbc.Col(dbc.NavbarBrand("Logo", className="ms-2")),
                    ],
                    align="center",
                    className="g-0",
                ),
                href="/",
                style={"textDecoration": "none"},
            ),
            dbc.NavbarToggler(id="navbar-toggler2", n_clicks=0),
            dbc.Collapse(
                dbc.Nav(
                    [dropdown],
                    className="ms-auto",
                    navbar=True,
                ),
                id="navbar-collapse2",
                navbar=True,
            ),
        ],
    ),
    color="dark",
    dark=True,
    className="mb-5",
)
