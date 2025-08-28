import dash
from dash import html
import dash_bootstrap_components as dbc

dash.register_page(__name__, path="/research")

layout = dbc.Container([
    html.H2("Research", className="text-center mb-4"),
    dbc.Row([
        dbc.Col(
            dbc.Card([
                dbc.CardBody([
                    html.H4("Company X", className="card-title"),
                    html.P("Worked on data visualization dashboards."),
                    html.Small("Summer 2023")
                ])
            ]), width=12
        ),
        dbc.Col(
            dbc.Card([
                dbc.CardBody([
                    html.H4("Company Y", className="card-title"),
                    html.P("Developed GIS spatial analysis workflows."),
                    html.Small("Summer 2022")
                ])
            ]), width=12
        ),
    ], className="gy-3")
])
