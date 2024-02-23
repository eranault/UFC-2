import dash
from dash import html, dcc, callback, Input, Output
import a  # Supposé être un module personnalisé contenant des données ou des fonctions
import figure  # Supposé être un module personnalisé contenant des figures Plotly
import pandas as pd
import plotly.express as px

# Enregistrement de la page dans l'application Dash
dash.register_page(__name__)

# Couleurs pour les détails des combattants
detail_colors = ['#1C1C1C', '#1C1C1C', '#1C1C1C', '#1C1C1C', '#1C1C1C','#1C1C1C']

# Callback pour mettre à jour les détails du combattant sélectionné
@callback(
    Output('fighter-details', 'children'),
    [Input('fighter-dropdown', 'value')]
)
def update_fighter_details(selected_fighter):
    """
    Met à jour les détails du combattant sélectionné pour afficher dans une application Dash.

    Parameters:
    - selected_fighter (str): Le nom du combattant sélectionné.

    Returns:
    - cards (List[dash_html_components._components.Div]): Une liste de composants HTML représentant les détails du combattant.
    """
    
    # Filtrer le DataFrame pour le combattant sélectionné
    fighter_details = a.df[(a.df['R_fighter'] == selected_fighter) | (a.df['B_fighter'] == selected_fighter)]
    fighter_details = fighter_details.sort_values(by='date', ascending=False)
    latest_details = fighter_details.iloc[-1]  # Dernière entrée

    # Calculer les victoires et les défaites
    win_count, lose_count = 0, 0
    for index, row in a.df.iterrows():
        winner = row['Winner']
        if (winner == 'Red' and row['R_fighter'] == selected_fighter) or (winner == 'Blue' and row['B_fighter'] == selected_fighter):
            win_count += 1
        elif (winner == 'Blue' and row['R_fighter'] == selected_fighter) or (winner == 'Red' and row['B_fighter'] == selected_fighter):
            lose_count += 1

    # Extraire les détails requis
    details = {
        'Height': latest_details['R_Height_cms'] if latest_details['R_fighter'] == selected_fighter else latest_details['B_Height_cms'],
        'Reach': latest_details['R_Reach_cms'] if latest_details['R_fighter'] == selected_fighter else latest_details['B_Reach_cms'],
        'Weight Class': latest_details['weight_class'],
        'Gender': latest_details['gender'],
        'Wins': win_count,
        'Losses': lose_count,
    }

    # Créer des cartes colorées pour le combattant sélectionné
    cards = [html.Div([
                html.H3(key),
                html.Ul([html.Li(f"{key}: {value}")]),
            ], style={'color':'white','background-color': detail_colors[i], 'padding': '10px', 'margin-bottom': '20px','margin': '20px'})
            for i, (key, value) in enumerate(details.items())]
    return cards

# Dropdown pour sélectionner un combattant
fighter_dropdown2 = dcc.Dropdown(
    id='fighter-dropdown2',
    options=[{'label': fighter, 'value': fighter} for fighter in a.fighters],
    value=a.fighters[0]  # Sélection par défaut
)

# Callback pour mettre à jour le graphique en camembert des types de finitions
@callback(
    Output('finish-type-chart', 'figure'),
    [Input('fighter-dropdown2', 'value')]
)
def update_finish_chart(selected_fighter):
    """
    Met à jour un graphique en camembert montrant la distribution des types de finitions pour un combattant sélectionné.

    Parameters:
    - selected_fighter (str): Le nom du combattant sélectionné.

    Returns:
    - pie_chart (plotly.graph_objs._pie.Pie): Le graphique en camembert mis à jour.
    """
    
    # Filtrer les données pour le combattant sélectionné
    selected_fighter_wins_df = a.df[((a.df['Winner'] == 'Red') & (a.df['R_fighter'] == selected_fighter)) | 
                                    ((a.df['Winner'] == 'Blue') & (a.df['B_fighter'] == selected_fighter))]
    total_fighter_wins = len(selected_fighter_wins_df)

    # Statistiques des types de finitions
    finishing_stats = {}
    for index, row in selected_fighter_wins_df.iterrows():
        finish = row['finish']
        if finish in finishing_stats:
            finishing_stats[finish]['count'] += 1
        else:
            finishing_stats[finish] = {'count': 1, 'total': 0}

    # Calcul du pourcentage pour chaque type de finition
    for finish_type, stats in finishing_stats.items():
        stats['total'] = total_fighter_wins
        stats['percentage'] = (stats['count'] / stats['total']) * 100

    # Création d'un DataFrame pour la distribution des types de finitions
    finish_counts = pd.Series(finishing_stats).reset_index()
    finish_counts.columns = ['Type de Finish', 'Stats']
    finish_data = {
        'Type de Finish': finish_counts['Type de Finish'],
        'Pourcentage': finish_counts['Stats'].apply(lambda stats: stats['percentage'])
    }

    # Création du graphique en camembert
    pie_chart = px.pie(finish_data, names='Type de Finish', values='Pourcentage')
    pie_chart.update_layout(title_text='Distribution du type de Finish pour les victoires du combattant')
    return pie_chart




# Définition de la mise en page de la page web
layout = html.Div([
    # Section pour choisir un combattant
    html.Div([
        html.Br(),
        html.P(
            children="Choisissez votre combattant !",
            className="hello",
        ),
        html.Br(),
    ], className="header", style={"text_align": 'center', 'color': 'black', 'background-color': 'white'}),
    
    html.Br(),

    # Dropdown pour sélectionner un combattant et affichage des détails
    html.Div([
        dcc.Dropdown(
            id='fighter-dropdown',
            options=[{'label': fighter, 'value': fighter} for fighter in a.fighters],
            value=a.fighters[0]  # Valeur par défaut
        ),
        html.Div(id='fighter-details', style={'display': 'flex', 'flex-wrap': 'wrap'}),
        dcc.Dropdown(  # Deuxième dropdown, probablement défini ailleurs dans le code
            id='fighter-dropdown2',
            options=[{'label': fighter, 'value': fighter} for fighter in a.fighters],
            value=a.fighters[0]  # Valeur par défaut
        ),
        dcc.Graph(id='finish-type-chart')  # Graphique pour les types de finitions
    ], style={
        'width': '100%',
        'border': '1px solid #ccc',
        'border-radius': '5px',
        'padding': '5px',
        'background-color': '#f5f5f5',
        'color': '#333',
        'font-size': '16px'
    }),

    # Graphique montrant la répartition géographique des combattants
    html.Div(
        dcc.Graph(id="homemap", figure=figure.home),
    ),

    # Section informative sur la répartition géographique des combattants
    html.Div([
        html.Br(),
        html.P(
            children="La majorité des combattants viennent des USA, du Brésil, du Canada et de la Russie !",
            className="hello",
        ),
        html.P(
            children="La présence du Brésil en 2nd position peut s'expliquer par l'omniprésence du ju jitsu brésilien au Brésil !",
            className="hello",
        ),
        html.Br(),
    ], className="header", style={"text_align": 'center', 'color': 'black', 'background-color': 'white'}),
])
