"""
Christian Johansson
Artificial Intelligence, Homework 6
4/15/2022
Professor Silveyra
This file is the learner for naive Bayesian learning
"""
import os
import json

HAM_DIRECTORY = "ham"
HAM_JSON = "hamWordBag.json"
SPAM_DIRECTORY = "spam"
SPAM_JSON = "spamWordBag.json"


def getHAM_DIRECTORY():
    return HAM_DIRECTORY


def getHAM_JSON():
    return HAM_JSON


def getSPAM_DIRECTORY():
    return SPAM_DIRECTORY


def getSPAM_JSON():
    return SPAM_JSON


class Learn:

    def __init__(self):
        self.spamDictionary = dict()
        self.hamDictionary = dict()

    def training(self):
        for filename in os.listdir(HAM_DIRECTORY):
            with open(os.path.join(HAM_DIRECTORY, filename), 'r', errors='ignore') as f:
                text = f.read()
                text = text.lower()
                text = text.split()
                for word in text:
                    self.hamDictionary[word] = self.hamDictionary.get(word, 0) + 1

        for filename in os.listdir(SPAM_DIRECTORY):
            with open(os.path.join(SPAM_DIRECTORY, filename), 'r', errors='ignore') as f:
                text = f.read()
                text = text.lower()
                text = text.split()
                for word in text:
                    self.spamDictionary[word] = self.spamDictionary.get(word, 0) + 1

        with open(HAM_JSON, "w") as outfile:
            json.dump(self.hamDictionary, outfile)

        with open(SPAM_JSON, "w") as outfile:
            json.dump(self.spamDictionary, outfile)

# test = Learn()
# test.training()
# print(test.hamDictionary)
# print("\n\n")
# print(test.spamDictionary)
