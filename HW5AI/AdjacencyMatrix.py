import random


class AdjacencyMatrix:

    def __init__(self, maxConnections = 3, connectionChance = 25):
        self.numNodes = random.randint(200, 500)
        self.Alist = [[0, [1, 2, 3], []] for i in range(self.numNodes)]
        for i in range(self.numNodes):
            while random.randint(0,100) >= connectionChance and len(self.Alist[i][2]) < maxConnections:
                while True:
                    tempConnection = random.randint(0,self.numNodes-1)
                    if len(self.Alist[tempConnection][2]) > maxConnections - 1:
                        continue
                    else:
                        break
                if tempConnection != i and tempConnection not in self.Alist[i][2]:
                    self.Alist[i][2].append(tempConnection)
                    self.Alist[tempConnection][2].append(i)
