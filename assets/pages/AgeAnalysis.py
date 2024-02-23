import dash
from dash import html, dcc
import a  # Supposé être un module personnalisé contenant des données ou des fonctions
import figure  # Supposé être un module personnalisé contenant des figures Plotly

# Enregistrement de la page dans l'application Dash
dash.register_page(__name__)

# Mise en page de la page Dash
layout = html.Div([
    # Section pour les coups significatifs
    html.Div([
        html.Br(),  # Espaces pour la mise en forme
        # Paragraphe expliquant l'objectif de la section
        html.P(
            children="Dans cette section on vérifie une relation entre la moyenne des coups significatifs et l'âge.",
            className="hello",
        ),
        html.P(
            children="La moyenne des coups significatifs d'un combattant étant un paramètre important pour les jurys dans le cas où le combat va à la décision.",
            className="hello",
        ),
        html.Br(),  # Espaces pour la mise en forme
    ], className="header", style={"text_align": 'center', 'color': 'black', 'background-color': 'white'}),
    # Graphique pour les coups significatifs des combattants B
    html.Div(
        dcc.Graph(id="strikeB_graph", figure=figure.strikeB), style={"width": '95%', 'display': 'inline-block', 'margin': '5px'}
    ),
    # Graphique pour les coups significatifs des combattants R
    html.Div(
        dcc.Graph(id="strikeR_graph", figure=figure.strikeR), style={"width": '95%', 'display': 'inline-block', 'margin': '5px'}
    ),
    html.Br(),

    # Section pour les takedowns
    html.Div([
        html.Br(),  # Espaces pour la mise en forme
        # Paragraphe expliquant l'objectif de la section
        html.P(
            children="On effectue le même processus pour la moyenne des takedowns réussis des combattants.",
            className="hello",
        ),
        html.P(
            children="Notons que le takedown est probablement le processus le plus épuisant et demandant musculairement lors d'un combat.",
            className="hello",
        ),
        html.Br(),  # Espaces pour la mise en forme
    ], className="header", style={"text_align": 'center', 'color': 'black', 'background-color': 'white'}),
    # Graphique pour les takedowns des combattants B
    html.Div(
        dcc.Graph(id="takedownB_graph", figure=figure.takedownB), style={"width": '95%', 'display': 'inline-block', 'margin': '5px'}
    ),
    # Graphique pour les takedowns des combattants R
    html.Div(
        dcc.Graph(id="takedownR_graph", figure=figure.takedownR), style={"width": '95%', 'display': 'inline-block', 'margin': '5px'}
    ),
    html.Br(),
])
