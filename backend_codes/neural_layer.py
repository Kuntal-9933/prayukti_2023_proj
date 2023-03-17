import numpy as np
import nltk
from nltk.stem.porter import PorterStemmer

stemmer=PorterStemmer()

def tokenize(sentence):
    return nltk.word_tokenize(sentence)

def word_stem(word):
    return stemmer.stem(word.lower())

def bag_of_words(token_sent,words):
    sent_word=[word_stem(i) for i in token_sent]
    bag=np.zeros(len(words),dtype=np.float32)
    for indx , w in enumerate(words):
        if w in sent_word:
            bag[indx]=1
        return bag
