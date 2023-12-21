from dash import Dash, dcc, html

import plotly_express as px
from histogramme_date_installation import affiche_diagramme_date_install
from histogramme_vitesse_max import affiche_diagramme_vitesse_max
from histogramme_exces_de_vitesse import affiche_histo_exces_de_vitesse

if __name__ == '__main__':
    # Création de l'application du dashboard
    app = Dash(__name__)

    app.layout = html.Div([
        html.Div(
            style={
                "backgroundColor": "#b3dacb",
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
        dcc.Markdown("# Le nombre de radars par département"),

        # Intégration de la carte
        html.Iframe(srcDoc=open('templates/radars_map_count_by_department.html', 'r').read(), width='40%',
                    height='475'),
    ])

    # Lancement de l'application
    app.run_server(debug=True)
