"""
Christian Johansson
Artificial Intelligence, Homework 6
4/15/2022
Professor Silveyra
This file is the filter for naive Bayesian learning. It can alter the bag of words made from Learn.py
to remove stopwords and/or lemmatize words. It then can proceed to classify new text files as spam or ham
based on naive Bayesian learning. All alterations to the bag of words are saved as new .json files
"""

import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import json
import Learn
import copy
import os
import math
# nltk.download('stopwords')
# nltk.download('wordnet')
# nltk.download('omw-1.4')

# Global variable for names of json files and directories
# as well as turning off/on prints
PRINT_MESSAGES = False
HAM_JSON_SW = "hamNotStopWordsBag.jason"
HAM_JSON_LEM = "hamLemmatizationBag.json"
HAM_JSON_SW_LEM = "hamUltimateFormBag.json"
SPAM_JSON_SW = "spamNotStopWordsBag.jason"
SPAM_JSON_LEM = "spamLemmatizationBag.json"
SPAM_JSON_SW_LEM = "spamUltimateFormBag.json"
TEST_HAM_DIRECTORY3 = "ham3"
TEST_SPAM_DIRECTORY3 = "spam3"
TEST_HAM_DIRECTORY2 = "ham2"
TEST_SPAM_DIRECTORY2 = "spam2"


class Filter:

    """
    Constructor for Filter. Takes bag of words for ham and spam .json files and turns them
    into dictionaries.
    @:param removeStopWords boolean control variable for removal of stopwords
    @:param lemmatization boolean control variable for the lemmatization of words
    """
    def __init__(self, removeStopWords=False, lemmatization=False):
        # Boolean controls
        self.removeStopWords = removeStopWords
        self.lemmatization = lemmatization
        # Turning ham and spam .json files into dictionaries
        with open(Learn.getSPAM_JSON()) as jsonFile:
            self.spamDictionary = dict()
            self.spamDictionary = json.load(jsonFile)
        with open(Learn.getHAM_JSON()) as jsonFile:
            self.hamDictionary = dict()
            self.hamDictionary = json.load(jsonFile)

    """
    Categorizes new text files as spam or ham according to naive Bayesian learning
    comparison with bag of words
    """
    def categorize(self):
        # Preform any alterations to the bag of words dictionaries by call out
        if self.removeStopWords and self.lemmatization:
            self.filterStopWords()
            self.filterLemmatization()
        elif self.removeStopWords:
            self.filterStopWords()
        elif self.lemmatization:
            self.filterLemmatization()

        # Total counted sum of all word values in dictionaries
        countHam = sum([self.hamDictionary.values()][0])
        countSpam = sum([self.spamDictionary.values()][0])

        # Metrics to be returned for accuracy, precision and recall
        truePositive2 = 0
        falsePositive2 = 0
        trueNegative2 = 0
        falseNegative2 = 0
        # Counter so that message count can be seen if desired
        counter = 1
        if PRINT_MESSAGES:
            print("Enron 2:")
        # Open known ham testing directory from enron 2
        for filename in os.listdir(TEST_HAM_DIRECTORY2):
            # Variables for evaluating spam or ham category placing of text
            spam = 0
            ham = 0
            with open(os.path.join(TEST_HAM_DIRECTORY2, filename), 'r', errors='ignore') as f:
                text = f.read()
                # Make all words lowercase and turn into list
                text = text.lower()
                text = text.split()
                # For each word sum the log10 of that words count value in corresponding dictionary
                # over sum of the total sum word counts in that dictionary and the number of unique words
                for word in text:
                    spam += math.log10(self.hamDictionary.get(word, 1) / (countHam + len(self.hamDictionary)))
                    ham += math.log10(self.spamDictionary.get(word, 1) / (countSpam + len(self.spamDictionary)))
                # Adding in the log10 of the probability of a word belonging to that category
                spam += math.log10(len(self.spamDictionary) / (len(self.spamDictionary) + len(self.hamDictionary)))
                ham += math.log10(len(self.hamDictionary) / (len(self.spamDictionary) + len(self.hamDictionary)))
                # Spam or ham determination for text based on which had a larger value in the end
                # corresponding metric is incremented along with the counter, option message print
                if spam > ham:
                    counter += 1
                    falseNegative2 += 1
                    if PRINT_MESSAGES:
                        print("Message " + str(counter) + ": " + str(spam) + " Spam. Real: Ham.")
                else:
                    counter += 1
                    trueNegative2 += 1
                    if PRINT_MESSAGES:
                        print("Message " + str(counter) + ": " + str(ham) + " Ham. Real: Ham.")

        # Open known spam testing directory from enron 2
        for filename in os.listdir(TEST_SPAM_DIRECTORY2):
            spam = 0
            ham = 0
            with open(os.path.join(TEST_SPAM_DIRECTORY2, filename), 'r', errors='ignore') as f:
                text = f.read()
                # Make all words lowercase and turn into list
                text = text.lower()
                text = text.split()
                # For each word sum the log10 of that words count value in corresponding dictionary
                # over sum of the total sum word counts in that dictionary and the number of unique words
                for word in text:
                    spam += math.log10(self.hamDictionary.get(word, 1) / (countHam + len(self.hamDictionary)))
                    ham += math.log10(self.spamDictionary.get(word, 1) / (countSpam + len(self.spamDictionary)))
                # Adding in the log10 of the probability of a word belonging to that category
                spam += math.log10(len(self.spamDictionary)/(len(self.spamDictionary)+len(self.hamDictionary)))
                ham += math.log10(len(self.hamDictionary)/(len(self.spamDictionary)+len(self.hamDictionary)))
                # Spam or ham determination for text based on which had a larger value in the end
                # corresponding metric is incremented along with the counter, option message print
                if spam > ham:
                    counter += 1
                    truePositive2 += 1
                    if PRINT_MESSAGES:
                        print("Message " + str(counter) + ": " + str(spam) + " Spam. Real: Spam.")
                else:
                    counter += 1
                    falsePositive2 += 1
                    if PRINT_MESSAGES:
                        print("Message " + str(counter) + ": " + str(ham) + " Ham. Real: Spam.")

        # Metrics to be returned for accuracy, precision and recall
        truePositive3 = 0
        falsePositive3 = 0
        trueNegative3 = 0
        falseNegative3 = 0
        # Counter so that message count can be seen if desired
        counter = 1
        if PRINT_MESSAGES:
            print("Enron 3:")
        # Open known ham testing directory from enron 3
        for filename in os.listdir(TEST_HAM_DIRECTORY3):
            spam = 0
            ham = 0
            with open(os.path.join(TEST_HAM_DIRECTORY3, filename), 'r', errors='ignore') as f:
                text = f.read()
                text = text.lower()
                text = text.split()
                # For each word sum the log10 of that words count value in corresponding dictionary
                # over sum of the total sum word counts in that dictionary and the number of unique words
                for word in text:
                    spam += math.log10(self.hamDictionary.get(word, 1) / (countHam + len(self.hamDictionary)))
                    ham += math.log10(self.spamDictionary.get(word, 1) / (countSpam + len(self.spamDictionary)))
                # Adding in the log10 of the probability of a word belonging to that category
                spam += math.log10(len(self.spamDictionary) / (len(self.spamDictionary) + len(self.hamDictionary)))
                ham += math.log10(len(self.hamDictionary) / (len(self.spamDictionary) + len(self.hamDictionary)))
                # Spam or ham determination for text based on which had a larger value in the end
                # corresponding metric is incremented along with the counter, option message print
                if spam > ham:
                    counter += 1
                    falseNegative3 += 1
                    if PRINT_MESSAGES:
                        print("Message " + str(counter) + ": " + str(spam) + " Spam. Real: Ham.")
                else:
                    counter += 1
                    trueNegative3 += 1
                    if PRINT_MESSAGES:
                        print("Message " + str(counter) + ": " + str(ham) + " Ham. Real: Ham.")

        # Open known testing directory from enron 3
        for filename in os.listdir(TEST_SPAM_DIRECTORY3):
            spam = 0
            ham = 0
            with open(os.path.join(TEST_SPAM_DIRECTORY3, filename), 'r', errors='ignore') as f:
                text = f.read()
                text = text.lower()
                text = text.split()
                for word in text:
                    spam += math.log10(self.hamDictionary.get(word, 1) / (countHam + len(self.hamDictionary)))
                    ham += math.log10(self.spamDictionary.get(word, 1) / (countSpam + len(self.spamDictionary)))
                spam += math.log10(len(self.spamDictionary) / (len(self.spamDictionary) + len(self.hamDictionary)))
                ham += math.log10(len(self.hamDictionary) / (len(self.spamDictionary) + len(self.hamDictionary)))
                if spam > ham:
                    counter += 1
                    truePositive3 += 1
                    if PRINT_MESSAGES:
                        print("Message " + str(counter) + ": " + str(spam) + " Spam. Real: Spam.")
                else:
                    counter += 1
                    falsePositive3 += 1
                    if PRINT_MESSAGES:
                        print("Message " + str(counter) + ": " + str(ham) + " Ham. Real: Spam.")

        return truePositive2,falsePositive2,trueNegative2,falseNegative2,truePositive3,falsePositive3,trueNegative3,falseNegative3

    """
    Removes stopwords from the dictionaries
    """
    def filterStopWords(self):
        # Get list of stopwords in english from nltk
        stopwordsList = set(stopwords.words('english'))
        # Any key that matches a stopword in the list is removed
        for word in stopwordsList:
            if word in [self.hamDictionary.keys()][0]:
                self.hamDictionary.pop(word)
            if word in [self.spamDictionary.keys()][0]:
                self.spamDictionary.pop(word)
        # Changes saved to .json
        self.saveToFile()

    """
    Preforms lemmatization of a dictionary of words, adding the lemmatized word,
    count from the original and removal of old word. Counts are combined if word exists.
    """
    def filterLemmatization(self):
        # Gives access to lemmatization from nltk
        lemmatizer = WordNetLemmatizer()
        # Shallow copies of dictionaries are made as to avoid error
        # when altering a dictionary which iterating through its keys
        hamCopy = copy.copy(self.hamDictionary)
        spamCopy = copy.copy(self.spamDictionary)
        # Keys in ham
        for key in hamCopy:
            lemmatized = lemmatizer.lemmatize(key)
            # Stops lemmatization of an already present key (avoids duplicates)
            if lemmatized != key:
                # If the key is already in dictionary the values are summed and the old key deleted
                if lemmatized in self.hamDictionary:
                    self.hamDictionary[lemmatized] = self.hamDictionary.get(lemmatized) + self.hamDictionary.get(key)
                    self.hamDictionary.pop(key)
                # New key made with old keys value and old key removed
                else:
                    self.hamDictionary[lemmatized] = self.hamDictionary.get(key)
                    self.hamDictionary.pop(key)
        # Keys in spam
        for key in spamCopy:
            lemmatized = lemmatizer.lemmatize(key)
            # Stops lemmatization of an already present key (avoids duplicates)
            if lemmatized != key:
                # If the key is already in dictionary the values are summed and the old key deleted
                if lemmatized in self.spamDictionary:
                    self.spamDictionary[lemmatized] = self.spamDictionary.get(lemmatized) + self.spamDictionary.get(key)
                    self.spamDictionary.pop(key)
                # New key made with old keys value and old key removed
                else:
                    self.spamDictionary[lemmatized] = self.spamDictionary.get(key)
                    self.spamDictionary.pop(key)
        # Changes saved to .json
        self.saveToFile()

    """
    Saves ham & spam dictionaries into .json files, corresponds to the alteration of the original
    bag of words. i.e removal of stopwords and/or lemmatization
    """
    def saveToFile(self):
        # Removal of stopwords and lemmatization
        if self.removeStopWords and self.lemmatization:
            with open(HAM_JSON_SW_LEM, "w") as outfile:
                json.dump(self.hamDictionary, outfile)

            with open(SPAM_JSON_SW_LEM, "w") as outfile:
                json.dump(self.spamDictionary, outfile)
        # Removal of stopwords only
        elif self.removeStopWords:
            with open(HAM_JSON_SW, "w") as outfile:
                json.dump(self.hamDictionary, outfile)

            with open(SPAM_JSON_SW, "w") as outfile:
                json.dump(self.spamDictionary, outfile)
        # Lemmatization only
        elif self.lemmatization:
            with open(HAM_JSON_LEM, "w") as outfile:
                json.dump(self.hamDictionary, outfile)

            with open(SPAM_JSON_LEM, "w") as outfile:
                json.dump(self.spamDictionary, outfile)
