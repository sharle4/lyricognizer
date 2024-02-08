import os
import random

# Chemin du dossier contenant les fichiers à renommer
dossier = "./lyrics/nekfeu/raw/"

# Liste des noms de fichiers dans le dossier
noms_fichiers = os.listdir(dossier)

# Mélanger aléatoirement la liste des noms de fichiers
random.shuffle(noms_fichiers)

# Renommer les fichiers dans l'ordre aléatoire
for i, nom_fichier in enumerate(noms_fichiers, start=1):
    chemin_origine = os.path.join(dossier, nom_fichier)
    extension = os.path.splitext(nom_fichier)[1]
    nouveau_nom = f"{i}{extension}"
    chemin_destination = os.path.join(dossier, nouveau_nom)
    os.rename(chemin_origine, chemin_destination)

print("Les fichiers ont été renommés dans un ordre aléatoire.")
