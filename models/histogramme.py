import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# On place les données du fichier CSV dans une DataFrame
radars = pd.read_csv('../radars.csv', sep=';')

# On renomme la colonne pour une appelation plus courte et explicite
radars = radars.rename(columns={'vitesse_vehicule_legers_kmh': 'vitesse_max'})

# On supprime les lignes où la vitesse n'est pas renseignée (NaN)
radars = radars.dropna(subset=['vitesse_max'])

# On définie les emplacements des barres pour chaque dizaine
bins = np.arange(0, radars['vitesse_max'].max() + 10, 10)

# Création de l'histogramme
plt.figure(figsize=(8, 6))
plt.hist(radars['vitesse_max'], bins=10, color='#78B7C5', edgecolor='black', width=5, linewidth=1.5)

plt.title('Analyse des vitesses maximales des radars routiers en France')
plt.xlabel('Vitesse maximale (km/h)')
plt.ylabel('Nombre de radars')


plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.xticks(bins, rotation=45)
plt.show()

