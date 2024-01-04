import pandas as pd
import plotly_express as px


class Histogramme:
    """
    Classe permettant de créer un histogramme basé sur les excès de vitesse à partir d'un fichier CSV.
    """
    # Constructeur de la classe Histogramme
    def __init__(self, fichier_csv):
        """
        Initialise une instance de la classe Histogramme.

        Paramètres:
        - fichier_csv (str): Le chemin vers le fichier CSV contenant les données des excès de vitesse  en km/h.
        """
        self.fichier_csv = fichier_csv

    # Fonction permettant d'avoir les excès de vitesse inférieur à 50km/h dans une série
    def extraction_exces_vitesse(self):
        """
        Extrait les excès de vitesse inférieurs ou égaux à 50 km/h à partir du fichier CSV.

        Returns:
        - pandas.Series: Une série contenant les excès de vitesse.
        """
        # on place les données du fichier CSV dans une DataFrame en prenant les 1 000 000 premières années
        data = pd.read_csv(self.fichier_csv, sep=';', nrows=1000000)

        # On sélectionne seulement les mesures de vitesse qui dépassent les limites du radar
        vitesse_sup_limite = data[data['mesure'] > data['limite']]

        # On calcule le nombre de km en excès et on place ça dans une nouvelle série
        exces_vitesse = vitesse_sup_limite['mesure'] - vitesse_sup_limite['limite']

        # On prend les excès inférieurs ou égals à 50 et on place ça dans une nouvelle série
        exces_vitesse_50 = exces_vitesse[exces_vitesse <= 50]

        return exces_vitesse_50

    # Fonction qui affiche l'histogramme sur les excès de vitesse
    def affiche_histo_exces_de_vitesse(self):
        """
        Affiche un histogramme des excès de vitesse inférieurs ou égaux à 50 km/h.

        Returns:
        - plotly.graph_objs.Figure: L'objet Figure de Plotly représentant l'histogramme.
        """
        # Series contenant les excès de vitesse inférieurs ou égals à 50km/h
        exces_vitesse_50 = self.extraction_exces_vitesse()

        # Création de l'histogramme
        fig = px.histogram(
            x=exces_vitesse_50,  # Série sur laquelle est basée l'histogramme
            nbins=10,  # Nombre de tranches
            range_x=[0, 50],  # Etendue de la tranche
            title='Histogramme sur les excès de vitesse <br> par tranche de 5 km/h de 0-50 km/h',
            # Titre de l'histogramme
            labels={'x': 'Excès de vitesse (km/h)'},  # Noms de l'axe des abscisses
            color_discrete_sequence=['#78B7C5'],  # Couleur des barres
        )

        # Permet le formattage des barres
        fig.update_traces(marker_line_color='gray', marker_line_width=1,
                          xbins=dict(start=0.5, end=49.5, size=5))

        # Donne un nom à l'axe des ordonnées et ajuste le titre
        fig.update_layout(yaxis_title='Nombre de véhicules',
                          title=dict(
                              text='Histogramme sur les excès de vitesse<br>par tranche de 5 km/h de 0-50 km/h',
                              x=0.5,  # Met le titre au centre
                              y=0.9,  # Met le titre en haut
                              xanchor='center',
                              yanchor='top',
                          )
                          )

        return fig
