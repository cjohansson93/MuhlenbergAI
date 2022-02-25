"""
Christian Johansson & Michael Norton
Artificial Intelligence, Homework 4
3/1/2022
Professor Silveyra
This file contains the environment for the agent
"""

import random
import math


class Environment:
    """
    Constructor
    Initializes a grid of lists with an X value, Y value, cost and heuristic
    @:param width of the environment
    @:param height of the environment
    @:param grid representation of the environment
    """
    def __init__(self, width=10, height=10):
        self.width = width
        self.height = height
        self.graph = dict()
        self.grid = [[[] for i in range(height)] for j in range(width)]
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                self.grid[i][j].append(j)  # Adds x value
                self.grid[i][j].append(i)  # Adds y value
                self.grid[i][j].append(0)  # 1 = is a wall, 0 = not a wall
        for k in range(0, 7):
            while 1:
                randX = random.randint(0, 9)
                randY = random.randint(0, 9)
                if not ((randX == 0 and randY == 0) or (randX == 9 and randY == 9)):
                    if self.grid[randX][randY][2] == 0:
                        self.grid[randX][randY][2] = 1
                        break
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if not self.grid[j][i][2] == 1:
                    self.graph[(j, i)] = dict()
                    if not ((j + 1) == 10):
                        if (j+1, i) in self.graph:
                            self.graph[(j, i)][(j+1, i)] = self.graph[(j+1, i)][(j, i)]
                        else:
                            self.graph[(j, i)][(j + 1, i)] = [random.randint(1, 20), round(
                                math.sqrt(math.pow((i-9), 2) + math.pow((j-9), 2)), 2)]
                    if not ((j - 1) == -1):
                        if (j - 1, i) in self.graph:
                            self.graph[(j, i)][(j - 1, i)] = self.graph[(j - 1, i)][(j, i)]
                        else:
                            self.graph[(j, i)][(j - 1, i)] = [random.randint(1, 20), round(
                                math.sqrt(math.pow((i - 9), 2) + math.pow((j - 9), 2)), 2)]
                    if not ((i + 1) == 10):
                        if (j, i+1) in self.graph:
                            self.graph[(j, i)][(j, i+1)] = self.graph[(j, i+1)][(j, i)]
                        else:
                            self.graph[(j, i)][(j, i+1)] = [random.randint(1, 20), round(
                                math.sqrt(math.pow((i - 9), 2) + math.pow((j - 9), 2)), 2)]
                    if not ((i - 1) == -1):
                        if (j, i - 1) in self.graph:
                            self.graph[(j, i)][(j, i - 1)] = self.graph[(j, i - 1)][(j, i)]
                        else:
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

    # """
    # Checks if the position of the Agent (through the passed x and y values)
    # @param x the x value of the agent
    # @param y the y value of the agent
    # """
    # def isDirty(self, x, y):
    #     if self.grid[x][y][2] == 1:
    #         return True
    #     else:
    #         return False

    # prints environment
    def printEnviro(self):
        for i in range(len(self.grid)):
            print(self.grid[i])
        [print(key, ':', value) for key, value in self.graph.items()]

    # def numDirty(self):
    #     self.count = 0
    #     for i in range(len(self.grid)):
    #         for j in range(len(self.grid[i])):
    #             if self.grid[i][j][2] == 1:
    #                 self.count += 1
    #     return self.count


t = Environment()
t.printEnviro()
