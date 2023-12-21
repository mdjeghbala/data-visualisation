import pandas as pd
import matplotlib.pyplot as plt

# Fonction permettant d'avoir les exces de vitesse inférieur à 50km
def extraction_exces_vitesse(fichier_csv):
    # on place les données du fichier CSV dans une DataFrame en prenant les 1 000 000 premières années
    data = pd.read_csv(fichier_csv, sep=';', nrows=1000000)

    # On sélectionne seulement les mesures de vitesse qui dépassent les limites du radar
    vitesse_sup_limite = data[data['mesure'] > data['limite']]

    # On calcule le nombre de km en excès et on place ça dans une nouvelle série
    exces_vitesse = vitesse_sup_limite['mesure'] - vitesse_sup_limite['limite']

    # On prend les excès inférieurs ou égals à 50 et on place ça dans une nouvelle série
    exces_vitesse_50 = exces_vitesse[exces_vitesse <= 50]
    return exces_vitesse_50


# Fonction pour mettre les pourcentages
def affichePourcentage(barres, fichier_csv):
    data = pd.read_csv(fichier_csv, sep=';', nrows=1000000)
    exces_vitesse_50 = extraction_exces_vitesse(fichier_csv)

    for barre in barres:
        height = barre.get_height()
        pourcentage = '{:.1f}%'.format(100 * height / len(exces_vitesse_50))         #calcule les pourcentages
        plt.text(barre.get_x() + barre.get_width() / 2., height, pourcentage,        #place les pourcentages au dessus de chaque barre au milieu
                 ha='center', va='bottom')

# Fonction qui affiche l'histogramme sur les excès de vitesse
def affiche_histo_exces_de_vitesse(fichier_csv):
    # on place les données du fichier CSV dans une DataFrame
    data = pd.read_csv(fichier_csv, sep=';', nrows=1000000)
    exces_vitesse_50 = extraction_exces_vitesse(fichier_csv)

    # On segmente les barres par tranche de 5km d'excès
    tranches = range(0, 51, 5)

    # Créer l'histogramme
    plt.figure(figsize=(8, 6))
    plt.hist(exces_vitesse_50, bins=tranches, color='#78B7C5', edgecolor='black', linewidth=1.5)

    # les barres de l'histogramme
    barres = plt.gca().patches

    # Mettre les pourcentages
    affichePourcentage(barres, fichier_csv)

    #On donne un nom à l'histogramme ainsi que les axes
    plt.title('Excès de vitesse par tranche de 5 km/h de 0-50km/h')
    plt.xlabel('Excès de vitesse (km/h)')
    plt.ylabel('Nombre de véhicules')

    plt.xticks(rotation=45)
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.show()



