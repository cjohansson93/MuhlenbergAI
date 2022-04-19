"""
Christian Johansson
Artificial Intelligence, Homework 6
4/15/2022
Professor Silveyra
This file is the filter for naive Bayesian learning
"""
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import json
import Learn
import copy
# nltk.download('stopwords')
# nltk.download('wordnet')
# nltk.download('omw-1.4')


class Filter:

    def __init__(self, removeStopWords=False, lemmatization=False):
        self.removeStopWords = removeStopWords
        self.lemmatization = lemmatization
        with open(Learn.getSPAM_JSON()) as jsonFile:
            self.spamDictionary = dict()
            self.spamDictionary = json.load(jsonFile)
        with open(Learn.getHAM_JSON()) as jsonFile:
            self.hamDictionary = dict()
            self.hamDictionary = json.load(jsonFile)
        # print(len(self.spamDictionary))
        # print(len(self.hamDictionary))

    def categorize(self):
        if self.removeStopWords:
            self.filterStopWords()
        if self.lemmatization:
            self.filterLemmatization()

    def filterStopWords(self):
        stopwordsList = set(stopwords.words('english'))
        for word in stopwordsList:
            if word in [self.hamDictionary.keys()][0]:
                self.hamDictionary.pop(word)
            if word in [self.spamDictionary.keys()][0]:
                self.spamDictionary.pop(word)
        # print(len(self.spamDictionary))
        # print(len(self.hamDictionary))

    def filterLemmatization(self):
        lemmatizer = WordNetLemmatizer()
        hamCopy = copy.copy(self.hamDictionary)
        spamCopy = copy.copy(self.spamDictionary)
        for key in hamCopy:
            lemmatized = lemmatizer.lemmatize(key)
            if lemmatized != key:
                if lemmatized in self.hamDictionary:
                    self.hamDictionary[lemmatized] = self.hamDictionary.get(lemmatized) + self.hamDictionary.get(key)
                    self.hamDictionary.pop(key)
                else:
                    self.hamDictionary[lemmatized] = self.hamDictionary.get(key)
                    self.hamDictionary.pop(key)
        for key in spamCopy:
            lemmatized = lemmatizer.lemmatize(key)
            if lemmatized != key:
                if lemmatized in self.spamDictionary:
                    self.spamDictionary[lemmatized] = self.spamDictionary.get(lemmatized) + self.spamDictionary.get(key)
                    self.spamDictionary.pop(key)
                else:
                    self.spamDictionary[lemmatized] = self.spamDictionary.get(key)
                    self.spamDictionary.pop(key)
        # print(len(self.spamDictionary))
        # print(len(self.hamDictionary))


test = Filter()
test.filterStopWords()
test.filterLemmatization()
