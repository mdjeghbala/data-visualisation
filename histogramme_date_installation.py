import matplotlib.pyplot as plt
import pandas as pd

# Fonction pour mettre les pourcentages
def affichePourcentage(barres):
    for barre in barres:
        height = barre.get_height()
        percentage = '{:.1f}%'.format(100 * height / len(data['annee']))        #calcule le pourcentage
        plt.text(barre.get_x() + barre.get_width() / 2, height, percentage,     #place le texte au dessus de chaque barre au milieu
                 ha='center', va='bottom')

# On place les données du fichier CSV dans une DataFrame
data = pd.read_csv('radars.csv', sep=';')

# On crée une Série qui est basée sur une colonne de la DataFrame
date = data['date_installation']

# On convertit la colonne représentant la date d'installation dans un format de date/heure facilitant l'analyse des données
date = pd.to_datetime(date, format='%Y-%m-%dT%H:%M:%SZ')

# Crée une nouvelle colonne "annee" qui extrait les années de "date"
data['annee'] = date.dt.year

# Calcul des positions des barres pour chaque année
bar_positions = data['annee'].value_counts().sort_index().index

# Création de l'histogramme
plt.figure(figsize=(8, 6))
plt.hist(data['annee'], bins=bar_positions, color='#78B7C5', edgecolor='black', linewidth=1.5)

# rectangles de l'histogramme
barres = plt.gca().patches

# Ajout des pourcentages
affichePourcentage(barres)

# On donne un nom à l'histogramme ainsi que les axes
plt.title('Nombre de radars installé par année')
plt.xlabel('Année de création')
plt.ylabel('Nombre de radars')

# Affichage d'une année sur deux sur l'axe x
plt.xticks(bar_positions[::2], rotation=45)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.show()
