import random


class AdjacencyMatrix:

    def __init__(self):
        self.numNodes = random.randint(200, 500)
        self.matrix = [[0,[1,2,3],[]] for i in range(self.numNodes)]
        for i in range(self.numNodes):
            while random.randint(0,100) >= 50:
                self.tempConnection = random.randint(0,self.numNodes-1)
                if self.tempConnection != i and self.tempConnection not in self.matrix[i][2]:
                    self.matrix[i][2].append(self.tempConnection)
                    self.matrix[self.tempConnection][2].append(i)
