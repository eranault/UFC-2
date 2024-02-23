import dash
from dash import html, dcc
import a  # Supposé être un module personnalisé contenant des données ou des fonctions
import figure  # Supposé être un module personnalisé contenant des figures Plotly

dash.register_page(__name__)

# Définition de la mise en page de la page web
layout = html.Div([
    # Section sur la garde des combattants
    html.Div([
        html.Br(),
        html.P(
            children="La garde de la majorité des combattants de l'ufc est orthodox : les southpaws et les switchs étant en minorité.",
            className="hello",
        ),
        html.Br(),
    ], className="header", style={"text_align": 'center', 'color': 'black', 'background-color': 'white'}),

    html.Br(),
    html.Br(),

    # Graphiques sur les gardes des combattants
    html.Div(
        dcc.Graph(id="nbreko_round_graph", figure=figure.fig3),
        style={"width": '45%', 'display': 'inline-block', 'margin': '5px'}
    ),
    html.Div(
        dcc.Graph(id="nbreko_round_graph", figure=figure.fig4),
        style={"width": '45%', 'display': 'inline-block', 'margin': '5px'}
    ),

    html.Br(),

    # Section sur le lien entre la garde et le pourcentage de victoire
    html.Div([
        html.Br(),
        html.P(
            children="Vient alors la question que tout pratiquant d'arts martiaux se pose !",
            className="hello",
        ),
        html.P(
            children="Il y a t-il un lien entre la Garde (Stance) et le pourcentage de victoire ?",
            className="hello",
        ),
        html.Br(),
    ], className="header", style={"text_align": 'center', 'color': 'black', 'background-color': 'white'}),

    html.Br(),

    # Graphiques sur le pourcentage de victoire en fonction de la garde
    html.Div(
        dcc.Graph(id="example_graph", figure=figure.BStance),
        style={"width": '45%', 'display': 'inline-block', 'margin': '5px'}
    ),
    html.Div(
        dcc.Graph(id="example_graph", figure=figure.RStance),
        style={"width": '45%', 'display': 'inline-block', 'margin': '5px'}
    ),
    html.Br(),

    # Section sur les observations des résultats
    html.Div([
        html.Br(),
        html.P(
            children="On remarque que ce ne sont non pas les southpaws mais les switchs qui ont le pourcentage de victoire le plus élevé.",
            className="hello",
        ),
        html.P(
            children="Deuxièmement remarquons que le côté le plus souvent victorieux est le corner Rouge. Ce qui est attendu : il s'agit généralement du corner du Champion/Combattant le plus expérimenté.",
            className="hello",
        ),
        html.Br(),
    ], className="header", style={"text_align": 'center', 'color': 'black', 'background-color': 'white'}),

    html.Br(),

    # Graphique sur le taux de victoire par corner
    html.Div(
        dcc.Graph(id="example_graph", figure=figure.CornerWinRate),
        style={"width": '75%', 'display': 'inline-block', 'margin': '5px'}
    ),

    html.Br(),
])
