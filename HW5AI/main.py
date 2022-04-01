import CSP


def main():
    # solutionsFound = 0
    # totalRecursions = 0
    # for i in range(100):
    #     print("Start test ", i)
    #     recursions = CSP.CSP().solveCSP()
    #     if recursions > 0:
    #         solutionsFound += 1
    #         totalRecursions += recursions

    # print("Found ", solutionsFound, " solutions.")
    # print("Avg recursions was ", totalRecursions / solutionsFound)

    solutionsFound = 0
    totalRecursions = 0
    for i in range(100):
        print("Start test ", i)
        recursions = CSP.CSP(mostConstrained=True).solveCSP()
        if recursions > 0:
            solutionsFound += 1
            totalRecursions += recursions

    print("Found ", solutionsFound, " solutions.")
    print("Avg recursions was ", totalRecursions / solutionsFound)

if __name__ == "__main__":
    main()
