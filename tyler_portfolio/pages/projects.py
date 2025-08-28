import dash
from dash import html
import dash_bootstrap_components as dbc

dash.register_page(__name__, path="/projects")

projects = [
    {"title": "Interactive Data Dashboard", "desc": "Built using Dash + Plotly"},
    {"title": "GIS Mapping App", "desc": "Leaflet + Geopandas + Dash"},
    {"title": "Machine Learning Model", "desc": "Predictive model for sales data"}
]

layout = dbc.Container([
    html.H2("Personal Projects", className="text-center mb-4"),
    dbc.Row([
        dbc.Col(
            dbc.Card([
                dbc.CardBody([
                    html.H4(p["title"], className="card-title"),
                    html.P(p["desc"])
                ])
            ]), md=4
        ) for p in projects
    ], className="gy-4")
])
