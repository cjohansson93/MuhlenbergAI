"""
Christian Johansson
Artificial Intelligence, Final Project
5/1/2022
Professor Silveyra
This program is a mini search engine for the muhlenberg.edu website, with simple menu.
Using text from crawled pages an inverted index is made from which an entered query can
produce results by Tf-idf ranking. Results are displayed as top 10 links to pages relevant to search.
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

# Globals for word filters and total number documents
REMOVE_STOPWORDS = True
STEM_WORDS = True
TOTAL_DOCUMENTS = 10393

"""
Mini search engine for the muhlenberg.edu website, with simple menu. 
Using text from crawled pages an inverted index is made from which an entered query can 
produce results by Tf-idf ranking. Results are displayed as top 10 links to pages relevant to search.
"""
class SearchEngine:

    """
    Class constructor, initializes query, dictionaries for tf-idf ranking calculations
    and word filtering conditions.
    """
    def __init__(self, query="Jorge Silveyra"):
        self.query = query
        self.invertedIndex = dict()
        # Word filters
        self.stopWords = REMOVE_STOPWORDS
        self.stemming = STEM_WORDS
        # Used in tf-idf ranking calculations
        self.denominator = dict()
        self.numerator = dict()
        # Each index corresponds to a document, storing max frequency
        # of said document (Empty initialization here)
        self.maxFrequency = [0] * (TOTAL_DOCUMENTS+1)

    """
    Makes inverted index from text documents in directory 'Text'. Index key for each unique
    word across documents. Stored value consists of pair value list(s), pair is composed of
    document number followed by the number of times that word appears in it. Max word frequency
    is also determined for any given document in this process as well.
    Index can be altered by none, one or both word filtering processes.
    """
    def makeInvertedIndex(self):
        # Open and read every .txt file in directory, turn into split list
        for filename in os.listdir("Text"):
            # Temporary dictionary for each page
            pageDictionary = dict()
            with open(os.path.join("Text", filename), 'r', errors='ignore') as f:
                text = f.read()
                # Remove case sensitivity and punctuation
                text = text.lower()
                text = text.translate(str.maketrans('', '', string.punctuation))
                text = text.split()

                # Fill temp dictionary with words from that page
                for word in text:
                    pageDictionary[word] = pageDictionary.get(word, 0) + 1

                # Optionally clean out stop words and/or stem words
                if REMOVE_STOPWORDS and STEM_WORDS:
                    pageDictionary = self.filterStopWords(pageDictionary)
                    pageDictionary = self.filterStemming(pageDictionary)
                elif REMOVE_STOPWORDS:
                    pageDictionary = self.filterStopWords(pageDictionary)
                elif STEM_WORDS:
                    pageDictionary = self.filterStemming(pageDictionary)

                # Add unique words to inverted index dictionary, or sum word count if already present
                for word in pageDictionary:
                    if word not in self.invertedIndex:
                        self.invertedIndex[word] = [[int(filename.split(".")[0]), pageDictionary.get(word)]]
                    else:
                        self.invertedIndex[word].append([int(filename.split(".")[0]), pageDictionary.get(word)])

                # Store page/documents maximum word count across all its words into list
                # where document name = index in list (self.maxFrequency)
                if len(pageDictionary.values()):
                    self.maxFrequency[int(filename.split(".")[0])] = max(pageDictionary.values())
                else:
                    self.maxFrequency[int(filename.split(".")[0])] = 0

        # Write altered inverted dictionaries to .json files
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
    @:param unmodifiedDict An unmodified dictionary with word keys and frequency values,
                           to preform the filter on
    @:returns modifiedDict A modified version of unmodified dictionary with stop words removed
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
    Stems words in dictionary to their root.
    @:param unmodifiedDict An unmodified dictionary with word keys and frequency values,
                           to preform the filter on
    @:returns modifiedDict A modified version of unmodified dictionary with words stemmed
    """
    def filterStemming(self, unmodifiedDict):
        modifiedDict = unmodifiedDict
        # Make shallow copy to allow iteration or keys while altering original
        dictCopy = copy.copy(modifiedDict)
        # From nltk stemming sub library
        stemmer = PorterStemmer()
        for key in dictCopy:
            # Each key is stemming, only roots different from key matter
            stemmed = stemmer.stem(key)
            if stemmed != key:
                # If the root word exists in inverted index, values summed and original key removed
                # else a new key is make with previous key's value and original key removed
                if stemmed in modifiedDict:
                    modifiedDict[stemmed] = modifiedDict.get(stemmed) + modifiedDict.get(key)
                    modifiedDict.pop(key)
                else:
                    modifiedDict[stemmed] = modifiedDict.get(key)
                    modifiedDict.pop(key)
        return modifiedDict

    """
    Preforms cleaning of user search query. Removes capitalization, punctuation and optionally
    stop words and/or stemming of words. Query is then turned into a dictionary and max frequency
    stored in list at index 0.
    @:returns queryDictionary A dictionary based on query with word keys and frequency values
    """
    def processQuery(self):
        queryDictionary = dict()
        # Remove case sensitivity and punctuation, turn into list
        modifiedQuery = self.query.lower()
        modifiedQuery = modifiedQuery.translate(str.maketrans('', '', string.punctuation))
        modifiedQuery = modifiedQuery.split()

        # Fill temp dictionary with words from that query
        for word in modifiedQuery:
            queryDictionary[word] = queryDictionary.get(word, 0) + 1

        # Optionally clean out stop words and/or stem words
        if REMOVE_STOPWORDS and STEM_WORDS:
            queryDictionary = self.filterStopWords(queryDictionary)
            queryDictionary = self.filterStemming(queryDictionary)
        elif REMOVE_STOPWORDS:
            queryDictionary = self.filterStopWords(queryDictionary)
        elif STEM_WORDS:
            queryDictionary = self.filterStemming(queryDictionary)

        # Store page/documents maximum word count across all its words into list
        # where query max = index[0] in list (self.maxFrequency)
        if len(queryDictionary.values()):
            self.maxFrequency[0] = max(queryDictionary.values())
        else:
            self.maxFrequency[0] = 1

        return queryDictionary

    """
    Calculates ranking of document's relevance to query using tf-idf of query and documents.
    Top 10 most relevant URLs to the search query are displayed
    """
    def results(self):
        # Clean query
        query = self.processQuery()
        # Only calculate tf-idf for term in query that exists in inverted index
        for term in query:
            if term in self.invertedIndex:
                # Calculation is preformed for each time that word appears in query
                for i in range(query.get(term)):
                    tfidfQ = (query.get(term)/self.maxFrequency[0]) * math.log10(TOTAL_DOCUMENTS/len(self.invertedIndex[term]))
                    self.denominator["q"] = self.denominator.get("q", 0) + tfidfQ**2
                    for doc in self.invertedIndex[term]:
                        tfidfDoc = (doc[1]/self.maxFrequency[doc[1]]) * math.log10(TOTAL_DOCUMENTS/len(self.invertedIndex[term]))
                        self.denominator[str(doc[0])] = self.denominator.get(str(doc[0]), 0) + tfidfDoc**2
                        self.numerator[str(doc[0])] = self.numerator.get(str(doc[0]), 0) + ((tfidfQ**2) * (tfidfDoc**2))
        # Values stored in heap for sorting by value
        heap = []
        for key in self.numerator:
            value = self.numerator.get(key) / math.sqrt(self.denominator.get("q") + self.denominator.get(key))
            heapq.heappush(heap, (value, key))

        # Printing of the top 10 pages rankings and URLs
        print("Top 10 Page Results: \n")
        for i in heapq.nlargest(10, heap):
            with open('Pages/page' + i[1] + '.txt', 'r', encoding='utf-8') as f:
                print("Value: {:.3f}".format(i[0]) + ", URL: " + f.read())

    """
    Simple menu to allow for multiple query searches or program exit
    """
    def menu(self):
        print("Please wait, initializing inverted index.")
        t.makeInvertedIndex()
        proceed = True
        while proceed:
            print("-------Muhlenberg.edu Mini Search Engine Menu-------")
            print("1: Enter query \n2: Exit Program")
            answer = input("Enter corresponding number to action: ")
            if answer == "1":
                self.query = input("Enter search query: ")
                t.results()
            elif answer == "2":
                proceed = False
            else:
                print("Invalid choice selection.\n")


t = SearchEngine()
t.menu()
