import os
import random

def renamer(rd:bool, num=False): #
    dossier_principal = "./lyrics/"
    artistes = [dossier for dossier in os.listdir(dossier_principal) if os.path.isdir(os.path.join(dossier_principal, dossier))]

    for artiste in artistes:
        if rd: #random rename
            dossier = f"{dossier_principal}{artiste}/raw"
            noms_fichiers = os.listdir(dossier)
            random.shuffle(noms_fichiers)

            for i, nom_fichier in enumerate(noms_fichiers, start=1):
                chemin_origine =f"{dossier}/{nom_fichier}"
                nouveau_nom = f"_{i}.txt"
                chemin_destination = f"{dossier}/{nouveau_nom}"
                os.rename(chemin_origine, chemin_destination)
            
        else:
            subfolders = ['processed', 'processed_sw', 'processed_lm']
            for subfolder in subfolders:
                subfolder = f"{dossier_principal}{artiste}/{subfolder}"
                if num == False: #reduce 1
                    noms_fichiers = os.listdir(subfolder)

                    indices = [int(filename.split('_')[1].split('.')[0]) for filename in noms_fichiers]
                    indices.sort()
                    for i, index in enumerate(indices, start = 0):
                        ori_path = f"{subfolder}/_{index}.txt"
                        new_name = f"_{i}.txt"
                        tgt_path = f"{subfolder}/{new_name}"
                        os.rename(ori_path, tgt_path)
                else: #fill with 0
                    for fichier in os.listdir(subfolder):
                        nom_fichier, extension = os.path.splitext(fichier)
                        nom_fichier, numero = nom_fichier.split('_')
                        numero = numero.zfill(2)
                        nouveau_nom_fichier = f"{nom_fichier}_{numero}{extension}"
                        ancien_chemin = os.path.join(subfolder, fichier)
                        nouveau_chemin = os.path.join(subfolder, nouveau_nom_fichier)
                        os.rename(ancien_chemin, nouveau_chemin)
renamer(False, True)
                
