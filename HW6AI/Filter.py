"""
Christian Johansson
Artificial Intelligence, Homework 6
4/15/2022
Professor Silveyra
This file is the filter for naive Bayesian learning
"""
import Learn
import nltk


class Filter:

    def __init__(self, removeStopWords=False, lemmatization=False):
        self.removeStopWords = removeStopWords
        self.lemmatization = lemmatization
        self.learned = Learn.Learn()
        self.learned.training()

    def categorize(self):
        if self.removeStopWords:
            self.filterStopWords()
        if self.lemmatization:
            self.filterLemmatization()



    def filterStopWords(self):
        pass

    def filterLemmatization(self):
        pass
