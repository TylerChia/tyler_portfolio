import dash
from dash import html
import dash_bootstrap_components as dbc

dash.register_page(__name__, path="/contact")

layout = dbc.Container([
    html.H2("Get in Touch", className="my-4 text-center"),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.P("📧 Email: "),
                    html.A("yourname@email.com",
                           href="mailto:yourname@email.com",
                           className="d-block mb-3"),

                    html.P("💼 LinkedIn: "),
                    html.A("linkedin.com/in/yourprofile",
                           href="https://linkedin.com/in/yourprofile",
                           target="_blank",
                           className="d-block mb-3"),

                    html.P("📄 Resume:"),
                    dbc.Button("Download Resume",
                               href="/assets/resume.pdf",
                               download="resume.pdf",
                               color="primary")
                ])
            ], className="contact-section")
        ], width=6)
    ], justify="center")
])