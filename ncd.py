import bz2
import json

with open("compression_dict.txt", 'r', encoding='utf-8') as file:
    compression_dict = json.load(file)

def ncd(text1, test_artist, test_song, base_artist, base_song, text_format):
    path = f"./lyrics/{base_artist}/{text_format}/{base_song}"
    with open(path, 'r', encoding='utf-8') as file:
        text2 = file.read()
        
    t1_2 = text1 + ' ' + text2
    l1 = compression_dict[test_artist][int(text_format)][int(test_song[1:-4])]
    l2 = compression_dict[base_artist][int(text_format)][int(base_song[1:-4])]
    l1_2 = len(bz2.compress(t1_2.encode('utf-8')))

    return (l1_2 - min(l1, l2)) / max(l1, l2)