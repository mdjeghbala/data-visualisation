import pandas as pd
import plotly.express as px


class DiagrammeVitesse:
    """
    Classe permettant de créer un diagramme basé sur les vitesses maximales des radars routiers en France.

    Attributs:
    - fichier_csv (str): Le chemin vers le fichier CSV contenant les données des radars.

    Methodes:
    - __init__(fichier_csv: str): Initialise une instance de la classe.
    - affiche_diagramme_vitesse_max(): Affiche un diagramme analysant les vitesses maximales des radars routiers en France.
    """
    # Constructeur de la classe DiagrammeVitesse
    def __init__(self, fichier_csv):
        """
        Initialise une instance de la classe DiagrammeVitesse.

        Paramètres:
        - fichier_csv (str): Le chemin vers le fichier CSV contenant les données des radars.
        """
        self.fichier_csv = fichier_csv

    # Fonction qui affiche le diagramme sur les vitesses max des radars
    def affiche_diagramme_vitesse_max(self):
        """
        Affiche un diagramme analysant les vitesses maximales des radars routiers en France.

        Returns:
        - plotly.graph_objs.Figure: L'objet Figure de Plotly représentant le diagramme.
        """
        # On place les données du fichier CSV dans une DataFrame
        radars = pd.read_csv(self.fichier_csv, sep=';')

        # On renomme la colonne pour une appelation plus courte et explicite
        radars = radars.rename(columns={'vitesse_vehicule_legers_kmh': 'vitesse_max'})

        # On supprime les lignes où la vitesse n'est pas renseignée (NaN)
        radars = radars.dropna(subset=['vitesse_max'])

        # Création de l'histogramme
        fig = px.histogram(
            radars,
            x='vitesse_max',
            nbins=10,
            title='Diagramme analysant les vitesses maximales des radars routiers en France',
            labels={'vitesse_max': 'Vitesse maximale (km/h)'},
            color_discrete_sequence=['#78B7C5'],
            height=450
        )

        # Permet le formattage des barres
        fig.update_traces(marker_line_color='black', marker_line_width=1)

        # Donne un nom à l'axe des ordonnées et ajuste le titre
        fig.update_layout(yaxis_title='Nombre de radars',
                          title=dict(
                              text='Diagramme analysant les vitesses maximales des radars routiers en France',
                              x=0.5,  # Met le titre au centre
                              y=0.9,  # Met le titre en haut
                              xanchor='center',
                              yanchor='top',
                          )
                          )

        return fig
