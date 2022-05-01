"""
Christian Johansson
Artificial Intelligence, Final Project
5/1/2022
Professor Silveyra

"""
import copy
import os
import string
import json
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
#nltk.download('stopwords')

REMOVE_STOPWORDS = True
STEM_WORDS = True


class SearchEngine:

    def __init__(self, query="Jorge Silveyra"):
        self.query = query
        self.invertedIndex = dict()
        self.stopWords = REMOVE_STOPWORDS
        self.stemming = STEM_WORDS
        self.denominator = dict()
        self.numerator = dict()
        self.maxFrequency = [0] * 10394

    def makeInvertedIndex(self):
        for filename in os.listdir("Text"):
            pageDictionary = dict()
            with open(os.path.join("Text", filename), 'r', errors='ignore') as f:
                text = f.read()
                text = text.lower()
                text = text.translate(str.maketrans('', '', string.punctuation))
                text = text.split()

                for word in text:
                    pageDictionary[word] = pageDictionary.get(word, 0) + 1

                if REMOVE_STOPWORDS and STEM_WORDS:
                    pageDictionary = self.filterStopWords(pageDictionary)
                    pageDictionary = self.filterStemming(pageDictionary)
                elif REMOVE_STOPWORDS:
                    pageDictionary = self.filterStopWords(pageDictionary)
                elif STEM_WORDS:
                    pageDictionary = self.filterStemming(pageDictionary)

                for word in pageDictionary:
                    if word not in self.invertedIndex:
                        self.invertedIndex[word] = [[int(filename.split(".")[0]), pageDictionary.get(word)]]
                    else:
                        self.invertedIndex[word].append([int(filename.split(".")[0]), pageDictionary.get(word)])

                if len(pageDictionary.values()):
                    self.maxFrequency[int(filename.split(".")[0])] = max(pageDictionary.values())
                else:
                    self.maxFrequency[int(filename.split(".")[0])] = 0

        if REMOVE_STOPWORDS and STEM_WORDS:
            with open("InvertedIndexBothFilters.json", "w") as outfile:
                json.dump(self.invertedIndex, outfile)
        elif REMOVE_STOPWORDS:
            with open("InvertedIndexJustStopwords.json", "w") as outfile:
                json.dump(self.invertedIndex, outfile)
        elif STEM_WORDS:
            with open("InvertedIndexJustStemming.json", "w") as outfile:
                json.dump(self.invertedIndex, outfile)
        else:
            with open("InvertedIndexNada.json", "w") as outfile:
                json.dump(self.invertedIndex, outfile)

    """
    Removes stopwords from the dictionary
    """
    def filterStopWords(self, unmodifiedDict):
        modifiedDict = unmodifiedDict
        # Get list of stopwords in english from nltk
        stopwordsList = set(stopwords.words('english'))
        # Any key that matches a stopword in the list is removed
        for word in stopwordsList:
            if word in [modifiedDict.keys()][0]:
                modifiedDict.pop(word)
        return modifiedDict

    """
    
    """
    def filterStemming(self, unmodifiedDict):
        modifiedDict = unmodifiedDict
        dictCopy = copy.copy(modifiedDict)
        stemmer = PorterStemmer()
        for key in dictCopy:
            stemmed = stemmer.stem(key)
            if stemmed != key:
                if stemmed in modifiedDict:
                    modifiedDict[stemmed] = modifiedDict.get(stemmed) + modifiedDict.get(key)
                    modifiedDict.pop(key)
                else:
                    modifiedDict[stemmed] = modifiedDict.get(key)
                    modifiedDict.pop(key)
        return modifiedDict


t = SearchEngine()
t.makeInvertedIndex()
