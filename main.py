import os
from cleaner import *
from frequency import get_frequency
from ncd import *
from ngd import *
from plotter import bar_chart

def mean(L):
    """donne la moyenne d'une liste d'entiers""" 
    if L ==[]:
        return 0
    else:
        return(sum(L)/len(L))
    
def save_dico_txt(dico, filename):
    with open(filename, 'w') as f:
        for cle, valeur in dico.items():
            f.write(f"{cle}: {valeur}\n")
            
def get_ngd(text,artist):
    """donne la moyenne des ngd entre les mots les plus fréquents du texte et le nom de l'artiste """
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
    results = {}
    for text_format in ["processed_sw"]:
        for test_artist in artists:
            res_test_artist = [{artist[2:]: [[], []] for artist in artists}]
            
            for test_song in os.listdir(f"./lyrics/{test_artist}/{text_format}")[:20]:
                res_test_song = {artist[2:]: [[], []] for artist in artists}
                with open(f"./lyrics/{test_artist}/{text_format}/{test_song}", 'r', encoding='utf-8') as file:
                    text_test_song = file.read()
                print(f"Méthode de formattage : {text_format} - Analyse des paroles de la chanson {test_song} de {test_artist}")
                
                for base_artist in artists:
                    invdist = [0,0,0]
                    songs_count = 0
                    
                    for base_song in os.listdir(f"./lyrics/{base_artist}/{text_format}")[20:]:
                        with open(f"./lyrics/{base_artist}/{text_format}/{base_song}", 'r', encoding='utf-8') as file:
                            text_base_song = file.read()
                        invdist[0] += 1-ncd(text_test_song, text_base_song, 'zlib')
                        invdist[1] += 1-ncd(text_test_song, text_base_song, 'lzma')
                        invdist[2] += 1-ncd(text_test_song, text_base_song, 'bz2')
                        songs_count += 1

                    invdist = [id/songs_count for id in invdist]
                    res_test_song[base_artist[2:]][0] = invdist.copy()
                for artiste in res_test_song:
                    for i in range(3):
                        scores_i = [res_test_song[artiste][0][i] for artiste in res_test_song]
                        rang = sorted(scores_i, reverse=True).index(res_test_song[artiste][0][i]) + 1
                        res_test_song[artiste][1].append(rang)
            
                res_test_artist.append(res_test_song)
                
            for artist in artists:
                dist, rank = [0,0,0], [0,0,0]
                for dico_res_musique in res_test_artist[1:]:
                    for i in range(3):
                        dist[i] += dico_res_musique[artist[2:]][0][i]/20
                        rank[i] += dico_res_musique[artist[2:]][1][i]/20
                res_test_artist[0][artist[2:]][0] = dist.copy()
                res_test_artist[0][artist[2:]][1] = rank.copy()

                
        results[test_artist[2:]] = res_test_artist
            
    save_dico_txt(results, "final_results_sw.txt")
    print("enfin fini")
