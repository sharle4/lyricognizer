import matplotlib.pyplot as plt
import os

result = []
compressed_res = {}
for artist in result.keys():
    print("Nous étudions les résultas pour ", artist)
    for c_artist in result[artist][0].keys():
        print(result[artist][0][c_artist][0][0]*100, "'%' de chance que ", c_artist, " soit l'auteur de ", artist, " par la méthode zlib, ce qui fait de lui le rang ", result[artist][0][c_artist][1][0])
        print(result[artist][0][c_artist][0][1]*100, "'%' de chance que ", c_artist, " soit l'auteur de ", artist, " par la méthode nzma, ce qui fait de lui le rang ", result[artist][0][c_artist][1][1])
        print(result[artist][0][c_artist][0][2]*100, "'%' de chance que ", c_artist, " soit l'auteur de ", artist, " par la méthode bz2, ce qui fait de lui le rang ", result[artist][0][c_artist][1][2])
        compressed_res[c_artist] = [result[artist][0][c_artist][0][0]*100, result[artist][0][c_artist][0][1]*100, result[artist][0][c_artist][0][2]*100]
    i = 1
    for dico_chanson in result[artist][1:]:
        print('Analyse de la chanson ', i)
        for c_artist in result[artist][i].keys():
            print(result[artist][i][c_artist][0][0]*100, "'%' de chance que ", c_artist, " soit l'auteur de la chanson ", i, " " ,artist, " par la méthode zlib, ce qui fait de lui le rang ", result[artist][i][c_artist][1][0])
            print(result[artist][i][c_artist][0][1]*100, "'%' de chance que ", c_artist, " soit l'auteur de la chanson ", i, " " ,artist, " par la méthode nzma, ce qui fait de lui le rang ", result[artist][i][c_artist][1][1])
            print(result[artist][i][c_artist][0][2]*100, "'%' de chance que ", c_artist, " soit l'auteur de la chanson ", i, " "  ,artist, " par la méthode bz2, ce qui fait de lui le rang ", result[artist][i][c_artist][1][2])
        i+=1

artists = []
for folder in os.listdir("./lyrics"):
    artists.append(folder[2:])
    
# Tri des artistes par ordre alphabétique
artistes_triés = sorted(compressed_res.keys())

# Extraction des pourcentages pour chaque méthode
pourcentages_zlib = [compressed_res[artiste][0] for artiste in artistes_triés]
pourcentages_nzma = [compressed_res[artiste][1] for artiste in artistes_triés]
pourcentages_bz2 = [compressed_res[artiste][2] for artiste in artistes_triés]

# Création du graphe à barres pour la méthode zlib
plt.bar(artistes_triés, pourcentages_zlib, label='zlib')

# Ajout des barres pour les autres méthodes avec un décalage sur l'axe x
x = range(len(artistes_triés))
plt.bar([i + 0.2 for i in x], pourcentages_nzma, width=0.2, label='nzma')
plt.bar([i + 0.4 for i in x], pourcentages_bz2, width=0.2, label='bz2')

# Ajout de légendes et d'étiquettes
plt.xlabel('Artistes')
plt.ylabel('Pourcentage de chance')
plt.title('Pourcentages de chance par méthode et par artiste')
plt.legend()

# Affichage du graphe
plt.xticks(rotation=45, ha='right')  # Rotation des étiquettes des artistes pour éviter le chevauchement
plt.tight_layout()  # Ajustement automatique de la mise en page pour éviter la coupure des étiquettes
plt.show()