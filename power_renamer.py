import os
import random

import os

# Chemin du dossier principal contenant les dossiers d'artistes
dossier_principal = "./lyrics/"

# Liste des noms d'artistes basée sur les noms de dossiers
artistes = [dossier for dossier in os.listdir(dossier_principal) if os.path.isdir(os.path.join(dossier_principal, dossier))]

# Parcours des dossiers pour chaque artiste
for artiste in artistes:
    dossier = f"{dossier_principal}{artiste}/raw"
    print(dossier)
    # Liste des noms de fichiers dans le dossier
    noms_fichiers = os.listdir(dossier)

    # Mélanger aléatoirement la liste des noms de fichiers
    random.shuffle(noms_fichiers)

    # Renommer les fichiers dans l'ordre aléatoire
    for i, nom_fichier in enumerate(noms_fichiers, start=1):
        chemin_origine =f"{dossier}/{nom_fichier}"
        nouveau_nom = f"_{i}.txt"
        chemin_destination = f"{dossier}/{nouveau_nom}"
        os.rename(chemin_origine, chemin_destination)

    print("Les fichiers ont été renommés dans un ordre aléatoire.")
