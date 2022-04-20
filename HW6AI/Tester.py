"""
Christian Johansson
Artificial Intelligence, Homework 6
4/15/2022
Professor Silveyra
This file is the tester for naive Bayesian learning, in which the precision,
recall and accuracy are determined. Tests are preformed on unmodified, removed stopwords
and lemmatizied versions of the learning.
"""

import Filter
import Learn


def main():
    Learn.Learn()
    Learn.Learn().training()

    # Enron 2 statistics. Precision, Recall, and Accuracy &
    # Enron 3 statistics. Precision, Recall, and Accuracy
    test1 = Filter.Filter()
    testBasic = test1.categorize()
    # All statistics are formatted to 3 decimal places and given in %
    print("Enron 2 statistics. Precision: " + "{:.3f}".format((testBasic[0]/(testBasic[0]+testBasic[1]))*100) +
          ", Recall: " + "{:.3f}".format((testBasic[0]/(testBasic[0]+testBasic[2]))*100) +
          ", and Accuracy: " + "{:.3f}".format(((testBasic[0]+testBasic[3])/(testBasic[0]+testBasic[1]+testBasic[2]+testBasic[3]))*100))
    print("Enron 3 statistics. Precision: " + "{:.3f}".format(testBasic[4] / (testBasic[4] + testBasic[5])) +
          ", Recall: " + "{:.3f}".format((testBasic[4] / (testBasic[4] + testBasic[6]))*100) +
          ", and Accuracy: " + "{:.3f}".format((
        (testBasic[4] + testBasic[7]) / (testBasic[4] + testBasic[5] + testBasic[6] + testBasic[7]))*100))

    # Enron 2 statistics. Precision, Recall, and Accuracy removing stopwords &
    # Enron 3 statistics. Precision, Recall, and Accuracy removing stopwords
    test2 = Filter.Filter(True)
    testStopWords = test2.categorize()
    # All statistics are formatted to 3 decimal places and given in %
    print("Enron 2 statistics no stopwords. Precision: " + "{:.3f}".format((testStopWords[0] / (testStopWords[0] + testStopWords[1]))*100) +
          ", Recall: " + "{:.3f}".format((testStopWords[0] / (testStopWords[0] + testStopWords[2]))*100) +
          ", and Accuracy: " + "{:.3f}".format((
        (testStopWords[0] + testStopWords[3]) / (testStopWords[0] + testStopWords[1] + testStopWords[2] + testStopWords[3]))*100))
    print("Enron 3 statistics no stopwords. Precision: " + "{:.3f}".format((testStopWords[4] / (testStopWords[4] + testStopWords[5]))*100) +
          ", Recall: " + "{:.3f}".format((testStopWords[4] / (testStopWords[4] + testStopWords[6]))*100) +
          ", and Accuracy: " + "{:.3f}".format((
        (testStopWords[4] + testStopWords[7]) / (testStopWords[4] + testStopWords[5] + testStopWords[6] + testStopWords[7]))*100))

    # Enron 2 statistics. Precision, Recall, and Accuracy lemmatization &
    # Enron 3 statistics. Precision, Recall, and Accuracy lemmatization
    test3 = Filter.Filter(False, True)
    testLemmatization = test3.categorize()
    # All statistics are formatted to 3 decimal places and given in %
    print("Enron 2 statistics with lemmatization. Precision: " + "{:.3f}".format((testLemmatization[0] / (testLemmatization[0] + testLemmatization[1]))*100) +
          ", Recall: " + "{:.3f}".format((testLemmatization[0] / (testLemmatization[0] + testLemmatization[2]))*100) +
          ", and Accuracy: " + "{:.3f}".format((
        (testLemmatization[0] + testLemmatization[3]) / (testLemmatization[0] + testLemmatization[1] + testLemmatization[2] + testLemmatization[3]))*100))
    print("Enron 3 statistics with lemmatization. Precision: " + "{:.3f}".format((testLemmatization[4] / (testLemmatization[4] + testLemmatization[5]))*100) +
          ", Recall: " + "{:.3f}".format((testLemmatization[4] / (testLemmatization[4] + testLemmatization[6]))*100) +
          ", and Accuracy: " + "{:.3f}".format((
        (testLemmatization[4] + testLemmatization[7]) / (testLemmatization[4] + testLemmatization[5] + testLemmatization[6] + testLemmatization[7]))*100))

    # Enron 2 statistics. Precision, Recall, and Accuracy removing stopwords and lemmatization &
    # Enron 3 statistics. Precision, Recall, and Accuracy removing stopwords and lemmatization
    test3 = Filter.Filter(True, True)
    testBoth = test3.categorize()
    # All statistics are formatted to 3 decimal places and given in %
    print("Enron 2 statistics with both. Precision: " + "{:.3f}".format((testBoth[0] / (testBoth[0] + testBoth[1]))*100) +
          ", Recall: " + "{:.3f}".format((testBoth[0] / (testBoth[0] + testBoth[2]))*100) +
          ", and Accuracy: " + "{:.3f}".format((
        (testBoth[0] + testBoth[3]) / (testBoth[0] + testBoth[1] + testBoth[2] + testBoth[3]))*100))
    print("Enron 3 statistics with both. Precision: " + "{:.3f}".format((testBoth[4] / (testBoth[4] + testBoth[5]))*100) +
          ", Recall: " + "{:.3f}".format((testBoth[4] / (testBoth[4] + testBoth[6]))*100) +
          ", and Accuracy: " + "{:.3f}".format((
        (testBoth[4] + testBoth[7]) / (testBoth[4] + testBoth[5] + testBoth[6] + testBoth[7]))*100))


if __name__ == '__main__':
    main()
