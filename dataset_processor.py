from cleaner import preprocess
import os

for artiste in os.listdir("./lyrics"):
    artist_folder = os.path.join("./lyrics", artiste)
    print(f"Processing artist: {artiste}")
    
    if artiste in ["bbj", "damso", "freeze", "gazo", "lomepal", "soolking", "nekfeu"]:
        lang = "french"
    elif artiste == 'drake':
        lang = "english"
    else:
        lang = None
        
    for file in os.listdir(os.path.join(artist_folder, "raw")):
        path_in = os.path.join(artist_folder, "raw", file)
        path_out = os.path.join(artist_folder, "processed", file)
        path_out_sw = os.path.join(artist_folder, "processed_sw", file)
        path_out_lm = os.path.join(artist_folder, "processed_lm", file)
        
        with open(path_in, 'r', encoding='utf-8') as f:
            text = f.read()
        
        preprocessed_text = preprocess(text, lang)
        preprocessed_text_sw = preprocess(text, lang, True)
        preprocessed_text_lm = preprocess(text, lang, True, True)
        
        with open(path_out, 'w', encoding='utf-8') as f:
            f.write(preprocessed_text)
        with open(path_out_sw, 'w', encoding='utf-8') as f:
            f.write(preprocessed_text_sw)
        with open(path_out_lm, 'w', encoding='utf-8') as f:
            f.write(preprocessed_text_lm)
                
    print(f"Finished processing artist: {artiste}")