import os
from cleaner import *
from frequency import get_frequency
from ncd import *
from ngd import *
from plotter import bar_chart

def mean(L):
    #return sum(L)/len(L)
    if L ==[]:
        return 0
    else:
        sum = 0
        for val in L:
            sum+=val
        return sum/len(L)

def get_ngd(text,artist):
    tmp = get_frequency(text)
    words = []
    google_distances = []
    for k in range(len(tmp)):
        words.append(str(tmp[k][0])) 
    print(words)
    for word in words:
        ngd = calculate_NGD(str(word),str(artist))
        print(ngd,word,artist)
        google_distances.append(ngd) 
    print(mean(google_distances))
    return mean(google_distances)

if __name__ == "__main__":
    artists = []
    for folder in os.listdir("./lyrics"):
        artists.append(folder)
        
    dico, dico_zlib, dico_lzma, dico_bz2, dico_ngd = {}, {}, {}, {}, {}
    text_to_test = str(input("Quelles sont vos paroles?"))

    for artist in artists:
        #dico_ngd[artist] = 1-get_ngd(text_to_test,artist)
        
        distances_zlib = []
        distances_lzma = []
        distances_bz2 = []
        path = f"./lyrics/{artist}/processed"
        songs = os.listdir(path)
        
        for song in songs:
            with open(f"{path}/{song}", 'r', encoding='utf-8') as file:
                referring_text = file.read()
            distance_zlib = ncd(text_to_test, referring_text, 'zlib')
            distance_lzma = ncd(text_to_test, referring_text, 'lzma')
            distance_bz2 = ncd(text_to_test, referring_text, 'bz2')
            distances_zlib.append(1-distance_zlib)
            distances_lzma.append(1-distance_lzma)
        dico_lzma[artist] = mean(distances_lzma)
        dico_zlib[artist] = mean(distances_zlib)
        dico[artist] = ((dico_lzma[artist]+dico_zlib[artist])*2+dico_ngd[artist])/3
    print(f"Dico_zlib: {dico_zlib}")
    print(f"dico_lzma: {dico_lzma}")
    print(f"dico: {dico}")
    print(f"dico_ngd: {dico_ngd}")
    bar_chart(dico_bz2,dico_lzma,dico_zlib,dico_ngd,dico)
        




