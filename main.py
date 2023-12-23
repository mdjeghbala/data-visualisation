from dash import Dash, dcc, html
from models.diagramme_date_installation import DiagrammeDate
from models.diagramme_vitesse_max import DiagrammeVitesse
from models.histogramme_exces_de_vitesse import Histogramme

if __name__ == '__main__':
    # Création de l'application du dashboard
    app = Dash(__name__)

    # Création de l'histogramme
    histogramme = Histogramme('assets/data/opendata-vitesse.csv')
    fig_histogramme = histogramme.affiche_histo_exces_de_vitesse()

    # Création des diagrammes
    diagramme_vitesse = DiagrammeVitesse('assets/data/radars.csv')
    fig_diagramme_vi = diagramme_vitesse.affiche_diagramme_vitesse_max()
    diagramme_date = DiagrammeDate('assets/data/radars.csv')
    fig_diagramme_da = diagramme_date.affiche_diagramme_date_install()


    # Définir la couleur de fond du body
    app.layout = html.Div(style={'backgroundColor': '#20283E'}, children=[
        html.Div(
            style={
                "backgroundColor": "#4B587B",
                "color": "#ffffff",
                "padding": "10px",
                "display": "flex",
                "alignItems": "center",
                "justifyContent": "space-between",
            },
            children=[
                html.Img(
                    src="assets/radar.png",
                    width="90px",
                    height="115px",
                ),
                html.Div(
                    [
                        html.Div(
                            [
                                html.H1(
                                    "Dashboard :",
                                    style={
                                        "font-size": "1.8em",
                                        "text-align": "center"
                                    }
                                ),
                                html.Div(
                                    "VISUALISATION DES RADARS",
                                    style={
                                        "backgroundColor": "#4B587B",
                                        "borderRadius": "15px",
                                        "padding": "10px",
                                        "margin-top": "5px",
                                        "width": "fit-content",
                                        "box-shadow": "2px 2px 5px 2px rgba(0, 0, 0, 0.2)",
                                        "font-size": "2em"  # Taille du texte augmentée
                                    }
                                ),
                            ],
                            style={"display": "flex", "flexDirection": "column", "alignItems": "center"}
                        ),
                    ],
                ),
                html.Img(
                    src="assets/radar.png",
                    width="90px",
                    height="115px",
                ),
            ],
        ),

        html.Div(
            [
                html.Div(
                    [
                        "Ce DashBoard vous propose de visualiser l'ensemble des radars dont la France dispose, que ce soit en France métropolitaine ou en France d'outre-mers.",
                        html.Br(),
                        "Vous pourrez observer le nombre de radars par département, leur emplacement et quelques statistiques assez intéressantes!"
                    ],
                    style={
                        "backgroundColor": "#4B587B",
                        "color": "#ffffff",  # Couleur du texte en blanc
                        "borderRadius": "15px",
                        "padding": "10px",
                        "margin": "auto",
                        "marginTop": "20px",
                        "width": "fit-content",
                        "box-shadow": "2px 2px 5px 2px rgba(0, 0, 0, 0.2)",
                        "text-align": "center"  # Centrage du texte à l'intérieur du rectangle
                    }
                ),
            ]
        ),

        html.Div([
            html.Div("Le nombre de radars par département",
                     style={'color': 'white', 'font-size': '30px', 'margin': 'auto'}),
            html.Div("Position de tous les radars",
                     style={'color': 'white', 'font-size': '30px', 'margin': 'auto'}),
        ], style={'display': 'flex', 'justifyContent': 'space-between', 'margin': '20px'}),

        # Conteneur pour aligner les éléments sur la même ligne avec des marges aux extrémités
        html.Div([
            # Intégration de la carte de radars par département
            html.Iframe(srcDoc=open('templates/radars_map_count_by_department.html', 'r').read(), width='47.5%',height='500px'),

            # Intégration de la deuxième carte affichant tout les radars
            html.Iframe(srcDoc=open('templates/all_radars_map.html', 'r').read(), width='47.5%', height='500px'),
        ], style={'display': 'flex', 'justifyContent': 'space-between', 'margin': '20px'}),


        # Ajout de l'histogramme et diagramme date
        html.Div([
            dcc.Graph(
                figure=fig_histogramme,
                style={"width": "46%", "height": "400px", "borderRadius": "15px", "border": "2px solid #ccc",
                       "overflow": "hidden", "marginRight": "20px", "marginLeft": "40px", "marginTop": "40px"}
            ),
            html.Div([
                html.Div([
                    dcc.Graph(
                        figure=fig_diagramme_da,
                        style={"width": "155%", "height": "400px", "borderRadius": "15px", "border": "2px solid #ccc",
                               "overflow": "hidden", "marginRight": "20px", "marginTop": "40px"}
                    ),
                ]),
            ], style={"width": "30%", "display": "flex", "flexDirection": "column"}),
        ], style={"display": "flex", "flexDirection": "row"}),  # Placement en ligne des deux éléments

        # Ajout du diagramme vitesse
        html.Div([
            dcc.Graph(
                figure=fig_diagramme_vi,
                # Mise en place du style ( marge, espace pris)
                style={"width": "60%", "borderRadius": "15px", "border": "2px solid #ccc", "overflow": "hidden",
                       "marginTop": "20px", "marginbottom": "20px"}
            ),
        ], style={"display": "flex", "justifyContent": "center", "flexDirection": "row"}),
    ])

    # Lancement de l'application
    app.run_server(debug=True)
