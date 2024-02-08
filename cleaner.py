import re
import unidecode
import spacy
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from langdetect import detect

def convert_lang_code(lang_code):
    lang_mapping = {
        'af': 'afrikaans', 'ar': 'arabic', 'bg': 'bulgarian', 'bn': 'bengali',
        'ca': 'catalan', 'cs': 'czech', 'cy': 'welsh', 'da': 'danish', 'de': 'german',
        'el': 'greek', 'en': 'english', 'es': 'spanish', 'et': 'estonian', 'fa': 'persian',
        'fi': 'finnish', 'fr': 'french', 'gu': 'gujarati', 'he': 'hebrew', 'hi': 'hindi',
        'hr': 'croatian', 'hu': 'hungarian', 'id': 'indonesian', 'it': 'italian', 'ja': 'japanese',
        'kn': 'kannada', 'ko': 'korean', 'lt': 'lithuanian', 'lv': 'latvian', 'mk': 'macedonian',
        'ml': 'malayalam', 'mr': 'marathi', 'ne': 'nepali', 'nl': 'dutch', 'no': 'norwegian',
        'pa': 'punjabi', 'pl': 'polish', 'pt': 'portuguese', 'ro': 'romanian', 'ru': 'russian',
        'sk': 'slovak', 'sl': 'slovenian', 'so': 'somali', 'sq': 'albanian', 'sv': 'swedish',
        'sw': 'swahili', 'ta': 'tamil', 'te': 'telugu', 'th': 'thai', 'tl': 'tagalog', 'tr': 'turkish',
        'uk': 'ukrainian', 'ur': 'urdu', 'vi': 'vietnamese', 'zh-cn': 'chinese', 'zh-tw': 'chinese',
    }
    return lang_mapping.get(lang_code.lower(), None)


def preprocess(text, lang, _stopwords=False, _lemmatization=False):
    text = text.replace("-", " ")
    text = text.replace("'", " ")
    text = re.sub(r'\[.*?\]', '', text)
    text = re.sub(r"[^\w\s\']", '', text)
    text = text.lower()
    text = text.replace("\n", " ")
    text = unidecode.unidecode(text)

    tokens = word_tokenize(text)

    if _stopwords == True:
        if lang == None:
            try:
                lang = detect(text)
            except:
                print('lang')
                return text
            lang = convert_lang_code(lang)
        stop_words = set(stopwords.words(lang))
        filtered_tokens = [word for word in tokens if word not in stop_words]
        tokens = filtered_tokens

    if _lemmatization == True:
        if lang == 'french':
            nlp = spacy.load("fr_core_news_sm")
        elif lang == 'english':
            nlp = spacy.load("en_core_web_sm")
        else:
            return(''.join(tokens))
        doc = nlp(' '.join(tokens))
        tokens = [token.lemma_ for token in doc]

    preprocessed_text = ' '.join(tokens)
    
    return preprocessed_text