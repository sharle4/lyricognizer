from cleaner import preprocess
import os

songs = os.listdir("./lyrics/freeze/raw")

if __name__ == "__main__":
    for file in songs:
        path_in = "./lyrics/freeze/raw/" + file
        path_out= "./lyrics/freeze/processed_sw/" + file
        with open(path_in, 'r', encoding='utf-8') as file:
            text = file.read()
        preprocessed_text = preprocess(text, True)
        with open(path_out, 'w', encoding='utf-8') as file:
            file.write(preprocessed_text)