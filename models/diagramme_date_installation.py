import pandas as pd
import plotly.express as px


class DiagrammeDate:
    """
    Classe permettant de créer un diagramme basé sur les dates d'installation des radars à partir d'un fichier CSV.
    """
    # Constructeur de la classe DiagrammeDate
    def __init__(self, fichier_csv):
        """
        Initialise une instance de la classe DiagrammeDate.

        Paramètres:
        - fichier_csv (str): Le chemin vers le fichier CSV contenant les données des radars.
        """
        self.fichier_csv = fichier_csv

    # Fonction permettant d'avoir une série avec seulement la date d'installation
    def extraction_annee(self):
        """
        Extrait les années d'installation des radars à partir du fichier CSV.

        Returns:
        - pandas.Series: Une série contenant les années d'installation.
        """
        # On place les données du fichier CSV dans une DataFrame
        data = pd.read_csv(self.fichier_csv, sep=';')

        # On crée une Série qui est basée sur une colonne de la DataFrame
        date = data['date_installation']

        # On convertit la colonne représentant la date d'installation dans un format de date/heure facilitant l'analyse des données
        date = pd.to_datetime(date, format='%Y-%m-%dT%H:%M:%SZ')

        # Crée une nouvelle colonne "annee" qui extrait les années de "date"
        data['annee'] = date.dt.year

        return data['annee']

    # Fonction qui affiche le diagramme sur les dates d'installation
    def affiche_diagramme_date_install(self):
        """
        Affiche un diagramme montrant le nombre de radars installés par année.

        Returns:
        - plotly.graph_objs.Figure: L'objet Figure de Plotly représentant le diagramme.
        """
        data = pd.read_csv('assets/data/radars.csv', sep=';')
        data['annee'] = self.extraction_annee()

        # Création de l'histogramme
        fig = px.histogram(
            data_frame=data,
            x='annee',
            title='Diagramme montrant le nombre de radars installés par année',
            labels={'annee': 'Année de création'},
            color_discrete_sequence=['#78B7C5']
        )

        # Permet le formattage des barres
        fig.update_traces(marker_line_color='gray', marker_line_width=1)

        # Donne un nom à l'axe des ordonnées et ajuste le titre
        fig.update_layout(yaxis_title='Nombre de radars',
                          title=dict(
                              text='Diagramme montrant le nombre de radars installés par année',
                              x=0.5,  # Met le titre au centre
                              y=0.9,  # Met le titre en haut
                              xanchor='center',
                              yanchor='top',
                          )
                          )

        # Permet de formatter l'axe des abscisses en affichant une année sur deux
        annee_unique = data['annee'].unique()
        annee_impaire = [annee for annee in annee_unique if annee % 2 != 0]
        fig.update_xaxes(tickvals=annee_impaire)

        return fig
