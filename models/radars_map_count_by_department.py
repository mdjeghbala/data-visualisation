import pandas as pd
import folium
import branca.colormap as cm


class RadarMapCountByDepartment:
    def __init__(self, csv_path, output_file="radars_map_count_by_department.html"):
        """
        Initialise une instance de la classe RadarMapCountByDepartment.

        Paramètres:
        - csv_path (str): Le chemin vers le fichier CSV contenant les données des radars.
        - output_file (str): Le nom du fichier de sortie pour la carte générée (par défaut: "radars_map_count_by_department.html").
        """
        self.colormap = None  # Pour stocker la colormap
        self.radars_data = pd.read_csv(csv_path, sep=';', encoding='utf-8')  # Lecture des données du fichier CSV
        self.output_file = output_file  # Nom du fichier de sortie par défaut
        self._clean_data()  # Nettoyage des données
        self._aggregate_data()  # Agrégation des données

    def _clean_data(self):
        """
        Nettoie les données en supprimant les lignes avec des valeurs vides pour le département.
        """
        self.radars_data = self.radars_data.dropna(subset=['departement'])

    def _aggregate_data(self):
        """
        Agrège les données par département et compte le nombre de radars dans chaque département.
        """
        self.aggregated_data = self.radars_data.groupby('departement').size().reset_index(name='radar_count')

    def _create_colormap(self):
        """
        Crée une colormap en fonction du nombre de radars par département.
        """
        return cm.LinearColormap(['yellow', 'red'],
                                 vmin=min(self.aggregated_data['radar_count']),
                                 vmax=max(self.aggregated_data['radar_count']))

    def _add_markers(self, radar_map):
        """
        Ajoute des marqueurs (cercles) à la carte en fonction du nombre de radars par département.
        """
        for index, row in self.aggregated_data.iterrows():
            color_by_department = self.colormap(row['radar_count'])
            circle_radius = row['radar_count'] * 0.125

            folium.CircleMarker(
                location=[
                    self.radars_data.loc[self.radars_data['departement'] == row['departement'], 'latitude'].mean(),
                    self.radars_data.loc[self.radars_data['departement'] == row['departement'], 'longitude'].mean()],
                radius=circle_radius,
                color=color_by_department,
                fill=True,
                fill_color=color_by_department,
                fill_opacity=0.6,
                tooltip=f"Numéro département: {row['departement']} Nombre total radars: {row['radar_count']}"
            ).add_to(radar_map)

    def _add_legend(self, radar_map):
        """
        Ajoute une légende à la carte en fonction du nombre de radars par département.
        """
        self.colormap.caption = 'Nombre de radars par département'
        self.colormap.add_to(radar_map)

    def generate_radar_map(self, output_path="templates/radars_map_count_by_department.html"):
        """
        Génère une carte Folium avec des marqueurs représentant le nombre de radars par département et ajoute une légende.
        Le résultat est sauvegardé dans le fichier spécifié lors de l'initialisation.
        """
        self.colormap = self._create_colormap()

        radar_map = folium.Map(location=[self.radars_data['latitude'].mean(), self.radars_data['longitude'].mean()],
                               zoom_start=5)

        self._add_markers(radar_map)
        self._add_legend(radar_map)

        radar_map.save(output_path)
