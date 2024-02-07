import re
import unidecode
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import SnowballStemmer
from nltk.stem import WordNetLemmatizer

def preprocess_str(text, _stopwords=False, _stemming=False, _lemmatization=False):
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
    
    if _stopwords == True:
        stop_words = set(stopwords.words('french'))
        filtered_tokens = [word for word in tokens if word not in stop_words]
        tokens = filtered_tokens

    if _stemming == True:
        stemmer = SnowballStemmer('french')
        stemmed_tokens = [stemmer.stem(token) for token in tokens]
        tokens = stemmed_tokens

    if _lemmatization == True:
        lemmatizer = WordNetLemmatizer()
        lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]
        tokens = lemmatized_tokens

    # Rejoindre les tokens lemmatisés en une seule chaîne de texte
    preprocessed_text = ' '.join(tokens)
    
    return preprocessed_text