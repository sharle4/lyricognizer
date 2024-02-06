import re
import unidecode

def preprocess_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        
    # Remove annotations indicating verses and choruses
    text = re.sub(r'\[.*?\]', '', text)

    # Remove punctuation and capital letters
    text = re.sub(r"[^\w\s\']", '', text)
    text = text.replace("'", " ")
    text = text.lower()

    # Delete line breaks
    text = text.replace("\n", " ")
    
    # Delete accents
    text = unidecode.unidecode(text)

    return text

def save_preprocessed_text(preprocessed_text, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(preprocessed_text)

file_path = "texts/lyrics.txt"
output_file = "texts/lyrics_preprocessed.txt"

preprocessed_text = preprocess_text(file_path)
save_preprocessed_text(preprocessed_text, output_file)
print("Texte prétraité enregistré avec succès dans", output_file)