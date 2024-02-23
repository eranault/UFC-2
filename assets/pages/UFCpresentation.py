import dash
from dash import html, dcc
import figure  # Supposé être un module personnalisé contenant des figures Plotly

dash.register_page(__name__, path='/')

# Définition de la mise en page de la page web
layout = html.Div([
    # Introduction à l'UFC
    html.Div(children=[
        html.Br(),
        html.P(
            children="The Ultimate Fighting Championship (UFC) is recognized as the premier organization in mixed martial arts, drawing top fighters from across the globe to compete in the octagon.",
            className="hello",
        ),
        html.P(
            children="we embark on a detailed examination of the intricate relationship between various parameters, including reach, age, and other factors, and how they impact the success and performance of UFC fighters.",
            className="hello",
        ),
        html.P(
            children="This exploration holds significance not only for fight enthusiasts and practitioners but also for researchers and sports analysts in pursuit of a deeper understanding of the elements that contribute to success within the UFC.",
            className="hello",
        ),
        html.Br(),
    ], className="header", style={"text_align": 'center', 'color': 'white', 'background-color': '#1A1A1D'}),

    html.Br(),

    # Contenu de la page
    html.Div(id='page-1-content'),
    html.Br(),

    # Carte de répartition des emplacements des combats
    html.Div([
        html.H1(
            children="Carte de Répartition des emplacements des Combats",
            className="hello",
        ),
        dcc.Graph(id="Map", figure=figure.map),
    ]),
    html.Br(),

    # Informations supplémentaires sur la répartition géographique des combats
    html.Div([
        html.P(
            children="L'UFC une division d'origine américaine développe ses premiers combats aux ÉTATS-UNIS: il s'agit de l'endroit ou le plus grand nombre de combat sont produits.",
            className="hello",
        ),
        html.Br(),
    ], className="header", style={"text_align": 'center', 'color': 'black', 'background-color': 'white'}),

    # Graphiques supplémentaires
    html.Div(
        dcc.Graph(id="nbreko_round_graph", figure=figure.fig8),
        style={"width": '70%', 'display': 'inline-block', 'margin': '5px'}
    ),
    html.Div(
        dcc.Graph(id="nbrfightyear", figure=figure.NbrFightsY),
        style={"width": '27%', 'display': 'inline-block', 'margin': '5px'}
    ),
    html.Br(),

    # Autres graphiques et visualisations
    html.Div(
        dcc.Graph(id="nbreko_round_graph", figure=figure.fig11),
        style={"width": '100%', 'display': 'inline-block', 'margin': '5px'}
    ),
    html.Div(
        dcc.Graph(id="example_graph", figure=figure.Bar),
        style={"width": '30%', 'display': 'inline-block', 'margin': '5px'}
    ),
    html.Div(
        dcc.Graph(id="nbreko_round_graph", figure=figure.fig9),
        style={"width": '30%', 'display': 'inline-block', 'margin': '5px'}
    ),
    html.Div(
        dcc.Graph(id="nbreko_round_graph", figure=figure.fig10),
        style={"width": '30%', 'display': 'inline-block', 'margin': '5px'}
    ),
    html.Br(),

    # Section sur les catégories de poids et les résultats des combats
    html.Div([
        html.P(
            children="Remarquons que chaque combats de l'UFC est organisé par catégories de poids. On distingue ainsi diverses catégories : allant de Flyweight à Heavyweight pour les hommes et de Strawweight à Featherweight pour les femmes.",
            className="hello",
        ),
        html.P(
            children="L'issue des combats est déterminée par : Unanimous Decision, KO/TKO, Split Decision, Majority Decision, un DQ ou un No Contest/Overturned.",
            className="hello",
        ),
        html.P(
            children="Les combattants sont répartis selon le corner Rouge et le corner Bleu. Notons que le pari sur le résultat du combat est une pratique courante chez les adeptes de l'UFC. Le max est du côté négatif du combattant rouge, c'est généralement le favoris du public ou l'ancien champion.",
            className="hello",
        ),
        html.Br(),
    ], className="header", style={"text_align": 'center', 'color': 'black', 'background-color': 'white'}),

    html.Br(),
], style={"width": '100%', 'background-color': '#f2f3f4', 'margin-left': '0', 'margin-right': '0', 'verticalAlign': 'middle', 'height': '100%', 'top': '0px', 'left': '0px', 'z-index': '1000'})

