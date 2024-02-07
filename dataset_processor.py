from cleaner import preprocess_text,save_preprocessed_text
import os

songs = os.listdir("./lyrics/bbj/raw")

if __name__ == "__main__":
    for file in songs:
        file_path = "./lyrics/bbj/processed/" + file
        preprocessed_text = preprocess_text(file_path)
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(preprocessed_text)