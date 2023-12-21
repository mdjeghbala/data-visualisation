import plotly_express as px
from histogramme_date_installation import affiche_diagramme_date_install
from histogramme_vitesse_max import affiche_diagramme_vitesse_max
from histogramme_exces_de_vitesse import affiche_histo_exces_de_vitesse
import dash
from dash import dcc
from dash import html

#
# Data

#affiche_diagramme_date_install('radars.csv')
affiche_histo_exces_de_vitesse('opendata-vitesse.csv')
#affiche_diagramme_vitesse_max('radars.csv')
