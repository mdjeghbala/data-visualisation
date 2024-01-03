from dash import Dash, dcc, html, Input, Output
from models.diagramme_date_installation import DiagrammeDate
from models.diagramme_vitesse_max import DiagrammeVitesse
from models.histogramme_exces_de_vitesse import Histogramme

if __name__ == '__main__':

    # Initialisation de l'application
    app = Dash(__name__)

    # Création de l'histogramme
    histogramme = Histogramme('assets/data/opendata-vitesse.csv')
    fig_histogramme = histogramme.affiche_histo_exces_de_vitesse()

    # Création des diagrammes
    diagramme_vitesse = DiagrammeVitesse('assets/data/radars.csv')
    fig_diagramme_vi = diagramme_vitesse.affiche_diagramme_vitesse_max()
    diagramme_date = DiagrammeDate('assets/data/radars.csv')
    fig_diagramme_da = diagramme_date.affiche_diagramme_date_install()

    # Liste des options pour la carte
    card_options = [
        {'label': 'Carte par département', 'value': 'department_map'},
        {'label': 'Tous les radars', 'value': 'all_radars_map'}
    ]

    # Mise en place du layout de l'application
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
                                        "font-size": "2em" # Taille du texte augmentée
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
                        "Ce DashBoard vous propose de visualiser l'ensemble des radars dont la France dispose, "
                        "que ce soit en France métropolitaine ou en France d'outre-mers.",
                        html.Br(),
                        "Vous pourrez observer le nombre de radars par département, leur emplacement et quelques "
                        "statistiques assez intéressantes!"
                    ],
                    style={
                        "backgroundColor": "#4B587B",
                        "color": "#ffffff", # Couleur du texte en blanc
                        "borderRadius": "15px",
                        "padding": "10px",
                        "margin": "auto",
                        "marginTop": '20px',
                        "width": "fit-content",
                        "box-shadow": "2px 2px 5px 2px rgba(0, 0, 0, 0.2)",
                        "text-align": "center" # Centrage du texte à l'intérieur du rectangle
                    }
                ),
            ]
        ),

        # Liste déroulante pour choisir la carte
        html.Div([
            dcc.Dropdown(
                id='card-dropdown',
                options=card_options,
                value=card_options[0]['value'],
                style={'width': '50%', 'margin': 'auto'}
            )
        ], style={'textAlign': 'center', 'marginBottom': '20px', 'marginTop': '20px'}),

        # Conteneur pour la carte
        html.Div(id='card-container', style={'marginLeft': '100px', 'marginRight': '100px'}),

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
                style={"width": "60%", "borderRadius": "15px", "border": "2px solid #ccc", "overflow": "hidden",
                       "marginTop": "20px", "marginbottom": "20px"}
            ),
        ], style={"display": "flex", "justifyContent": "center", "flexDirection": "row"}),
    ])

    # Callback pour mettre à jour la carte en fonction de la sélection de l'utilisateur
    @app.callback(
        Output('card-container', 'children'),
        [Input('card-dropdown', 'value')]
    )
    def update_card(selected_card):
        if selected_card == 'department_map':
            return html.Iframe(
                srcDoc=open('templates/radars_map_count_by_department.html', 'r', encoding='utf-8').read(),
                width='100%', height='500px')
        elif selected_card == 'all_radars_map':
            return html.Iframe(srcDoc=open('templates/all_radars_map.html', 'r', encoding='utf-8').read(), width='100%',
                               height='500px')
        else:
            return html.Div('Sélectionnez une carte à afficher.')


    # Lancement de l'application
    app.run_server(debug=True)
