from ncd import ncd
from sys import Argv
from cleaner import *



if __name__ == "__main__":
    text_to_test = str(input("Quelles sont vos lyrics?"))
    text_to_test = preprocess_str(text_to_test)
    save_preprocessed_text(text_to_test,"texts/lyrics_sample.txt")
    

