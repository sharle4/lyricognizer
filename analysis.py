import matplotlib.pyplot as plt
import os
import json

with open("final_results.txt", 'r', encoding='utf-8') as file:
    result = eval(file.read())

graphe_artiste = "soolking" 
compressed_res = {}
compressed_rank = {}
for artist in result.keys():
    print("Nous étudions les résultas pour ", artist)
    if artist == graphe_artiste:
        for c_artist in result[artist][0].keys():
        #print(result[artist][0][c_artist][0][0]*100, "'%' de chance que ", c_artist, " soit l'auteur de ", artist, " par la méthode zlib, ce qui fait de lui le rang ", result[artist][0][c_artist][1][0])
        #print(result[artist][0][c_artist][0][1]*100, "'%' de chance que ", c_artist, " soit l'auteur de ", artist, " par la méthode nzma, ce qui fait de lui le rang ", result[artist][0][c_artist][1][1])
        #print(result[artist][0][c_artist][0][2]*100, "'%' de chance que ", c_artist, " soit l'auteur de ", artist, " par la méthode bz2, ce qui fait de lui le rang ", result[artist][0][c_artist][1][2])
            compressed_res[c_artist] = [result[artist][0][c_artist][0][0]*100, result[artist][0][c_artist][0][1]*100, result[artist][0][c_artist][0][2]*100]
            compressed_rank[c_artist] = [result[artist][0][c_artist][1][0], result[artist][0][c_artist][1][1], result[artist][0][c_artist][1][2]]
        i = 0
        top1 = [0,0,0]
        #for dico_musique in result[artist][1:]:
        #    for sub_artist in dico_musique:
        #        dico_musique[sub_artist][0].append((dico_musique[sub_artist][0][0]+dico_musique[sub_artist][0][2])/2)
        #    for artiste in dico_musique:
        #            i = 3
        #            scores_i = [dico_musique[artiste][0][i] for artiste in dico_musique]
        #            rang = sorted(scores_i, reverse=True).index(dico_musique[artiste][0][i]) + 1
        #            dico_musique[artiste][1].append(rang)
        for dico_musique in result[artist][1:]: 
            print("Pour la musique ", i, " ", artist, " est top ", dico_musique[artist][1])
            for j in range(3):
                if dico_musique[artist][1][j] == 1:
                    top1[j] += 1
            i+=1
        print(artist, " a fait ces résultats en top 1 ", top1)
    #i = 1
    #for dico_chanson in result[artist][1:]:
    #    print('Analyse de la chanson ', i)
    #    for c_artist in result[artist][i].keys():
    #        print(result[artist][i][c_artist][0][0]*100, "'%' de chance que ", c_artist, " soit l'auteur de la chanson ", i, " " ,artist, " par la méthode zlib, ce qui fait de lui le rang ", result[artist][i][c_artist][1][0])
    #        print(result[artist][i][c_artist][0][1]*100, "'%' de chance que ", c_artist, " soit l'auteur de la chanson ", i, " " ,artist, " par la méthode nzma, ce qui fait de lui le rang ", result[artist][i][c_artist][1][1])
    #        print(result[artist][i][c_artist][0][2]*100, "'%' de chance que ", c_artist, " soit l'auteur de la chanson ", i, " "  ,artist, " par la méthode bz2, ce qui fait de lui le rang ", result[artist][i][c_artist][1][2])
    #    i+=1

artists = []
for folder in os.listdir("./lyrics"):
    artists.append(folder)
    
# Tri des artistes par ordre alphabétique
artistes_triés = sorted(compressed_res.keys())

# Extraction des pourcentages pour chaque méthode
pourcentages_zlib = [compressed_res[artiste][0] for artiste in artistes_triés]
pourcentages_nzma = [compressed_res[artiste][1] for artiste in artistes_triés]
pourcentages_bz2 = [compressed_res[artiste][2] for artiste in artistes_triés]
ranks_zlib = [compressed_rank[artiste][0] for artiste in artistes_triés]
ranks_nzma = [compressed_rank[artiste][1] for artiste in artistes_triés]
ranks_bz2 = [compressed_rank[artiste][2] for artiste in artistes_triés]
# Création du graphe à barres pour la méthode zlib
plt.bar(artistes_triés, pourcentages_zlib, label='distance processed', width=0.2)

# Ajout des barres pour les autres méthodes avec un décalage sur l'axe x
x = range(len(artistes_triés))
plt.bar([i + 0.2 for i in x], pourcentages_nzma, width=0.2, label='distance sw')
plt.bar([i + 0.4 for i in x], pourcentages_bz2, width=0.2, label='distance lm')

# Ajout de légendes et d'étiquettes
plt.xlabel('Artistes')
plt.ylabel(f"Distance avec les musiques de {graphe_artiste}")
plt.title(f"Distance par méthode et par artiste avec les musiques de {graphe_artiste}")
plt.legend()

# Affichage du graphe
plt.xticks(rotation=45, ha='right')  # Rotation des étiquettes des artistes pour éviter le chevauchement
plt.tight_layout()  # Ajustement automatique de la mise en page pour éviter la coupure des étiquettes
plt.show()

# Création du graphe à barres pour la méthode zlib
plt.bar(artistes_triés, ranks_zlib, label='rank processed', width=0.2)

# Ajout des barres pour les autres méthodes avec un décalage sur l'axe x
x = range(len(artistes_triés))
plt.bar([i + 0.2 for i in x], ranks_nzma, width=0.2, label='rank sw')
plt.bar([i + 0.4 for i in x], ranks_bz2, width=0.2, label='rank lm')

# Ajout de légendes et d'étiquettes
plt.xlabel('Artistes')
plt.ylabel(f"Rang de similarité lyricale avec {graphe_artiste}")
plt.title(f"Rang de similirité lyricale avec {graphe_artiste} par méthode et par artiste")
plt.legend()

# Affichage du graphe
plt.xticks(rotation=45, ha='right')  # Rotation des étiquettes des artistes pour éviter le chevauchement
plt.tight_layout()  # Ajustement automatique de la mise en page pour éviter la coupure des étiquettes
plt.show()