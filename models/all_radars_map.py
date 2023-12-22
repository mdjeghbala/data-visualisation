import pandas as pd
import folium
from folium.plugins import MarkerCluster

# Lecture du fichier csv
radars_data = pd.read_csv("../assets/data/radars.csv", sep=';')

# Suppression des lignes avec des valeurs vides pour latitude ou longitude
radars_data = radars_data.dropna(subset=['latitude', 'longitude', 'vitesse_vehicule_legers_kmh'])

# Création de la carte folium avec clustering
radar_map = folium.Map(location=[radars_data['latitude'].mean(), radars_data['longitude'].mean()], zoom_start=5)
marker_cluster = MarkerCluster().add_to(radar_map)

# Ajout des marqueurs pour chaque radar
for index, row in radars_data.iterrows():
    # Ajout d'un marqueur pour chaque radar au cluster
    folium.Marker(
        location=[row['latitude'], row['longitude']],
        popup=f"Département: {row['departement']} \n Ville: {row['emplacement']} \n Vitesse max: {int(row['vitesse_vehicule_legers_kmh'])} km/h "
    ).add_to(marker_cluster)

# Enregistrement de la carte en tant que fichier HTML
radar_map.save("all_radars_map.html")
