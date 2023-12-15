from dash import Dash, dcc, html
from map import create_radars_numbers_map


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
