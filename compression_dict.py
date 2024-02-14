import os
import bz2
import json

def save_dico_txt(dico, filename):
    with open(filename, 'w') as f:
        json.dump(dico, f, indent=4)
            
def dict_creation():
    compression_dict = {}
    for artist in os.listdir("lyrics"):
        compression_dict[artist] = []
        
        for method in range(3):
            compression_dict[artist].append([])
            directory = f"lyrics/{artist}/{method}"

            for text in os.listdir(directory):
                path = f"lyrics/{artist}/{method}/{text}"
                    
                with open(path, 'r', encoding='utf-8') as file:
                    compressed_length = len(bz2.compress(file.read().encode('utf-8')))
                    compression_dict[artist][-1].append(compressed_length)
                    
    return compression_dict

res = dict_creation()
save_dico_txt(res, "compression_dict.txt")