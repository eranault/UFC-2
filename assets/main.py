

from dash import Dash, html, dcc
import pandas as pd
import a  # Supposé être un module personnalisé
import figure  # Supposé être un module personnalisé
import numpy as np
from dash.dependencies import Input, Output
import plotly.express as px
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template
from plotly.subplots import make_subplots
import dash

# Chargement du template de style pour les figures Plotly
load_figure_template("zephyr")

# Initialisation de l'application Dash avec des feuilles de style externes
external_stylesheets = [
    {
        "href": "https://fonts.googleapis.com/css2?family=Lato:wght@400;700&display=swap",
        "rel": "stylesheet",
    },
    '/Users/andy/Desktop/Talisman/assets/style.css'
]
app = Dash(external_stylesheets=external_stylesheets, suppress_callback_exceptions=True, use_pages=True)

# Définition du titre de l'application
app.title = "UFC Analytics: Understand the UFC!"

# Définition de la mise en page de l'application
app.layout = html.Div(children=[
    html.Div([
        html.Div(children=[
            html.Br(),
            # Ajout d'images
            html.Img(
                src='https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/UFC_Logo.png/800px-UFC_Logo.png?20160112220530',
                style={"width": '82.5px', 'height': '29.7px', 'margin': 'auto'}
            ),
            html.Img(
                src='https://s.rfi.fr/media/display/c0de7ee2-4fa1-11ee-9464-005056bfb2b6/w:980/p:16x9/AP23253180380469.jpg',
                style={"box-shadow": "0 2px 6px 0 rgb(67 89 113 / 20%)", "float": "right", "width": "40%"}
            ),
            html.Br(),  # Plusieurs sauts de ligne pour l'espacement
            # Titre de la page
            html.H1(
                children="My Ultimate Fighting Dashboard",
                className="DashBoardtitle",
            ),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),

        ], className="header", style={"text_align": 'center', 'color': 'white', 'background-color': '#1A1A1D'}),
        dcc.Location(id='url', refresh=False),
        html.Div(id='page-content'),
        # Création de liens pour la navigation
        html.Div([
            html.Div(
                dcc.Link(f"{page['name']} - {page['path']}", href=page["relative_path"])
            ) for page in dash.page_registry.values()
        ]),
        dash.page_container
    ])
], style={'background-color': '#f2f3f4'})

# Exécution de l'application
if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8007, debug=False)
