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
    results = []
    for text_format in ["processed", "processed_sw", "processed_lm"]:
        for test_artist in artists:
            res_test_artist = []
            rank = [0, 0, 0]
            count_base_music = 0
            for test_song in os.listdir(f"./lyrics/{test_artist}/{text_format}")[:20]:
                res_test_song = {"zlib" : [{}], "lzma" : [{}], "bz2" : [{}]}
                with open(f"./lyrics/{test_artist}/{text_format}/{test_song}", 'r', encoding='utf-8') as file:
                    text_test_song = file.read()
                print(f"Méthode de formattage : {text_format} - Analyse des paroles de la chanson {test_song} de {test_artist}")
                
                for base_artist in artists:
                    distances_zlib = []
                    distances_lzma = []
                    distances_bz2 = []
                    for base_song in os.listdir(f"./lyrics/{base_artist}/{text_format}")[20:]:
                        with open(f"./lyrics/{base_artist}/{text_format}/{base_song}", 'r', encoding='utf-8') as file:
                            text_base_song = file.read()
                        distances_zlib.append(1-ncd(text_test_song, text_base_song, 'zlib'))
                        distances_lzma.append(1-ncd(text_test_song, text_base_song, 'lzma'))
                        distances_bz2.append(1-ncd(text_test_song, text_base_song, 'bz2'))
                        count_base_music += 1
                    res_test_song["zlib"][0][f"{base_artist}"[2:]] = mean(distances_zlib)
                    res_test_song["lzma"][0][f"{base_artist}"[2:]] = mean(distances_lzma)
                    res_test_song["bz2"][0][f"{base_artist}"[2:]] = mean(distances_bz2)
                    rank_artist_zlib = sorted(res_test_song["zlib"][0].values(), reverse=True).index(res_test_song["zlib"][0][f"{base_artist}"[2:]]) + 1
                    rank_artist_lzma = sorted(res_test_song["lzma"][0].values(), reverse=True).index(res_test_song["lzma"][0][f"{base_artist}"[2:]]) + 1
                    rank_artist_bz2 = sorted(res_test_song["bz2"][0].values(), reverse=True).index(res_test_song["bz2"][0][f"{base_artist}"[2:]]) + 1
                    res_test_song["zlib"].append(rank_artist_zlib)
                    res_test_song["lzma"].append(rank_artist_lzma)
                    res_test_song["bz2"].append(rank_artist_bz2)
                    rank[0] += rank_artist_zlib
                    rank[1] += rank_artist_lzma
                    rank[2] += rank_artist_bz2
                res_test_artist.append(res_test_song)
            rank = rank/count_base_music
            res_test_artist.append({"zlib" : rank[0], "lzma" : rank[0], "bz2" : rank[0]})
    
    final_results = {artists[i][2:]: results[i] for i in range(len(artists))}
    print(final_results)