import plotly_express as px
from histogramme_date_installation import affiche_diagramme_date_install
from histogramme_vitesse_max import affiche_diagramme_vitesse_max
from histogramme_exces_de_vitesse import affiche_histo_exces_de_vitesse

import dash
from dash import dcc
from dash import html




if __name__ == '__main__':

    # Création de l'application du dashboard
    app = Dash(__name__)

    # Creation de la carte radar folium
    card = create_radars_numbers_map('radars.csv')
    app.layout = html.Div([
        dcc.Markdown("# Le nombre de radars par département"),
        # Intégration de la carte
        html.Iframe(srcDoc=open('templates/radar_map_count_by_department.html', 'r').read(), width='100%', height='600'),
    ])

    # Lancement de l'application
    app.run_server(debug=True)
