"""
Christian Johansson
Artificial Intelligence, Homework 6
4/15/2022
Professor Silveyra
This file is the learner for naive Bayesian learning. It makes a known directory of
spam and non-spam(ham) .txt files, reads them word by word and adds them to a dictionary with
word counts. This dictionary is made into a .json file
"""
import os
import json

# Global variable for names of json files and directories
HAM_DIRECTORY = "ham"
HAM_JSON = "hamWordBag.json"
SPAM_DIRECTORY = "spam"
SPAM_JSON = "spamWordBag.json"


# Getters for the names of json files and directories
def getHAM_DIRECTORY():
    return HAM_DIRECTORY


def getHAM_JSON():
    return HAM_JSON


def getSPAM_DIRECTORY():
    return SPAM_DIRECTORY


def getSPAM_JSON():
    return SPAM_JSON


class Learn:

    """
    Constructor, initializes spam and ham dictionaries
    """
    def __init__(self):
        self.spamDictionary = dict()
        self.hamDictionary = dict()

    """
    Training for naive Bayesian learning, creates bag of words by reading .txt files for directory.
    Creates corresponding .json file
    """
    def training(self):
        # Get each .txt file in the ham directory
        for filename in os.listdir(HAM_DIRECTORY):
            # Open each file, ignoring unicode characters that can't be decoded
            with open(os.path.join(HAM_DIRECTORY, filename), 'r', errors='ignore') as f:
                text = f.read()
                # Make all words lowercase and turn into list
                text = text.lower()
                text = text.split()
                # Add unique words to dictionary or increment if already present
                for word in text:
                    self.hamDictionary[word] = self.hamDictionary.get(word, 0) + 1

        # Get each .txt file in the spam directory
        for filename in os.listdir(SPAM_DIRECTORY):
            # Open each file, ignoring unicode characters that can't be decoded
            with open(os.path.join(SPAM_DIRECTORY, filename), 'r', errors='ignore') as f:
                text = f.read()
                # Make all words lowercase and turn into list
                text = text.lower()
                text = text.split()
                # Add unique words to dictionary or increment if already present
                for word in text:
                    self.spamDictionary[word] = self.spamDictionary.get(word, 0) + 1

        # Turn both dictionaries to .json files
        with open(HAM_JSON, "w") as outfile:
            json.dump(self.hamDictionary, outfile)

        with open(SPAM_JSON, "w") as outfile:
            json.dump(self.spamDictionary, outfile)
