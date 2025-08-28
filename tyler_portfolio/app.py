import dash
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from dash_iconify import DashIconify
# Use a modern dark theme
app = Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.CYBORG])



navbar = dbc.NavbarSimple(
    brand="Tyler Chia's Portfolio",
    brand_href="/",
    color="teal",
    dark=True,
    fluid=True,
    sticky="top",
    children=[
        dbc.NavItem(
            dbc.NavLink([DashIconify(icon="mdi:home", width=20), " Home"], href="/")
        ),
        dbc.NavItem(
            dbc.NavLink([DashIconify(icon="mdi:briefcase", width=20), " Employment"], href="/employment")
        ),
        dbc.NavItem(
            dbc.NavLink([DashIconify(icon="mdi:laptop", width=20), " Projects"], href="/projects")
        ),
        dbc.NavItem(
            dbc.NavLink([DashIconify(icon="mdi:flask", width=20), " Research"], href="/research")
        ),
        dbc.NavItem(
            dbc.NavLink([DashIconify(icon="mdi:map", width=20), " GIS Work"], href="/gis")
        ),
        dbc.NavItem(
            dbc.NavLink([DashIconify(icon="mdi:email", width=20), " Contact"], href="/contact")
        ),
    ],
)


# App Layout
app.layout = dbc.Container(
    [
        navbar,
        html.Br(),
        dash.page_container
    ],
    fluid=True,
    style={"backgroundColor": "#0d1b1e", "color": "#e0f2f1", "minHeight": "100vh", "padding": "20px"}
)



# Repeat similar structure for projects.py, internships.py, research.py, employment.py, gis.py, contact.py

if __name__ == "__main__":
    app.run(debug=True)
