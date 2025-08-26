import dash
from dash import html
import dash_bootstrap_components as dbc

dash.register_page(__name__, path="/")

layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("Welcome!", className="text-center my-4"))
    ]),

    dbc.Row([
        dbc.Col([
            html.H3("About Me"),
            html.P("I’m a freelance social media marketer specializing in building brand awareness, running ad campaigns, and growing engagement."),
        ], width=6),
        dbc.Col([
            html.H3("Sample Ad Video"),
            html.Video(src="/assets/sampleruluu.MOV", controls=True, style={"width": "100%", "height": "500px", "border-radius": "12px"})
        ], width=6)
    ])
])