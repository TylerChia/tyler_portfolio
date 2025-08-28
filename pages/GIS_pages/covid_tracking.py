import dash
from dash import html

dash.register_page(__name__, path="/projects/covid-tracking")

layout = html.Div([
    html.H1("COVID-19 Tracking Project"),
    html.P("Detailed write-up, charts, and explanations here...")
])