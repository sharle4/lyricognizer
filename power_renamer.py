import os
import random

def renamer(rd:bool, num=False):
    # Chemin du dossier principal contenant les dossiers d'artistes
    dossier_principal = "./lyrics/"

    # Liste des noms d'artistes basée sur les noms de dossiers
    artistes = [dossier for dossier in os.listdir(dossier_principal) if os.path.isdir(os.path.join(dossier_principal, dossier))]

    # Parcours des dossiers pour chaque artiste
    for artiste in artistes:
        if rd: 
            dossier = f"{dossier_principal}{artiste}/raw"
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
        else:
            subfolders = ['processed', 'processed_sw', 'processed_lm']
            for subfolder in subfolders:
                subfolder = f"{dossier_principal}{artiste}/{subfolder}"
                if num == False:
                    noms_fichiers = os.listdir(subfolder)

                    indices = [int(filename.split('_')[1].split('.')[0]) for filename in noms_fichiers]
                    indices.sort()
                    for i, index in enumerate(indices, start = 0):
                        ori_path = f"{subfolder}/_{index}.txt"
                        new_name = f"_{i}.txt"
                        tgt_path = f"{subfolder}/{new_name}"
                        os.rename(ori_path, tgt_path)
                else:
                    for fichier in os.listdir(subfolder):
                        nom_fichier, extension = os.path.splitext(fichier)
                        nom_fichier, numero = nom_fichier.split('_')
                        numero = numero.zfill(2)
                        nouveau_nom_fichier = f"{nom_fichier}_{numero}{extension}"
                        ancien_chemin = os.path.join(subfolder, fichier)
                        nouveau_chemin = os.path.join(subfolder, nouveau_nom_fichier)
                        os.rename(ancien_chemin, nouveau_chemin)
renamer(False, True)
                
