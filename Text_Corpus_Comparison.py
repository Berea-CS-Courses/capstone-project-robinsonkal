import nltk
from nltk.corpus import webtext
from nltk.corpus import twitter_samples
from nltk.tag import pos_tag
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk import FreqDist
from nltk.tokenize import word_tokenize
import random
import re, string
from nltk import classify
from nltk import NaiveBayesClassifier






custom_tweet = "shut the fuck up you skittle you're just spamming meaning replies so the thread hits the bump limit faster."

#custom_tokens = remove_noise(word_tokenize(custom_tweet))

#print(classifier.classify(dict([token, True] for token in custom_tokens)))



def rare_words(corp_type):

    j=0
    for i in split_message:
        #print(j)
    #    print(wordsss[j])
        if split_message[j] in webtext.raw(corp_type)[:100000000]:
            #print(split_message[j]+" is not in")
            print(split_message[j])
            split_message.remove(split_message[j])
            print(split_message)
        j+=1


#for fileid in webtext.fileids():
#    print(fileid)
if __name__ == '__main__':
    for fileid in webtext.fileids():
        print(fileid)
    split_message=custom_tweet.split()
    rare_words("firefox.txt")
    rare_words("grail.txt")
    rare_words("pirates.txt")
    rare_words("overheard.txt")
    rare_words("wine.txt")
    rare_words("singles.txt")

