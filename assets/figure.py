# Importation des bibliothèques nécessaires
import plotly.express as px  # Pour la visualisation de données
import pandas as pd  # Pour la manipulation de données
import a
# Création d'un graphique en barres pour visualiser la distribution des stances (B)
fig3 = px.bar(x=a.stance_countsB.index, y=a.stance_countsB.values, labels={'x': 'Stance', 'y': 'Count'})
fig3.update_traces(marker_color='skyblue')  # Définit la couleur des barres en bleu ciel
fig3.update_xaxes(categoryorder='total ascending')  # Trie les catégories par ordre croissant
fig3.update_layout(xaxis_tickangle=-45)  # Incline les étiquettes de l'axe des x
fig3.update_xaxes(title_text='Stance')  # Titre de l'axe des x
fig3.update_yaxes(title_text='Count')  # Titre de l'axe des y
fig3.update_layout(title_text='Distribution des Gardes')  # Titre du graphique

# Répétition du processus pour un autre ensemble de données (R)
fig4 = px.bar(x=a.stance_countsR.index, y=a.stance_countsR.values, labels={'x': 'Stance', 'y': 'Count'})
fig4.update_traces(marker_color='red')  # Définit la couleur des barres en rouge
# Les autres mises à jour sont similaires à fig3

# Création d'un graphique en barres empilées pour les KO finis par round
fig5 = px.bar(a.crosstab, barmode='stack')
fig5.update_xaxes(title_text='Round')  # Titre de l'axe des x
fig5.update_yaxes(title_text='Count')  # Titre de l'axe des y
fig5.update_layout(title_text='Nombre de KO moyen par round')  # Titre du graphique

# Graphique en barres montrant le nombre de KO par round
ko_round = px.bar(a.kos_by_round, x='finish_round', title='Nombre total de KO par round',
                  labels={'finish_round': 'Round number', 'count': 'KOs'})

# Graphique en barres pour les détails de finition
fig7 = px.bar(a.count_df, x='finish_details', title='Détails de finition', labels={'finish_details': 'Finish Details', 'count': 'Count'})
fig7.update_xaxes(categoryorder='total ascending')  # Trie les catégories par ordre croissant
# Les autres mises à jour sont similaires aux graphiques précédents

# Graphique en secteurs montrant les lieux des combats de l'UFC
colors = px.colors.qualitative.Set1  # Définit un ensemble de couleurs
fig8 = px.pie(names=a.labels, values=a.size, color=a.labels, color_discrete_sequence=colors,
              hole=0.4, title='Lieux de déroulement des combats')
fig8.update_layout(width=800, height=600)  # Ajuste la taille du graphique

# Création d'une carte géographique montrant les lieux des événements de l'UFC
location_freq = a.df.groupby(['latitude', 'longitude']).size().reset_index(name='frequency')
df = a.df.merge(location_freq, on=['latitude', 'longitude'])
map = px.scatter_geo(df, lat="latitude", lon="longitude", size="frequency", hover_name="location",
                     color="frequency", color_continuous_scale=['grey', 'red'], projection="natural earth",
                     title="Répartition des fréquences des lieux")
# Personnalisation de la carte
map.update_layout(
    margin={"r":0,"t":0,"l":0,"b":0},
    geo=dict(
        showland=True, landcolor="white", countrycolor="grey", showlakes=True, lakecolor="grey",
        showocean=True, oceancolor="black"
    )
)

# Lecture des données depuis un fichier CSV
df1 = pd.read_csv('Hometown.csv')

# Calcul de la fréquence des origines des combattants
freq_df = pd.concat([df1['R_nat'].value_counts(), df1['B_nat'].value_counts()], axis=1).fillna(0)
freq_df.columns = ['R_nat_frequency', 'B_nat_frequency']
freq_df.reset_index(inplace=True)
freq_df.rename(columns={'index': 'location'}, inplace=True)

# Création d'une autre carte géographique pour les origines des combattants
home = px.scatter_geo(freq_df, locations="location", locationmode="country names", size="R_nat_frequency",
                      color_continuous_scale="solar", projection="natural earth",
                      title="Répartition des Origines des Combattants")
home.update_geos(resolution=110, showcoastlines=True, coastlinecolor="Black", showland=True, landcolor="white")
# Ajout d'une trace supplémentaire pour B_nat
home.add_trace(px.scatter_geo(freq_df, locations="location", locationmode="country names", size="B_nat_frequency",
                              color_continuous_scale="solar", projection="natural earth").data[0])

import plotly.express as px  # Importation de Plotly Express pour la visualisation

# Histogrammes pour la distribution des cotes des combattants dans les coins bleu et rouge
fig9 = px.histogram(df, x="B_odds", title="Distribution de la cote du combattant B (Blue Corner)")
fig10 = px.histogram(df, x="R_odds", title="Distribution de la cote du combattant  R (Red Corner)")
# Ces histogrammes montrent la distribution des cotes pour les combattants dans les coins bleu et rouge.

# Graphique en barres pour le nombre de combats par catégorie de poids, coloré par genre
fig11 = px.bar(a.data_sorted, y='ordered_weight_class', title='Nombre de combats par catégories de poids',
               labels={'ordered_weight_class': 'Ordered Weight Class', 'index': 'Number of Fights'}, color=a.data_sorted['gender'])
fig11.update_layout(height=800)  # Ajustement de la hauteur du graphique

# Heatmaps pour les pourcentages de coups significatifs chez les hommes et les femmes
heatmap1 = px.imshow(a.mens, color_continuous_scale="Greens", title='Pourcentage de frappes significatives (hommes)')
heatmap2 = px.imshow(a.womens, color_continuous_scale="peach", title='Pourcentage de frappes significatives (femmes)')


# Calcul du pourcentage de types de finitions pour tous les combats

finish_percentage_all = (df['finish'].value_counts(normalize=True) * 100).reset_index().rename(columns={'proportion': 'Percentage of Finish', 'finish': 'Type_of_Finish'})



# Graphique en barres pour les pourcentages de types de finitions

Bar = px.bar(x=finish_percentage_all['Percentage of Finish'], y=finish_percentage_all['Type_of_Finish'],

labels={'x': 'Pourcentage', 'y': 'Type de Finish'},

title='Pourcentage de "finish" pour l\'ensemble des données',

color_discrete_sequence=['blue'])


# Graphique en barres pour le nombre de combats par année
NbrFightsY = px.bar(df['date'].value_counts().reset_index(), x=df['date'].value_counts().index, y='date', title='Nombres de combats par an')
NbrFightsY.update_xaxes(type='category', categoryorder='total ascending', title_text='Year')
NbrFightsY.update_yaxes(title_text='Number of Matches')

# Graphiques en nuage de points pour la relation entre l'âge et les coups significatifs atterris/takedowns réussis
strikeB = px.scatter(df, x='B_age', y='B_avg_SIG_STR_landed', color='B_fighter', title='Relation entre l\'âge et le nombre moyen de coups significatifs atterris (combattants B)', labels={'B_age': 'Âge', 'B_avg_SIG_STR_landed': 'Moyenne de coups significatifs atterris'}, hover_data=['B_fighter'])
strikeR = px.scatter(df, x='R_age', y='R_avg_SIG_STR_landed', color='R_fighter', title='Relation entre l\'âge et le nombre moyen de coups significatifs atterris (combattants R)', labels={'R_age': 'Âge', 'R_avg_SIG_STR_landed': 'Moyenne de coups significatifs atterris'}, hover_data=['R_fighter'])
takedownB = px.scatter(df, x='B_age', y='B_avg_TD_landed', color='B_fighter', title='Relation entre l\'âge et le nombre moyen de takedown réussis (combattants B)', labels={'B_age': 'Âge', 'B_avg_TD_landed': 'Moyenne de takedown réussis'}, hover_data=['B_fighter'])
takedownR = px.scatter(df, x='R_age', y='R_avg_TD_landed', color='R_fighter', title='Relation entre l\'âge et le nombre moyen de takedown réussis (combattants R)', labels={'R_age': 'Âge', 'R_avg_TD_landed': 'Moyenne de takedown réussis'}, hover_data=['R_fighter'])

# Graphiques en barres pour les pourcentages de finitions et de victoires par stance
titlefig = px.bar(x=a.finish_percentage.index, y=a.finish_percentage.values, labels={'x': 'Type de Finish', 'y': 'Pourcentage'}, title='Pourcentage de "finish" pour title_bout=True', color_discrete_sequence=['orange'])
BStance = px.bar(x=a.win_percentage_by_stance['B_Stance'], y=a.win_percentage_by_stance['Win Percentage'], labels={'x': 'B_Stance', 'y': 'Pourcentage de victoire'}, title='Pourcentage de victoire des combattants B par stance (B_Stance)', color_discrete_sequence=['green'])
RStance = px.bar(x=a.win_percentage_by_stanceR['R_Stance'], y=a.win_percentage_by_stanceR['Win Percentage'], labels={'x': 'R_Stance', 'y': 'Pourcentage de victoire'}, title='Pourcentage de victoire des combattants R par stance (R_Stance)', color_discrete_sequence=['red'])

# Graphique en barres pour le taux de victoire par coin (Blue et Red)
CornerWinRate = px.bar(x=['Blue', 'Red'], y=[a.blue_win_percentage, a.red_win_percentage], labels={'x': 'Combattant', 'y': 'Pourcentage de victoire'}, title='Pourcentage de victoire des combattants Blue et Red')



