"""
Christian Johansson & Michael Norton
Artificial Intelligence, Homework 4
3/4/2022
Professor Silveyra
This file contains the environment for an agent. Environment is constructed as a grid in which a graph is based upon.
The width and height is retrievable, as well as determining if something is within bounds and printing the grid & graph.
Walls can be placed in the Grid and corresponding nodes in the graph will be removed.
"""

import random
import math


class Environment:
    """
    Constructor for grid
    Initializes a grid of lists with an X value, Y value, and binary integer wall placement.
    Grid is then used for construction of a graph, with connections to neighboring grids.
    @:param width of the environment
    @:param height of the environment
    """
    def __init__(self, width=10, height=10):
        self.width = width
        self.height = height
        # Graph is stored as a dictionary
        self.graph = dict()
        # Construction of empty list of lists size width x height
        self.grid = [[[] for i in range(height)] for j in range(width)]
        # Iterate through each internal list
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                self.grid[i][j].append(j)  # Adds x value
                self.grid[i][j].append(i)  # Adds y value
                self.grid[i][j].append(0)  # 1 = is a wall, 0 = not a wall

        # Grid to Graph conversion starts here
        # Iterates through all grid slots
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                # Makes key in dictionary for each grid slot (x,y)
                self.graph[(j, i)] = dict()
                # Prevents right side out of bounds
                if not ((j + 1) == 10):
                    # To stop assigning a new cost each time a node has a connection with the same node
                    # if sets its value to continue to equal what it's right neighbor has for that cost
                    if (j+1, i) in self.graph:
                        self.graph[(j, i)][(j+1, i)] = self.graph[(j+1, i)][(j, i)]
                    # If the connection is new its node is made and its coordinates, cost and heuristic is stored
                    else:
                        self.graph[(j, i)][(j + 1, i)] = [random.randint(1, 20), round(
                            math.sqrt(math.pow((i-9), 2) + math.pow((j-9), 2)), 2)]
                # Prevents left side out of bounds
                if not ((j - 1) == -1):
                    # To stop assigning a new cost each time a node has a connection with the same node
                    # if sets its value to continue to equal what it's left neighbor has for that cost
                    if (j - 1, i) in self.graph:
                        self.graph[(j, i)][(j - 1, i)] = self.graph[(j - 1, i)][(j, i)]
                    else:
                        # If the connection is new its node is made and its coordinates, cost and heuristic is stored
                        self.graph[(j, i)][(j - 1, i)] = [random.randint(1, 20), round(
                            math.sqrt(math.pow((i - 9), 2) + math.pow((j - 9), 2)), 2)]
                # Prevents bottom side out of bounds
                if not ((i + 1) == 10):
                    if (j, i+1) in self.graph:
                        # To stop assigning a new cost each time a node has a connection with the same node
                        # if sets its value to continue to equal what it's bottom neighbor has for that cost
                        self.graph[(j, i)][(j, i+1)] = self.graph[(j, i+1)][(j, i)]
                    else:
                        # If the connection is new its node is made and its coordinates, cost and heuristic is stored
                        self.graph[(j, i)][(j, i+1)] = [random.randint(1, 20), round(
                            math.sqrt(math.pow((i - 9), 2) + math.pow((j - 9), 2)), 2)]
                # Prevents top side out of bounds
                if not ((i - 1) == -1):
                    if (j, i - 1) in self.graph:
                        # To stop assigning a new cost each time a node has a connection with the same node
                        # if sets its value to continue to equal what it's top neighbor has for that cost
                        self.graph[(j, i)][(j, i - 1)] = self.graph[(j, i - 1)][(j, i)]
                    else:
                        # If the connection is new its node is made and its coordinates, cost and heuristic is stored
                        self.graph[(j, i)][(j, i - 1)] = [random.randint(1, 20), round(
                            math.sqrt(math.pow((i - 9), 2) + math.pow((j - 9), 2)), 2)]

    # Getters for width and height of environment
    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    """
    Checks if the Agent(through the passed x and y values) is currently in bounds
    @:param x the x value of the agent
    @:param y the y value of the agent
    """
    def inBounds(self, x, y):
        if (0 <= x <= self.getWidth() - 1) & (0 <= y <= self.getHeight() - 1):
            return True
        else:
            return False

    def makeWalls(self):
        # Range can be changed to produce more or less walls
        for k in range(0, 7):
            # This loop is manually broken within when a wall is made in the grid
            while 1:
                # Goes to a random (x,y)
                randX = random.randint(0, 9)
                randY = random.randint(0, 9)
                # Will not place a wall at (0,0) <-- start or (9,9) <-- End
                if not ((randX == 0 and randY == 0) or (randX == 9 and randY == 9)):
                    # 1 represents a wall in the grid
                    if self.grid[randX][randY][2] == 0:
                        self.grid[randX][randY][2] = 1
                        break
        # Iterate through every slot in grid
        for row in self.grid:
            for col in row:
                # Stop everywhere there is a wall
                if col[2] == 1:
                    # Remove the wall node from the graph and from its neighbors connections
                    for g in self.graph:
                        self.graph[g].pop((col[0], col[1]), 0)
                    self.graph.pop((col[0], col[1]))

    """prints environment"""
    def printEnviro(self):
        for i in range(len(self.grid)):
            print(self.grid[i])
        [print(key, ':', value) for key, value in self.graph.items()]
