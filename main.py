from dash import Dash, dcc, html

import plotly_express as px
from models.diagramme_date_installation import affiche_diagramme_date_install
from models.diagramme_vitesse_max import affiche_diagramme_vitesse_max
from models.histogramme_exces_de_vitesse import affiche_histo_exces_de_vitesse

if __name__ == '__main__':
    # Création de l'application du dashboard
    app = Dash(__name__)

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
                html.Div([
                    html.H1(
                        "Dashboard",
                        style={"font-size": "2em", "margin-right": "10px"}
                    ),
                    html.Img(
                        src="assets/dashboard.png",
                        width="40px",
                        height="40px",
                    ),
                ], style={"display": "flex", "alignItems": "center"}),

                html.Img(
                    src="assets/radar.png",
                    width="90px",
                    height="115px",
                ),
            ],
        ),

        html.Div([
            html.Div("Le nombre de radars par département", style={'color': 'white', 'font-size': '30px', 'margin': 'auto'}),
            html.Div("Position de tous les radars", style={'color': 'white', 'font-size': '30px', 'margin': 'auto'}),
        ], style={'display': 'flex', 'justifyContent': 'space-between', 'margin': '20px'}),

        # Conteneur pour aligner les éléments sur la même ligne avec des marges aux extrémités
        html.Div([
            # Intégration de la carte de radars par département
            html.Iframe(srcDoc=open('templates/radars_map_count_by_department.html', 'r').read(), width='47.5%',
                        height='500px'),

            # Intégration de la deuxième carte affichant tout les radars
            html.Iframe(srcDoc=open('templates/all_radars_map.html', 'r').read(), width='47.5%',height='500px'),
        ], style={'display': 'flex', 'justifyContent': 'space-between', 'margin': '20px'})
    ])

    # Lancement de l'application
    app.run_server(debug=True)
