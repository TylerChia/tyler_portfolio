import dash
from dash import html
import dash_bootstrap_components as dbc
from dash import dcc

dash.register_page(__name__, path="/gis")

layout = dbc.Container([
    html.H2("GIS Work", className="text-center mb-4"),
    html.P("During the summer of 2020, I took six classes, one of which was a GIS course based in R. "
           "Out of the three coding classes I took this summer, this GIS course was the most hands-on and provided me with the most experience for data science. " 
           "Below is a collection of links for all the projects that I completed. Click on each card to view the project."),
    html.Hr(style={"borderColor": "#26a69a", "margin": "40px 0"}),

    # dbc.Col(
    #     dcc.Link(
    #         dbc.Card(
    #             dbc.Row([
    #                 # Left side: text content
    #                 dbc.Col(
    #                     dbc.CardBody([
    #                         html.H4("Tracking COVID-19 Data", className="card-title"),
    #                         html.Ul([
    #                             html.Li("Built interactive dashboards with Plotly and Dash"),
    #                             html.Li("Automated ETL pipeline for data ingestion"),
    #                             html.Li("Deployed app on Heroku for live monitoring")
    #                         ]),
    #                         html.Small("Summer 2023", className="text-muted"),
    #                     ]),
    #                     width=8
    #                 ),

    #                 # Right side: preview image
    #                 dbc.Col(
    #                     html.Img(
    #                         src="/assets/GIS_imgs/lab02img.png",
    #                         style={
    #                             "width": "100%",
    #                             "height": "100%",
    #                             "objectFit": "cover",
    #                             "borderRadius": "8px"
    #                         }
    #                     ),
    #                     width=4
    #                 ),
    #             ],
    #             className="g-0 d-flex align-items-center"),
    #             style={"cursor": "pointer"}
    #         ),
    #         href="https://tylerchia.github.io/geog-176A-labs/lab-02.html",  # ✅ link target
    #         style={"textDecoration": "none", "color": "inherit"}  # remove underline + keep text color
    #     ),
    #     width=12,
    #     className="mb-4"
    # ),

    dbc.Col(
        html.A(
            dbc.Card([
                dbc.Row([
                    # Left: text
                    dbc.Col(
                        dbc.CardBody([
                            html.H4("Tracking COVID-19 Data", className="card-title"),
                            html.Ul([
                                html.Li("Learned the basics of data wrangling"),
                                html.Li("Gained the ability to analyze data sets in order to be able to be able to identify important information as well as merge multiple data sets on recurring variables"),
                                html.Li("Learned the basics of ggplot2 which allows me to present my data analysis through graphs and other visualizations"),
                                html.Li("Helped me understand the importance of scale when graphing as two graphs with the same data can imply two very different results")
                            ]),
                            html.Small("Summer 2020", className="text-muted")
                        ]),
                        width=8
                    ),

                    # Right: scaled preview image
                    dbc.Col(
                        html.Img(
                            src="/assets/GIS_imgs/lab02img.png",
                            style={
                                "maxHeight": "250px",  # scale down
                                "width": "auto",       # maintain aspect ratio
                                "borderRadius": "8px",
                                "display": "block",
                                "margin": "auto"       # center vertically
                            }
                        ),
                        width=4,
                        className="d-flex align-items-center"  # vertically center the column
                    )
                ], className="g-0"),
            ],
            style={"cursor": "pointer", "marginBottom": "20px"}
            ),
            href="https://tylerchia.github.io/geog-176A-labs/lab-02.html",
            target="_blank",
            style={"textDecoration": "none", "color": "inherit"}
        ),
        width=12
    ),


    dbc.Col(
        html.A(
            dbc.Card([
                dbc.Row([
                    # Left: text
                    dbc.Col(
                        dbc.CardBody([
                            html.H4("Distances and the Border Zone", className="card-title"),
                            html.Ul([
                                html.Li("Reading in data and creating sf objects"),
                                html.Li("Transforming both coordinate systems and geometries in order to find distance between objects"),
                                html.Li("Dropping and converting units from meters to kilometers"),
                                html.Li("Using ggrepel and gghighlight to create visuals for the data")
                            ]),
                            html.Small("Summer 2020", className="text-muted")
                        ]),
                        width=8
                    ),

                    # Right: scaled preview image
                    dbc.Col(
                        html.Img(
                            src="/assets/GIS_imgs/lab3img.png",
                            style={
                                "maxHeight": "250px",  # scale down
                                "width": "auto",       # maintain aspect ratio
                                "borderRadius": "8px",
                                "display": "block",
                                "margin": "auto"       # center vertically
                            }
                        ),
                        width=4,
                        className="d-flex align-items-center"  # vertically center the column
                    )
                ], className="g-0"),
            ],
            style={"cursor": "pointer", "marginBottom": "20px"}
            ),
            href="https://tylerchia.github.io/geog-176A-labs/lab-03.html",
            target="_blank",
            style={"textDecoration": "none", "color": "inherit"}
        ),
        width=12
    ),


    dbc.Col(
        html.A(
            dbc.Card([
                dbc.Row([
                    # Left: text
                    dbc.Col(
                        dbc.CardBody([
                            html.H4("Tessellations and Point-In-Polygon", className="card-title"),
                            html.Ul([
                                html.Li("Creating functions as a way of making calculations and visualizations easier"),
                                html.Li("Simplifying geometries in order to speed up the processing time for my computer"),
                                html.Li("Creating tessellations that describe the extent of a region with geometric shapes"),
                                html.Li("Different tessellations can show very different results which is the MAUP problem"),
                                html.Li("Building leaflets that give users an interactive experience with mapping")
                            ]),
                            html.Small("Summer 2020", className="text-muted")
                        ]),
                        width=8
                    ),

                    # Right: scaled preview image
                    dbc.Col(
                        html.Img(
                            src="/assets/GIS_imgs/lab4img.png",
                            style={
                                "maxHeight": "250px",  # scale down
                                "width": "auto",       # maintain aspect ratio
                                "borderRadius": "8px",
                                "display": "block",
                                "margin": "auto"       # center vertically
                            }
                        ),
                        width=4,
                        className="d-flex align-items-center"  # vertically center the column
                    )
                ], className="g-0"),
            ],
            style={"cursor": "pointer", "marginBottom": "20px"}
            ),
            href="https://tylerchia.github.io/geog-176A-labs/lab-04.html",
            target="_blank",
            style={"textDecoration": "none", "color": "inherit"}
        ),
        width=12
    ),

    dbc.Col(
        html.A(
            dbc.Card([
                dbc.Row([
                    # Left: text
                    dbc.Col(
                        dbc.CardBody([
                            html.H4("Rasters and Remote Sensing", className="card-title"),
                            html.Ul([
                                html.Li("Identifying an AOI by using a bounding box created from max/min x and y points"),
                                html.Li("Download, cache, and load images as multiband raster object and crop domain to AOI"),
                                html.Li("Creating RGB plots using Landsat 8 Operational Land Imager"),
                                html.Li("Using Raster Algebra and Raster Thresholding to display flood raster stack through different methods"),
                                html.Li("Utilizing K-Means algorithm to identify similar features in a continuous field")
                            ]),
                            html.Small("Summer 2020", className="text-muted")
                        ]),
                        width=8
                    ),

                    # Right: scaled preview image
                    dbc.Col(
                        html.Img(
                            src="/assets/GIS_imgs/lab4img.png",
                            style={
                                "maxHeight": "250px",  # scale down
                                "width": "auto",       # maintain aspect ratio
                                "borderRadius": "8px",
                                "display": "block",
                                "margin": "auto"       # center vertically
                            }
                        ),
                        width=4,
                        className="d-flex align-items-center"  # vertically center the column
                    )
                ], className="g-0"),
            ],
            style={"cursor": "pointer", "marginBottom": "20px"}
            ),
            href="https://tylerchia.github.io/geog-176A-labs/lab-05.html",
            target="_blank",
            style={"textDecoration": "none", "color": "inherit"}
        ),
        width=12
    ),


    dbc.Col(
        html.A(
            dbc.Card([
                dbc.Row([
                    # Left: text
                    dbc.Col(
                        dbc.CardBody([
                            html.H4("Flood Risk in Mission Creek: Past, Present, Future", className="card-title"),
                            html.Ul([
                                html.Li("Bringing data into R using Web APIs, specifically the NLDI and USGS gages"),
                                html.Li("Utilizing OSM to query building and stream data"),
                                html.Li("Creating HAND rasters for rapid flood assessment in order to see structures that were impacted by inundation"),
                                html.Li("Creating Flood Inundation Map Libraries as a way to form a 2-D flood warning system"),
                            ]),
                            html.Small("Summer 2020", className="text-muted")
                        ]),
                        width=8
                    ),

                    # Right: scaled preview image
                    dbc.Col(
                        html.Img(
                            src="/assets/GIS_imgs/mission-creek-fim.gif",
                            style={
                                "maxHeight": "250px",  # scale down
                                "width": "auto",       # maintain aspect ratio
                                "borderRadius": "8px",
                                "display": "block",
                                "margin": "auto"       # center vertically
                            }
                        ),
                        width=4,
                        className="d-flex align-items-center"  # vertically center the column
                    )
                ], className="g-0"),
            ],
            style={"cursor": "pointer", "marginBottom": "20px"}
            ),
            href="https://tylerchia.github.io/geog-176A-labs/lab-06.html",
            target="_blank",
            style={"textDecoration": "none", "color": "inherit"}
        ),
        width=12
    ),


    
    ], className="gy-3"   
)
