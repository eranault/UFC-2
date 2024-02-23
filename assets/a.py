import pandas as pd

# Chargement des données depuis un fichier CSV
df = pd.read_csv('ufc_R_projet.csv')



# Conversion de la colonne 'date' en format datetime et extraction de l'année
df['date'] = pd.to_datetime(df['date']).dt.year

# Préparation des données pour les combattants dans les coins bleu et rouge
df_b = df[['weight_class', 'date', 'B_avg_SIG_STR_pct']].dropna()
df_b.columns = ['weight_class', 'date', 'avg_SIG_STR_pct']

df_r = df[['weight_class', 'date', 'R_avg_SIG_STR_pct']].dropna()
df_r.columns = ['weight_class', 'date', 'avg_SIG_STR_pct']

# Fusion des données des combattants bleus et rouges
joined_data = pd.concat([df_r, df_b])

# Calcul de la moyenne des coups significatifs par catégorie de poids
avg_by_weight_class = pd.DataFrame(joined_data.groupby(['weight_class']).mean()['avg_SIG_STR_pct'])

# Ordonnancement des catégories de poids
new_order = ['Flyweight', 'Bantamweight', 'Featherweight', 'Lightweight', 'Welterweight', 'Middleweight', 'Light Heavyweight', 'Heavyweight', "Women's Strawweight", "Women's Flyweight", "Women's Bantamweight", "Women's Featherweight", 'Catch Weight']
avg_by_weight_class.index = pd.Categorical(avg_by_weight_class.index, categories=new_order, ordered=True)
avg_by_weight_class = avg_by_weight_class.reindex(new_order)
avg_by_weight_class = avg_by_weight_class.drop('Catch Weight')

# Séparation des données pour les hommes et les femmes
mens = avg_by_weight_class.loc[['Flyweight', 'Bantamweight', 'Featherweight', 'Lightweight', 'Welterweight', 'Middleweight', 'Light Heavyweight', 'Heavyweight']]
womens = avg_by_weight_class.loc[["Women's Strawweight", "Women's Flyweight", "Women's Bantamweight", "Women's Featherweight"]]

# Comptage des types de finitions
finish_count = pd.DataFrame(df.finish.value_counts()).reset_index().rename(columns={'index': 'Type of Finish', 'finish': 'Frequency of Finish'})
frequency_finish_sum = finish_count['Frequency of Finish'].sum()

# Analyse des stances des combattants
df_b1 = df[['B_Stance']].dropna()
df_r1 = df[['R_Stance']].dropna()
joined_data1 = pd.concat([df_r1, df_b1])
stance_countsB = df['B_Stance'].value_counts()
stance_countsR = df['R_Stance'].value_counts()

# Extraction des combattants uniques
fighters = list(set(df['R_fighter'].unique().tolist() + df['B_fighter'].unique().tolist()))

# Analyse des KOs par round
kos_by_round = df[['finish', 'finish_round']].query('finish == "KO/TKO"')
crosstab = pd.crosstab(kos_by_round['finish'], kos_by_round['finish_round'])

# Traitement des détails de finition
df["finish_details"] = df["finish_details"].fillna('No finish')
finish_det = df['finish_details'].loc[df['finish_details'] != 'No finish']
count_df = pd.DataFrame({'finish_details': finish_det})

# Correction des données de pays
cond = (df['country'].str[0] != ' ')
df['country_fixed'] = df['country'].where(cond, df['country'].str[1:])
n_countries = len(df['country_fixed'].unique())
labels = list(df['country_fixed'].unique())
size = df['country_fixed'].value_counts()

# Ordonnancement des catégories de poids pour le tri
weight_class_order = ["Women's Strawweight", "Women's Flyweight", "Women's Bantamweight", "Women's Featherweight", 'Flyweight', 'Bantamweight', 'Featherweight', 'Lightweight', 'Welterweight', 'Middleweight', 'Light Heavyweight', 'Heavyweight']
df['ordered_weight_class'] = pd.Categorical(df['weight_class'], weight_class_order)
data_sorted = df.sort_values('ordered_weight_class', ascending=False)

# Analyse des combats pour le titre
df_title_bout = df[df['title_bout'] == True]
finish_percentage = df_title_bout['finish'].value_counts(normalize=True) * 100

# Calcul des pourcentages de victoire par stance pour les coins bleu et rouge
win_percentage_by_stance = df_title_bout[df_title_bout['Winner'] == 'Blue'].groupby('B_Stance')['Winner'].count() / df_title_bout.groupby('B_Stance')['Winner'].count() * 100
win_percentage_by_stance = win_percentage_by_stance.reset_index().rename(columns={'Winner': 'Win Percentage'})

win_percentage_by_stanceR = df_title_bout[df_title_bout['Winner'] == 'Red'].groupby('R_Stance')['Winner'].count() / df_title_bout.groupby('R_Stance')['Winner'].count() * 100
win_percentage_by_stanceR = win_percentage_by_stanceR.reset_index().rename(columns={'Winner': 'Win Percentage'})

# Calcul des pourcentages de victoire pour les coins bleu et rouge
blue_win_percentage = (df['Winner'] == 'Blue').sum() / len(df) * 100
red_win_percentage = (df['Winner'] == 'Red').sum() / len(df) * 100
