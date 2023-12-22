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

    #Création des diagrammes
    diagramme_vitesse = DiagrammeVitesse('assets/data/radars.csv')
    fig_diagramme_vi = diagramme_vitesse.affiche_diagramme_vitesse_max()
    diagramme_date = DiagrammeDate('assets/data/radars.csv')
    fig_diagramme_da = diagramme_date.affiche_diagramme_date_install()


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

        html.Div([
            dcc.Markdown("# Le nombre de radars par département"),
            html.Iframe(srcDoc=open('templates/radars_map_count_by_department.html', 'r').read(),
                        width='100%', height='400px'),
        ]),

        # Ajout de l'histogramme et diagramme date
        html.Div([
            dcc.Graph(
                figure=fig_histogramme,
                # Mise en place du style ( marge, espace pris)
                style={"width": "46%", "height": "400px", "borderRadius": "15px", "border": "2px solid #ccc", "overflow": "hidden", "marginRight": "20px", "marginLeft": "40px", "marginTop": "40px"}
            ),
            html.Div([
                html.Div([
                    dcc.Graph(
                        figure=fig_diagramme_da,
                        # Mise en place du style ( marge, espace pris)
                        style={"width": "155%", "height": "400px", "borderRadius": "15px", "border": "2px solid #ccc", "overflow": "hidden", "marginRight": "20px", "marginTop": "40px"}
                    ),
                ]),
            ], style={"width": "30%", "display": "flex", "flexDirection": "column"}),
        ], style={"display": "flex",  "flexDirection": "row"}),  # Placement en ligne des deux éléments

        # Ajout du diagramme vitesse
        html.Div([
            dcc.Graph(
                figure=fig_diagramme_vi,
                # Mise en place du style ( marge, espace pris)
                style={"width": "60%", "borderRadius": "15px", "border": "2px solid #ccc", "overflow": "hidden", "marginTop": "20px"}
            ),
        ], style={"display": "flex", "justifyContent": "center", "flexDirection": "row"}),
    ])

    app.run_server(debug=True)