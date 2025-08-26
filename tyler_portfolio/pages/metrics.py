import dash
import plotly.express as px
import pandas as pd
from dash import html, dcc
import dash_bootstrap_components as dbc

dash.register_page(__name__, path="/metrics")

# Example Data
df = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr"],
    "Followers": [1000, 1300, 1800, 2500],
    "Engagement": [5.1, 6.3, 7.8, 9.2]
})

fig_followers = px.line(df, x="Month", y="Followers", markers=True, title="Follower Growth")
fig_engagement = px.bar(df, x="Month", y="Engagement", title="Engagement Rate (%)")

layout = dbc.Container([
    html.H2("Campaign Metrics", className="my-4 text-center"),
    dbc.Row([
        dbc.Col(dcc.Graph(figure=fig_followers), width=6),
        dbc.Col(dcc.Graph(figure=fig_engagement), width=6),
    ])
])
