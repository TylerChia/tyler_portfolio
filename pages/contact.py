import dash
from dash import html
import dash_bootstrap_components as dbc

import dash
from dash import html
import dash_bootstrap_components as dbc
import dash_iconify

dash.register_page(__name__, path="/contact")

layout = dbc.Container([
    html.H2("Contact Me", className="text-center mb-4"),

    dbc.Row([
        dbc.Col(
            dbc.Card([
                dbc.CardBody([
                    html.H4("Let's Connect", className="card-title text-center mb-3"),

                    # Resume Download
                    dbc.Button(
                        "📄 Download Resume",
                        href="/assets/resume.pdf",
                        color="info",
                        className="mb-3 w-100",
                        external_link=True
                    ),

                    # Social Links
                    dbc.Button("💼 LinkedIn", 
                               href="https://www.linkedin.com/in/tylerchia/", 
                               color="primary", 
                               className="mb-2 w-100",
                               external_link=True,
                               target="_blank"),

                    dbc.Button("💻 GitHub", 
                               href="https://github.com/TylerChia", 
                               color="dark", 
                               className="mb-2 w-100",
                               external_link=True,
                               target="_blank"),

                    dbc.Button("✉️ Email Me", 
                               href="mailto:tylerchia7@gmail.com", 
                               color="success", 
                               className="mb-2 w-100",
                               target="_blank")
                ])
            ], className="shadow-lg"),
            md=6
        )
    ], justify="center")
])

