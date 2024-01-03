import pandas as pd
import folium
from folium.plugins import MarkerCluster


class AllRadarsMap:
    def __init__(self, csv_path):
        # Initialisation de la classe avec le chemin du fichier CSV
        self.radars_data = pd.read_csv(csv_path, sep=';', encoding='utf-8')
        self._clean_data()

    def _clean_data(self):
        # Méthode pour nettoyer les données : suppression des lignes avec des valeurs vides pour latitude, longitude, et vitesse_vehicule_legers_kmh
        self.radars_data = self.radars_data.dropna(subset=['latitude', 'longitude', 'vitesse_vehicule_legers_kmh'])

    def _create_marker_cluster(self, map_obj):
        # Méthode pour créer un cluster de marqueurs sur la carte
        marker_cluster = MarkerCluster().add_to(map_obj)
        for index, row in self.radars_data.iterrows():
            # Ajout d'un marqueur pour chaque radar au cluster
            folium.Marker(
                location=[row['latitude'], row['longitude']],
                tooltip=f"Numéro département: {row['departement']} \n Ville: {row['emplacement']} \n Vitesse max: {int(row['vitesse_vehicule_legers_kmh'])} km/h "
            ).add_to(marker_cluster)

    def generate_map(self, output_path="all_radars_map.html"):
        # Méthode pour générer la carte et l'enregistrer en tant que fichier HTML
        radar_map = folium.Map(
            location=[self.radars_data['latitude'].mean(), self.radars_data['longitude'].mean()],
            zoom_start=5
        )

        # Appel de la méthode pour créer le cluster de marqueurs
        self._create_marker_cluster(radar_map)

        # Enregistrement de la carte en tant que fichier HTML
        radar_map.save(output_path)


# Utilisation de la classe
radar_map_generator = AllRadarsMap("../assets/data/radars.csv")
radar_map_generator.generate_map()
