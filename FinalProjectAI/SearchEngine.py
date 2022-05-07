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
import math
import heapq
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
#nltk.download('stopwords')

REMOVE_STOPWORDS = True
STEM_WORDS = True
TOTAL_DOCUMENTS = 10393


class SearchEngine:

    def __init__(self, query="Jorge Silveyra"):
        self.query = query
        self.invertedIndex = dict()
        self.stopWords = REMOVE_STOPWORDS
        self.stemming = STEM_WORDS
        self.denominator = dict()
        self.numerator = dict()
        self.maxFrequency = [0] * (TOTAL_DOCUMENTS+1)

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

    def processQuery(self):
        queryDictionary = dict()
        modifiedQuery = self.query.lower()
        modifiedQuery = modifiedQuery.translate(str.maketrans('', '', string.punctuation))
        modifiedQuery = modifiedQuery.split()

        for word in modifiedQuery:
            queryDictionary[word] = queryDictionary.get(word, 0) + 1

        if REMOVE_STOPWORDS and STEM_WORDS:
            queryDictionary = self.filterStopWords(queryDictionary)
            queryDictionary = self.filterStemming(queryDictionary)
        elif REMOVE_STOPWORDS:
            queryDictionary = self.filterStopWords(queryDictionary)
        elif STEM_WORDS:
            queryDictionary = self.filterStemming(queryDictionary)

        if len(queryDictionary.values()):
            self.maxFrequency[0] = max(queryDictionary.values())
        else:
            self.maxFrequency[0] = 1

        return queryDictionary

    def results(self):
        query = self.processQuery()
        print("Query: " + self.query)
        for term in query:
            if term in self.invertedIndex:
                for i in range(query.get(term)):
                    tfidfQ = (query.get(term)/self.maxFrequency[0]) * math.log10(TOTAL_DOCUMENTS/len(self.invertedIndex[term]))
                    self.denominator["q"] = self.denominator.get("q", 0) + tfidfQ**2
                    for doc in self.invertedIndex[term]:
                        tfidfDoc = (doc[1]/self.maxFrequency[doc[1]]) * math.log10(TOTAL_DOCUMENTS/len(self.invertedIndex[term]))
                        self.denominator[str(doc[0])] = self.denominator.get(str(doc[0]), 0) + tfidfDoc**2
                        self.numerator[str(doc[0])] = self.numerator.get(str(doc[0]), 0) + ((tfidfQ**2) * (tfidfDoc**2))
        heap = []
        for key in self.numerator:
            value = self.numerator.get(key) / math.sqrt(self.denominator.get("q") + self.denominator.get(key))
            heapq.heappush(heap, (value, key))

        print("Top 10 Page Results: \n")
        for i in heapq.nlargest(10, heap):
            with open('Pages/page' + i[1] + '.txt', 'r', encoding='utf-8') as f:
                print("Value: {:.3f}".format(i[0]) + ", URL: " + f.read())


t = SearchEngine()
t.makeInvertedIndex()
t.results()
