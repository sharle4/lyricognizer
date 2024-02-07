import re
import unidecode
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import SnowballStemmer
from nltk.stem import WordNetLemmatizer

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

def preprocess_str(text):
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

    # Tokenisation
    tokens = word_tokenize(text)

    # Supprimer les stopwords
    stop_words = set(stopwords.words('french'))
    filtered_tokens = [word for word in tokens if word not in stop_words]

    # Stemming
    stemmer = SnowballStemmer('french')
    stemmed_tokens = [stemmer.stem(token) for token in filtered_tokens]

    # Lemmatisation
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in stemmed_tokens]

    # Rejoindre les tokens lemmatisés en une seule chaîne de texte
    preprocessed_text = ' '.join(lemmatized_tokens)
    
    return preprocessed_text

if __name__ == "__main__":
    file_path = "texts/lyrics.txt"
    output_file = "texts/lyrics_preprocessed.txt"

    preprocessed_text = preprocess_text(file_path)
    save_preprocessed_text(preprocessed_text, output_file)
    print("Texte prétraité enregistré avec succès dans", output_file)