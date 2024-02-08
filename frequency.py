import nltk
nltk.download('punkt')
nltk.download('wordnet')
from nltk.corpus import stopwords
from collections import Counter
import re

def get_frequency(text, lang='french'):
    # Tokenize the text into words
    words = nltk.word_tokenize(text.lower())
    
    # Remove non-alphabetic characters and single characters
    words = [word for word in words if word.isalpha() and len(word) > 1]
    
    # Get French stopwords
    french_stopwords = set(stopwords.words(lang))
    
    # Filter out French stopwords
    filtered_words = [str(word) for word in words if word not in french_stopwords]
    
    # Count the frequency of each word
    word_freq = Counter(filtered_words)
    
    # Sort the words by frequency
    sorted_word_freq = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
    
    return sorted_word_freq[:5]


if __name__ == "__main__":
    # Example usage
    text = """
    ceci est un test tout comme la viande et comme le chocolat ainsi 
    que comme les pommes et comme le poisson
    """

    # Set the language to French
    nltk.download('stopwords')
    french_stopwords = set(stopwords.words('french'))

    # Filter out French stopwords
    non_french_frequent_words = [(word, freq) for word, freq in get_non_french_frequent_words(text) if word not in french_stopwords]

    print("Most frequent non-French words:")
    for word, freq in non_french_frequent_words:
        print(f"{word}: {freq}")
