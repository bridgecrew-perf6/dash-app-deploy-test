import dash_bootstrap_components as dbc
from dash import html
from dash_bootstrap_components._components.Container import Container


# make a reuseable navitem for the different examples
DHS_SECTIONS = [
    "Home",
    "Headcount",
    "Diversity Summary",
    "Diversity Targets",
    "Fiscal Year Hires",
    "Voluntary Attrition",
]
DROPDOWN_STYLE = { "color": "#FFFFFF",}
NAVBARBRAND_STYLE = { "font-size": "1.8rem", "color": "#FFFFFF" }
NAVBAR_STYLE = { "height": "6.1rem" }

# make a reuseable dropdown for the different examples
dropdown = dbc.DropdownMenu(
    children=[
        dbc.DropdownMenuItem(f"{section}", href=f"{section}",)
        for section in DHS_SECTIONS
    ],
    menu_variant="dark",
    toggle_style=DROPDOWN_STYLE,
    nav=True,
    in_navbar=True,
    label="Dashboard Sections",
    direction="down",
    className="text-capitalize",
)

app_navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(
                            html.Img(
                                src="assets/HP_Logo.png",
                                height="55px",
                                className="mr-4",
                            ),
                            className="mr-2",
                        ),
                        dbc.Col(
                            dbc.NavbarBrand(
                                "Diversity, Equity, & Inclusion",
                                className="ms-4 text-capitalize",
                                style=NAVBARBRAND_STYLE ,
                            )
                        ),
                    ],
                    align="center",
                    className="g-0",
                ),
                href="/",
                style={"textDecoration": "none"},
            ),
            dbc.NavbarToggler(id="navbar-toggler2", n_clicks=0,),
            dbc.Collapse(
                dbc.Nav(
                    [dropdown],
                    className="ms-auto",
                    navbar=True,
                    style={"font-size": "1.1rem"},
                ),
                id="navbar-collapse2",
                navbar=True,
            ),
        ],
    ),
    dark=False,
    color="#0096D6",
    className="mb-5",
    style=NAVBAR_STYLE,
)
