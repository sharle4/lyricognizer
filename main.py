from ncd_zlib import ncd as ncd_zlib
from ncd_lzma import ncd as ncd_lzma
from cleaner import *
import os
from frequency import get_frequency
from ngd import *

def mean(L):
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
    Dico_ngd = {}
    for folder in os.listdir("./lyrics"):
        artists.append(folder)
    text_to_test = str(input("Quelles sont vos paroles?"))
    #text_to_test = preprocess(text_to_test)
    print(text_to_test)

    Dico_zlib = {}
    Dico_lzma={}
    Dico = {}

    for artist in artists:
        Dico_ngd[artist] = 1-get_ngd(text_to_test,artist)
        distances_zlib = []
        distances_lzma = []
        path = f"./lyrics/{artist}/processed"
        songs = os.listdir(path)
        for song in songs:
            with open(f"{path}/{song}", 'r', encoding='utf-8') as file:
                referring_text = file.read()
            distance_zlib = ncd_zlib(text_to_test, referring_text)
            distance_lzma = ncd_lzma(text_to_test, referring_text)
            distances_zlib.append(1-distance_zlib)
            distances_lzma.append(1-distance_lzma)
        Dico_lzma[artist] = mean(distances_lzma)
        Dico_zlib[artist] = mean(distances_zlib)
        Dico[artist] = ((Dico_lzma[artist]+Dico_zlib[artist])*2+Dico_ngd[artist])/3
    print(f"Dico_zlib: {Dico_zlib}")
    print(f"Dico_lzma: {Dico_lzma}")
    print(f"Dico: {Dico}")
    print(f"Dico_ngd: {Dico_ngd}")
        




