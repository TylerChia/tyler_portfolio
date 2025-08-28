import dash
from dash import html
import dash_bootstrap_components as dbc

dash.register_page(__name__, path="/")

layout = dbc.Container([
    html.H1("Welcome to My Portfolio 👋", className="text-center mb-4"),
    html.Div([
        html.H3([
            "I'm a ",
            html.Span(id="typed-output", style={
                "color": "#00bfa5",
                "fontWeight": "bold",
                "fontSize": "inherit",      # matches parent H3 size
                "fontFamily": "inherit"     # matches parent H3 font
            })
        ], 
        className="text-center", 
        style={"color": "#e0f2f1", "fontSize": "2rem"})
    ], className="mb-5"),

    html.P(
        "Hi, I’m Tyler. I graduated from the University of California, Santa Barbara in 2022 "
        "with a B.S. in Statistics/Data Science and a B.A. in Economics with minors in Spatial "
        "Science and Technology Management. In 2025, I received my M.S. in Data Science after "
        "completing my coursework at the University of Texas at Austin. I have been working as a "
        "machine learning engineer for the past 3 years at Reyes Coca Cola Bottling and plan to "
        "show all the work related to my career through this portfolio. Thanks for viewing! "
        "Through this site, I wanted to test out the functionality of Plotly's dash. As you will "
        "see through my work, I enjoy enabling and deploying data science solutions through web applications for actionable insights. "
        "I have previously used Shiny's Python and R frameworks.",
        className="lead text-center"
    ),

    #html.Hr(style={"borderColor": "#26a69a", "margin": "40px 0"}),

    # --- Top Row (Main Grad Images) ---
    dbc.Row([
        dbc.Col([
            html.H3("UC Santa Barbara", className="text-center mb-3"),
            html.Img(src="/assets/home_imgs/ucsb_grad.JPG",
                     style={"height": "450px", "width": "auto", "borderRadius": "12px"})
        ], width=6, className="text-center"),

        dbc.Col([
            html.H3("UT Austin", className="text-center mb-3"),
            html.Img(src="/assets/home_imgs/utaustin_grad.jpg",
                     style={"height": "450px", "width": "auto", "borderRadius": "12px"})
        ], width=6, className="text-center"),
    ], className="mt-4"),

    # --- Bottom Row (Last 3 Images, all aligned) ---
    dbc.Row([
        dbc.Col([
            html.H5("B.S. Data Science", className="text-center mb-3"),
            html.Img(src="/assets/home_imgs/ucsb1.jpeg",
                     style={"height": "220px", "width": "auto", "borderRadius": "12px"})
        ], width=3, className="text-center"),
        dbc.Col([
            html.H5("B.A. Economics", className="text-center mb-3"),
            html.Img(src="/assets/home_imgs/ucsb2.jpeg",
                     style={"height": "220px", "width": "auto", "borderRadius": "12px"})
        ], width=3, className="text-center"),
        dbc.Col([
            html.H5("M.S. Data Science", className="text-center mb-3"),
            html.Img(src="/assets/home_imgs/utaustin.png",
                     style={"height": "220px", "width": "auto", "borderRadius": "12px"})
        ], width=6, className="text-center"),
    ], className="mt-4"),
])

