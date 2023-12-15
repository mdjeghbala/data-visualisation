import pandas as pd
import folium
import branca.colormap as cm

# Lecture du fichier csv

radars_data = pd.read_csv("../radars.csv", sep=';')

# Suppression des départements contenant des valeurs vides
radars_data = radars_data.dropna(subset=['departement'])

# Agrégation des données par département (nombre total de radars par département)
aggregated_data = radars_data.groupby('departement').size().reset_index(name='radar_count')

# Création de la colormap du bleu au rouge selon le nombre de radars par département
colormap = cm.LinearColormap(['blue', 'red'], vmin=min(aggregated_data['radar_count']), vmax=max(aggregated_data['radar_count']))

# Création de la carte folium
radar_map = folium.Map(location=[radars_data['latitude'].mean(), radars_data['longitude'].mean()], zoom_start=6)

# Ajout des marqueurs pour les départements
for index, row in aggregated_data.iterrows():

    # Récupération de la couleur en fonction du nombre de radars dans le département
    color_by_department = colormap(row['radar_count'])

    # Calcul de la taille du cercle en fonction du nombre de radars
    circle_radius = row['radar_count'] * 0.125

    # Ajout d'un cercle coloré pour représenter le département avec le nombre de radars
    folium.CircleMarker(
        # Représentation du cercle à la moyenne des coordonnées géodésiques afin de le centrer
        location=[radars_data.loc[radars_data['departement'] == row['departement'], 'latitude'].mean(),
                  radars_data.loc[radars_data['departement'] == row['departement'], 'longitude'].mean()],
        radius=circle_radius,
        color=color_by_department,
        fill=True,
        fill_color=color_by_department,
        fill_opacity=0.6,  # Réduction de l'opacité pour mieux voir les cercles
        #  Affichage d'une pop up pour chaque département indiquant son numéro et le nombre total de radars
        popup=f"{row['departement']} Departement\nTotal radars: {row['radar_count']}"
    ).add_to(radar_map)

# Ajout de la légende de la colormap à la carte
colormap.caption = 'Nombre de radars par département'
colormap.add_to(radar_map)

