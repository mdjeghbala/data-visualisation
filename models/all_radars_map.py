import pandas as pd
import folium
from folium.plugins import MarkerCluster


class AllRadarsMap:
    """
    Classe pour générer une carte Folium avec un cluster de marqueurs représentant tous les radars.

    Attributs:
    - radars_data (pd.DataFrame): Les données des radars à afficher sur la carte.

    Methodes:
    - __init__(csv_path: str): Initialise une instance de la classe.
    - _clean_data(): Nettoie les données en supprimant les lignes avec des valeurs vides.
    - _create_marker_cluster(map_obj: folium.Map): Crée un cluster de marqueurs sur la carte.
    - generate_map(output_path: str = "templates/all_radars_map.html"): Génère et enregistre la carte en tant que fichier HTML.
    """
    def __init__(self, csv_path):
        """
        Initialise une instance de la classe AllRadarsMap.

        Paramètres:
        - csv_path (str): Le chemin vers le fichier CSV contenant les données des radars.
        """
        self.radars_data = pd.read_csv(csv_path, sep=';', encoding='utf-8')
        self._clean_data()

    def _clean_data(self):
        """
        Nettoie les données en supprimant les lignes avec des valeurs vides pour latitude, longitude,
        et vitesse_vehicule_legers_kmh.
        """
        self.radars_data = self.radars_data.dropna(subset=['latitude', 'longitude', 'vitesse_vehicule_legers_kmh'])

    def _create_marker_cluster(self, map_obj):
        """
        Crée un cluster de marqueurs sur la carte en fonction des données des radars.

        Paramètres:
        - map_obj (folium.Map): L'objet carte Folium sur lequel les marqueurs seront ajoutés.
        """
        marker_cluster = MarkerCluster().add_to(map_obj)
        for index, row in self.radars_data.iterrows():
            # Ajout d'un marqueur pour chaque radar au cluster
            folium.Marker(
                location=[row['latitude'], row['longitude']],
                tooltip=f"Numéro département: {row['departement']} Ville: {row['emplacement']} Vitesse max: {int(row['vitesse_vehicule_legers_kmh'])} km/h"
            ).add_to(marker_cluster)

    def generate_map(self, output_path="templates/all_radars_map.html"):
        """
        Génère une carte Folium avec un cluster de marqueurs représentant tous les radars et enregistre la carte en
        tant que fichier HTML.

        Paramètres:
        - output_path (str): Le nom du fichier de sortie pour la carte générée (par défaut: "templates/all_radars_map.html").
        """
        radar_map = folium.Map(
            location=[self.radars_data['latitude'].mean(), self.radars_data['longitude'].mean()],
            zoom_start=5
        )

        # Appel de la méthode pour créer le cluster de marqueurs
        self._create_marker_cluster(radar_map)

        # Enregistrement de la carte en tant que fichier HTML
        radar_map.save(output_path)
