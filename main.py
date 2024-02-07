from ncd_zlib import ncd
from cleaner import *
import os

def mean(L):
    sum = 0
    for val in L:
        sum+=val
    return sum/len(L)


if __name__ == "__main__":
    text_to_test = str(input("Quelles sont vos lyrics?"))
    #text_to_test = preprocess_str(text_to_test)
    #save_preprocessed_text(text_to_test,"texts/lyrics_sample.txt")
    artists = []
    Dico = {}
    for file in os.listdir("./genius-lyrics-api-master/lib/dataset"):
        if file == "utils":
            continue
        elif os.path.isfile(file):
            continue    
        else:
            artists.append(file)
    for artist in artists:
        distances = []
        path = "./genius-lyrics-api-master/lib/dataset/"+artist
        songs = os.listdir(path)
        for song in songs:
            with open(path+"/"+song,'r',encoding='utf-8') as file:
                referring_text = file.read()
            distance = ncd(text_to_test, referring_text)
            distances.append(distance)
        Dico[artist] = mean(distances)
    print(Dico)
        




