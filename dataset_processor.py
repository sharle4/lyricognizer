from cleaner import preprocess_text,save_preprocessed_text
import os

songs = os.listdir("./genius-lyrics-api-master/lib/dataset/freeze_corleone")

if __name__ == "__main__":
    for file in songs:
        file_path = "./genius-lyrics-api-master/lib/dataset/freeze_corleone/" + file
        save_preprocessed_text(preprocess_text(file_path),file_path)

