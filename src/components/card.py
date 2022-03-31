from pydoc import classname
import dash_bootstrap_components as dbc
from dash import html

CARD_STYLE = {
    "width": "25rem",
    "boxShadow": "3px 3px 8px rgb(0 0 0 / 30%",
}
CARD_TITLE_STYLE = {"color": "#007dba"}
BTN_STYLE = {"backgroundColor": "#0096D6"}

card = lambda img_src, card_title, card_text, btn_text, btn_url: dbc.Card(
    [
        dbc.CardImg(src=img_src, top=True),
        dbc.CardBody(
            [
                html.H4(card_title, className="card-title", style=CARD_TITLE_STYLE),
                html.P(card_text, className="card-text",),
                dbc.Button(btn_text, style=BTN_STYLE, className="me-1", href=btn_url),
            ]
        ),
    ],
    style=CARD_STYLE,
)

text = "Some quick example text to build on the card title and make up the bulk of the card's content."
app_cards = dbc.Container(
    children=[
        dbc.Row(
            [
                dbc.Col(
                    card(
                        "assets/place_holder.png",
                        "Headcount",
                        text,
                        "Go to Headcount",
                        "/Headcount",
                    ),
                    width=4,
                ),
                dbc.Col(
                    card(
                        "assets/place_holder.png",
                        "Diversity Summary",
                        text,
                        "Go to Diversity Summary",
                        "/Diversity%20Summary",
                    ),
                    width=4,
                ),
                dbc.Col(
                    card(
                        "assets/place_holder.png",
                        "Diversity Targets",
                        text,
                        "Go to Diversity Targets",
                        "/Diversity%20Targets",
                    ),
                    width=4,
                ),
            ],
            className="pl-5, mb-5",
        ),
        dbc.Row(
            [
                dbc.Col(
                    card(
                        "assets/place_holder.png",
                        "Fiscal Year Hires",
                        text,
                        "Go to Fiscal Year Hires",
                        "/Fiscal%20Year%20Hires",
                    ),
                    width=4,
                ),
                dbc.Col(
                    card(
                        "assets/place_holder.png",
                        "Voluntary Attrition",
                        text,
                        "Go to Voluntary Attrition",
                        "/Voluntary%20Attrition",
                    ),
                    width=4,
                ),
            ],
            className="pl-5, mt-5",
        ),
    ]
)
