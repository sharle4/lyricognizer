import zlib

def ncd(text1, text2):
    # Concaténer les deux textes
    concatenated_text = text1 + text2
    
    # Calculer la taille de la compression du texte 1
    compressed_text1 = zlib.compress(text1.encode('utf-8'))
    compressed_size1 = len(compressed_text1)
    
    # Calculer la taille de la compression du texte 2
    compressed_text2 = zlib.compress(text2.encode('utf-8'))
    compressed_size2 = len(compressed_text2)
    
    # Calculer la taille de la compression du texte concaténé
    compressed_concatenated_text = zlib.compress(concatenated_text.encode('utf-8'))
    compressed_size_concatenated = len(compressed_concatenated_text)
    
    # Calculer la NCD
    ncd_value = (compressed_size_concatenated - min(compressed_size1, compressed_size2)) / max(compressed_size1, compressed_size2)
    
    return ncd_value


if __name__ == "__main__":
    file_path = "texts/lyrics_preprocessed"
    with open(file_path + ".txt", 'r', encoding='utf-8') as file:
        text1 = file.read()
    with open(file_path + "1.txt", 'r', encoding='utf-8') as file:
        text2 = file.read()
        
    distance = ncd(text1, text2)
    print("Normalized Compression Distance:", distance)
