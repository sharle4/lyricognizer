import os
import json
from ncd import ncd

def mean(L):
    """donne la moyenne d'une liste d'entiers""" 
    if L ==[]:
        return 0
    else:
        return(sum(L)/len(L))
    
def save_dico_txt(dico, filename):
    with open(filename, 'w') as f:
        json.dump(dico, f, indent=4)
            
if __name__ == "__main__":
    artists = []
    for folder in os.listdir("./lyrics"):
        artists.append(folder)
    results = {}
    for test_artist in artists:
        res_test_artist = [{artist: [[], []] for artist in artists}]
        
        for test_song_num in range(20):
            res_test_song = {artist: [[], []] for artist in artists}
            test_song = f"_{str(test_song_num).zfill(2)}.txt"
            text_test_song = []
            for i in range(3):
                with open(f"./lyrics/{test_artist}/{i}/{test_song}", 'r', encoding='utf-8') as file:
                    text_test_song.append(file.read())

            print(f"Analyse des paroles de la chanson {test_song} de {test_artist}")
            
            for base_artist in artists:
                dist = [0,0,0]                    
                for base_song_num in range(20,100):
                    base_song = f"_{str(base_song_num).zfill(2)}.txt"
                    for i in range(3):
                        dist[i] += ncd(text_test_song[i], test_artist, test_song, base_artist, base_song, i)
                    
                dist = [id/80 for id in dist]
                res_test_song[base_artist][0] = dist.copy()
                
            for artiste in res_test_song:
                for i in range(3):
                    scores_i = [res_test_song[artiste][0][i] for artiste in res_test_song]
                    rang = sorted(scores_i).index(res_test_song[artiste][0][i]) + 1
                    res_test_song[artiste][1].append(rang)
        
            res_test_artist.append(res_test_song)
            
            if test_artist == "aznavour" and test_song == '_00.txt': #debug
                save_dico_txt(res_test_song, "1.txt")
                
        for artist in artists:
            dist, rank = [0,0,0], [0,0,0]
            for dico_res_musique in res_test_artist[1:]:
                for i in range(3):
                    dist[i] += dico_res_musique[artist][0][i]/20
                    rank[i] += dico_res_musique[artist][1][i]/20
            res_test_artist[0][artist][0] = dist.copy()
            res_test_artist[0][artist][1] = rank.copy()
            
        if test_artist == "aznavour": #debug
                save_dico_txt(res_test_artist[0], "2.txt") 
                
        results[test_artist] = res_test_artist
            
    save_dico_txt(results, "final_results.txt")
    print("Processed finished")
