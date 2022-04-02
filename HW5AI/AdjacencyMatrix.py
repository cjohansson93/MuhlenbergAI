"""
Christian Johansson
Artificial Intelligence, Homework 5
4/1/2022
Professor Silveyra
This file creates an adjacency list with changeable node and interconnectivity quantity.
"""

import random


class AdjacencyMatrix:

    """
    Constructor for adjacency list
    @param maxConnections Integer representing the maximum number of connections per node
    @param connectionChance Integer representing the minimum threshold to obtain a new connection.
    """
    def __init__(self, maxConnections=3, connectionChance=25):
        # Node quantity is randomly generated between 200-500, changeable
        self.numNodes = random.randint(200, 500)
        # First integer is the color, first list is possible colors when not colored,
        # second list is empty and to be filled with index of connection to that node
        self.Alist = [[0, [1, 2, 3], []] for i in range(self.numNodes)]
        for i in range(self.numNodes):
            # If requirements met, node gains a connection
            while random.randint(0,100) >= connectionChance and len(self.Alist[i][2]) < maxConnections:
                # Prevent self connections
                while True:
                    tempConnection = random.randint(0,self.numNodes-1)
                    if len(self.Alist[tempConnection][2]) > maxConnections - 1:
                        continue
                    else:
                        break
                # Prevent duplicate connections
                if tempConnection != i and tempConnection not in self.Alist[i][2]:
                    self.Alist[i][2].append(tempConnection)
                    self.Alist[tempConnection][2].append(i)
