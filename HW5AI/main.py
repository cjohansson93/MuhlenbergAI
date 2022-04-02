"""
Christian Johansson
Artificial Intelligence, Homework 5
4/1/2022
Professor Silveyra
This file is the tester for a constraint satisfaction coloring problem. Each experiment contains differing
upgrade scenario combinations to the base algorithm, with the base as control. Each experiment is also run 100 times,
solutions out of 100 and average recursions across those successes is also given.
"""

import CSP


def main():

    # None: Backtracking only
    solutionsFound = 0
    totalRecursions = 0
    # Each experiment is run 100 times
    for i in range(100):
        #print("Start test ", i)
        recursions = CSP.CSP().solveCSP()
        if recursions > 0:
            solutionsFound += 1
            totalRecursions += recursions

    print("Found ", solutionsFound, " solutions using backtracking only.")
    print("Avg recursions was ", totalRecursions / solutionsFound)


    # Only A: Most constrained variable only
    solutionsFound = 0
    totalRecursions = 0
    # Each experiment is run 100 times
    for i in range(100):
        #print("Start test ", i)
        recursions = CSP.CSP(mostConstrained=True).solveCSP()
        if recursions > 0:
            solutionsFound += 1
            totalRecursions += recursions

    print("Found ", solutionsFound, " solutions using most constrained only.")
    print("Avg recursions was ", totalRecursions / solutionsFound)


    # Only B: Most constraining variable only
    solutionsFound = 0
    totalRecursions = 0
    # Each experiment is run 100 times
    for i in range(100):
        #print("Start test ", i)
        recursions = CSP.CSP(mostConstraining=True).solveCSP()
        if recursions > 0:
            solutionsFound += 1
            totalRecursions += recursions

    print("Found ", solutionsFound, " solutions using most constraining only.")
    print("Avg recursions was ", totalRecursions / solutionsFound)


    # Only C: The least constraining value only
    solutionsFound = 0
    totalRecursions = 0
    # Each experiment is run 100 times
    for i in range(100):
        #print("Start test ", i)
        recursions = CSP.CSP(leastConstraining=True).solveCSP()
        if recursions > 0:
            solutionsFound += 1
            totalRecursions += recursions

    print("Found ", solutionsFound, " solutions using least constraining only.")
    print("Avg recursions was ", totalRecursions / solutionsFound)


    # A and B: Most constrained variable and most constraining variable only
    solutionsFound = 0
    totalRecursions = 0
    # Each experiment is run 100 times
    for i in range(100):
        #print("Start test ", i)
        recursions = CSP.CSP(mostConstrained=True, mostConstraining=True).solveCSP()
        if recursions > 0:
            solutionsFound += 1
            totalRecursions += recursions

    print("Found ", solutionsFound,
          " solutions using most constrained and most constraining only.")
    print("Avg recursions was ", totalRecursions / solutionsFound)


    # A and C: Most constrained variable and least constraining value only
    solutionsFound = 0
    totalRecursions = 0
    # Each experiment is run 100 times
    for i in range(100):
        #print("Start test ", i)
        recursions = CSP.CSP(mostConstrained=True, leastConstraining=True).solveCSP()
        if recursions > 0:
            solutionsFound += 1
            totalRecursions += recursions

    print("Found ", solutionsFound,
          " solutions using most constrained and least constraining only.")
    print("Avg recursions was ", totalRecursions / solutionsFound)


    # B and C: Most constraining variable and most constraining variable only
    solutionsFound = 0
    totalRecursions = 0
    # Each experiment is run 100 times
    for i in range(100):
        #print("Start test ", i)
        recursions = CSP.CSP(mostConstraining=True, leastConstraining=True).solveCSP()
        if recursions > 0:
            solutionsFound += 1
            totalRecursions += recursions

    print("Found ", solutionsFound,
          " solutions using most constraining, and least constraining only.")
    print("Avg recursions was ", totalRecursions / solutionsFound)


    # A and B and C: Most constrained variable and most constraining variable and least constraining value.
    solutionsFound = 0
    totalRecursions = 0
    # Each experiment is run 100 times
    for i in range(100):
        #print("Start test ", i)
        recursions = CSP.CSP(mostConstrained=True, mostConstraining=True, leastConstraining=True).solveCSP()
        if recursions > 0:
            solutionsFound += 1
            totalRecursions += recursions

    print("Found ", solutionsFound, " solutions using most constrained, most constraining, and least constraining only.")
    print("Avg recursions was ", totalRecursions / solutionsFound)


if __name__ == "__main__":
    main()
