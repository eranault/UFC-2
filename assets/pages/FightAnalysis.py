import dash
from dash import html, dcc
import a  # Supposé être un module personnalisé contenant des données ou des fonctions
import figure  # Supposé être un module personnalisé contenant des figures Plotly

# Enregistrement de la page dans l'application Dash
dash.register_page(__name__)

# Mise en page de la page Dash
layout = html.Div([
    # Section pour l'analyse des coups significatifs par catégories de poids
    html.Div([
        html.Br(),  # Espaces pour la mise en forme
        # Paragraphe expliquant l'objectif de la section
        html.P(
            children="On analyse l'évolution de la moyenne des coups significatifs par catégories de poids",
            className="hello",
        ),
        html.P(
            children="Les Heavyweights et Featherweights plus forts et plus lourds ont en moyenne la plus grande moyenne de coups significatifs",
            className="hello",
        ),
        html.Br(),  # Espaces pour la mise en forme
    ], className="header", style={"text_align": 'center', 'color': 'black', 'background-color': 'white'}),
    # Graphiques pour les catégories de poids
    html.Div(
        dcc.Graph(id="heatmap_men", figure=figure.heatmap1),
        style={"width": '47%', 'display': 'inline-block', 'margin': '5px'}
    ),
    html.Div(
        dcc.Graph(id="heatmap_women", figure=figure.heatmap2),
        style={"width": '47%', 'display': 'inline-block', 'margin': '5px'}
    ),
    html.Br(),

    # Section pour la comparaison des résultats entre tous les combats et les combats pour le titre
    html.Div([
        html.Br(),  # Espaces pour la mise en forme
        # Paragraphe expliquant l'objectif de la section
        html.P(
            children="On compare ici les résultats entre tous les combats et les combats pour le titre.",
            className="hello",
        ),
        html.Br(),  # Espaces pour la mise en forme
    ], className="header", style={"text_align": 'center', 'color': 'black', 'background-color': 'white'}),
    # Graphiques pour la comparaison
    html.Div(
        dcc.Graph(id="title_fight_graph", figure=figure.titlefig),
        style={"width": '47%', 'display': 'inline-block', 'margin': '5px'}
    ),
    html.Div(
        dcc.Graph(id="overall_fight_graph", figure=figure.Bar),
        style={"width": '47%', 'display': 'inline-block', 'margin': '5px'}
    ),

    # Section pour les détails des KOs/TKOs
    html.Div([
        html.Br(),  # Espaces pour la mise en forme
        # Paragraphe expliquant l'objectif de la section
        html.P(
            children="Contrairement à ce que l'on pourrait penser, les combats pour le titre sont ceux avec le plus grand pourcentage de KOs/TKOs",
            className="hello",
        ),
        html.Br(),  # Espaces pour la mise en forme
    ], className="header", style={"text_align": 'center', 'color': 'black', 'background-color': 'white'}),
    # Graphiques pour les KOs/TKOs
    html.Div(
        dcc.Graph(id="ko_tko_round_graph", figure=figure.fig7),
        style={"width": '67%', 'display': 'inline-block', 'margin': '5px'}
    ),
    html.Div(
        dcc.Graph(id="ko_tko_method_graph", figure=figure.fig5),
        style={"width": '25%', 'display': 'inline-block', 'margin': '5px'}
    ),
    html.Br(),

    # Section pour les méthodes de KOs/TKOs
    html.Div([
        html.Br(),  # Espaces pour la mise en forme
        # Paragraphes expliquant les méthodes de KOs/TKOs
        html.P(
            children="Quand il s'agit des KOs/TKOs, ils se finissent généralement par des coups de marteaux ou par rear naked choke.",
            className="hello",
        ),
        html.P(
            children="Notons que pour les KOs/TKOs, ceux-ci ont souvent lieu dès le premier round !",
            className="hello",
        ),
        html.Br(),  # Espaces pour la mise en forme
    ], className="header", style={"text_align": 'center', 'color': 'black', 'background-color': 'white'}),
    html.Br(),
])
