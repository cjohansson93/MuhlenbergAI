"""
Christian Johansson & Michael Norton
Artificial Intelligence, Homework 4
3/1/2022
Professor Silveyra
This file is the agent, capable of moving both up/down/left/right
"""

import random


class Agent:

    """
    Constructor for the cleaning agent
    @param enviro The passed in environment the agent will exist within.
    @param locationX The x-coordinate of the position of the agent in the environment
    @param locationY The y-coordinate of the position of the agent in the environment
    """
    def __init__(self, enviro, locationX=0, locationY=0):
        self.environment = enviro
        self.locationX = locationX
        self.locationY = locationY

    """
    Changes the agents position by one in bounds of grid left/right/up/down.
    """
    def moveLocation(self, direct):
        # Produces random int between 1-4
        direction = random.randint(1, 4)
        # Right movement
        if direction == 1:
            # Checks if the potential new location is with bounds
            if self.environment.inBounds(self.locationX + 1, self.locationY):
                self.locationX += 1
        # Left movement
        elif direction == 2:
            # Checks if the potential new location is with bounds
            if self.environment.inBounds(self.locationX - 1, self.locationY):
                self.locationX -= 1
        # Up movement
        elif direction == 3:
            # Checks if the potential new location is with bounds
            if self.environment.inBounds(self.locationX, self.locationY + 1):
                self.locationY += 1
        # Down movement
        elif direction == 4:
            # Checks if the potential new location is with bounds
            if self.environment.inBounds(self.locationX, self.locationY - 1):
                self.locationY -= 1

    def printLocation(self):
        print("(" + str(self.locationX) + ", " + str(self.locationY) + ")")
