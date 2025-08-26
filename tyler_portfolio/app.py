import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
#import dash.pages 

# Initialize the app
app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server   # For deployment (Heroku, Render, etc.)

# Global layout
app.layout = dbc.Container([
    dbc.NavbarSimple(
        brand="Tyler Chia's Portfolio",
        color="dark", dark=True,
        children=[
            dbc.NavItem(dbc.NavLink("Home", href="/")),
            dbc.NavItem(dbc.NavLink("Portfolio", href="/portfolio")),
            dbc.NavItem(dbc.NavLink("Metrics", href="/metrics")),
            dbc.NavItem(dbc.NavLink("Contact", href="/contact")),
        ]
    ),

    # Page container asdfasdf
    dash.page_container
], fluid=True)

if __name__ == "__main__":
    app.run(debug=True)