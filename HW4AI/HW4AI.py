"""
Christian Johansson & Michael Norton
Artificial Intelligence, Homework 4
3/1/2022
Professor Silveyra
This file main, has DFS and BFS methods
"""

import Environment
import Agent
import copy
import heapq

"""
Main method contains the loop supporting Main menu, also handles result printing.
"""
def main():

    mainEnviro = Environment.Environment()

    # BFS
    numSolutions = 0
    numSteps = 0
    for test in range(100):
        bfsEnviro = copy.deepcopy(mainEnviro)
        bfsEnviro.makeWalls()
        bfsAgent = Agent.Agent(bfsEnviro)
        stepsANDsolution = bfs(bfsAgent, (0, 0))
        numSteps += int(stepsANDsolution[0])
        numSolutions += int(stepsANDsolution[1])

    print("BFS")
    print("Times exit found: " + str(numSolutions) + "\nThe average unique nodes visited: " + str(round(numSteps/ numSolutions)) + "\n")

    # DFS
    numSolutions = 0
    numSteps = 0
    for test in range(100):
        dfsEnviro = copy.deepcopy(mainEnviro)
        dfsEnviro.makeWalls()
        dfsAgent = Agent.Agent(dfsEnviro)
        stepsANDsolution = dfs(dfsAgent, (0, 0))
        numSteps += int(stepsANDsolution[0])
        numSolutions += int(stepsANDsolution[1])

    print("DFS")
    print("Times exit found: " + str(numSolutions) + "\nThe average steps: " + str(round(numSteps / numSolutions)) + "\n")

    # A*
    numSolutions = 0
    numSteps = 0
    for test in range(100):
        aStarEnviro = copy.deepcopy(mainEnviro)
        aStarEnviro.makeWalls()
        aStarAgent = Agent.Agent(aStarEnviro)
        stepsANDsolution = aStar(aStarAgent, (0, 0))
        numSteps += int(stepsANDsolution[0])
        numSolutions += int(stepsANDsolution[1])

    print("A*")
    print("Times exit found: " + str(numSolutions) + "\nThe average unique nodes visited: " + str(round(numSteps/numSolutions)) + "\n" + str(stepsANDsolution[2]) + "\n")

    # A*
    numSolutions = 0
    numSteps = 0
    for test in range(100):
        greedyEnviro = copy.deepcopy(mainEnviro)
        greedyEnviro.makeWalls()
        greedyAgent = Agent.Agent(greedyEnviro)
        stepsANDsolution = greedy(greedyAgent, (0, 0))
        numSteps += int(stepsANDsolution[0])
        numSolutions += int(stepsANDsolution[1])

    print("Greedy")
    print("Times exit found: " + str(numSolutions) + "\nThe average unique nodes visited: " + str(round(numSteps/numSolutions)) + "\n" + str(stepsANDsolution[2]) + "\n")


"""
Preforms a depth first search algorithm on adjacency(graph) list from a given starting point.
@param agent The agent containing the graph/adjacency list that is to be iterated through in the DFS search.
@param startingPoint The vertex/node in the graph/adjacency list from which the search will start from.
@return A tuple: (Number of steps taken to reach end/ 0 if no end found, 1 for end reached/ 0 if no end found)
"""
def dfs(agent, startingPoint):
    # The stack acts as the primary data structure in DFS
    dfsAgent = agent
    dfsEnviro = dfsAgent.environment.graph
    stack = list()
    start = startingPoint
    # Visited is a list composed of boolean falses top be turned true when
    # their corresponding index in the graph/adjacency list is visited
    # Total number of uniquely visited nodes/vertices
    numVisited = 0
    visitedNodes = list()
    path = list()
    steps = 0
    stack.append(start)
    # When the number visited is the length of all possible nodes/vertices
    # there is no more to be found and
    while numVisited < len(dfsEnviro):
        # If the exit is a disconnected node/graph, there is no path and no solution
        if len(stack) == 0 and (9, 9) not in visitedNodes:
            return 0, 0
        popped = stack.pop()
        if popped not in visitedNodes:
            visitedNodes.append(popped)
            if len(path) > 0:
                while True:
                    previous = path.pop()
                    if popped in dfsEnviro[previous]:
                        path.append(previous)
                        path.append(popped)
                        steps += 1
                        break
                    else:
                        steps += 1
            else:
                path.append(popped)
            # Appends all connecting nodes/vertices to the new popped location
            for node in dfsEnviro[popped]:
                if node == (9, 9):
                    return steps+1, 1
                stack.append(node)
            numVisited += 1
    return 0, 0


"""
Preforms a breadth first search algorithm on adjacency(graph) list from a given starting point.
@param agent The agent containing the graph/adjacency list that is to be iterated through in the BFS search.
@param startingPoint The vertex/node in the graph/adjacency list from which the search will start from.
@return (Number of steps taken to reach end/ 0 if no end found, 1 for end reached/ 0 if no end found)
"""
def bfs(agent, startingPoint):
    # The queue acts as the primary data structure in BFS
    bfsAgent = agent
    bfsEnviro = bfsAgent.environment.graph
    queue = list()
    start = startingPoint
    # Total number of uniquely visited nodes/vertices
    numVisited = 0
    visitedNodes = list()
    queue.append(start)
    # When the number visited is the length of all possible nodes/vertices
    # there is no more to be found and
    while numVisited < len(bfsEnviro):
        # If the exit is a disconnected node/graph, there is no path and no solution
        if len(queue) == 0 and (9, 9) not in visitedNodes:
            return 0, 0
        popped = queue.pop(0)
        if popped not in visitedNodes:
            visitedNodes.append(popped)
            # Appends all connecting nodes/vertices to the new popped location
            for node in bfsEnviro[popped]:
                if node == (9, 9):
                    return numVisited, 1
                queue.append(node)
            numVisited += 1
    return 0, 0


"""
Preforms an A* search algorithm on adjacency(graph) list from a given starting point.
@param agent The agent containing the graph/adjacency list that is to be iterated through in the A* search.
@param startingPoint The vertex/node in the graph/adjacency list from which the search will start from.
@return (Number of steps taken to reach end/ 0 if no end found, 1 for end reached/ 0 if no end found)
"""
def aStar(agent, startingPoint):
    # The queue acts as the primary data structure in A*
    aStarAgent = agent
    aStarEnviro = aStarAgent.environment.graph
    priorityQueue = list()
    visitedNodes = list()
    start = startingPoint
    numVisited = 0
    if len(aStarEnviro.get(start)) == 0:
        return 0, 0, 0
    else:
        heapq.heappush(priorityQueue, (0 + [aStarEnviro[[key for key in aStarEnviro[start]][0]].get(start)][0][1], (start, 0)))
    while numVisited < len(aStarEnviro):
        # If the exit is a disconnected node/graph, there is no path and no solution
        if len(priorityQueue) == 0 and (9, 9) not in visitedNodes:
            return 0, 0, 0
        smallestValue = heapq.heappop(priorityQueue)
        if smallestValue[1][0] not in visitedNodes:
            visitedNodes.append(smallestValue[1][0])
            numVisited += 1
            for node in aStarEnviro[smallestValue[1][0]]:
                if node == (9, 9):
                    return numVisited, 1, visitedNodes
                cost = smallestValue[1][1] + [aStarEnviro[smallestValue[1][0]].get(node)][0][0]
                value = cost + [aStarEnviro[smallestValue[1][0]].get(node)][0][1]
                heapq.heappush(priorityQueue, (value, (node, cost)))

    return 0, 0, 0


def greedy(agent, startingPoint):
    greedyAgent = agent
    greedyEnviro = greedyAgent.environment.graph
    heap = list()
    visited = list()
    start = startingPoint
    numVisited = 0

    if len(greedyEnviro.get(start)) == 0:
        return 0, 0, 0
    else:
        heapq.heappush(heap, ([greedyEnviro[[key for key in greedyEnviro[start]][0]].get(start)][0][1], start))
    while numVisited < len(greedyEnviro):
        if len(heap) == 0 and (9, 9) not in visited:
            return 0, 0, 0
        smallestValue = heapq.heappop(heap)
        if smallestValue[1] not in visited:
            visited.append(smallestValue[1])
            numVisited += 1
            for node in greedyEnviro[smallestValue[1]]:
                if node == (9, 9):
                    return numVisited, 1, visited
                heuristic = [greedyEnviro[smallestValue[1]].get(node)][0][1]
                heapq.heappush(heap, (heuristic, node))
    return 0, 0, 0


main()
