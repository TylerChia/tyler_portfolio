import dash
from dash import html
import dash_bootstrap_components as dbc

dash.register_page(__name__, path="/portfolio")

# Example client showcase cards
clients = [
    {"name": "Brand A", "desc": "Scaled TikTok followers from 0 → 50K in 6 months", "img": "/assets/brand_a.png"},
    {"name": "Brand B", "desc": "Increased Instagram engagement by 250%", "img": "/assets/brand_b.png"}
]

layout = dbc.Container([
    html.H2("Portfolio", className="my-4 text-center"),
    dbc.Row([
        dbc.Col(
            dbc.Card([
                dbc.CardImg(src=c["img"], top=True),
                dbc.CardBody([
                    html.H4(c["name"]),
                    html.P(c["desc"])
                ])
            ], className="shadow-sm mb-4"), width=6
        )
        for c in clients
    ])
])
