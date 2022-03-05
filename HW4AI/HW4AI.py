"""
Christian Johansson & Michael Norton
Artificial Intelligence, Homework 4
3/4/2022
Professor Silveyra
This file contains methods for preforming a BFS, DFS, Greedy best search and an A* search on a graph.
It also includes a main for testing the different searches on an agent in an environment. This gives the number
of successful searches out of 100 and the average steps in total successful searches and a sample of the total
path of the last search of the 100. DFS steps counts realistic backtracking steps as well.
"""

import Environment
import Agent
import copy
import heapq

"""
Main method contains the test for preforming a BFS, DFS, Greedy best search and an A* search on a graph.
This gives the number of successful searches out of 100 and the average steps in total successful searches 
and a sample of the total path of the last search of the 100. DFS steps counts realistic backtracking steps as well.
"""
def main():

    # Environment object of which all copy are made from to preserve costs
    mainEnviro = Environment.Environment()

    print("\n----Testing Search Algorithms----\n")

    # BFS
    numSolutions = 0
    numSteps = 0
    # Here the number of test runs can be changed in the range
    for test in range(100):
        # A copy of the main environment is made to preserve costs
        # but walls are randomized for each test, start & end can be block in
        bfsEnviro = copy.deepcopy(mainEnviro)
        bfsEnviro.makeWalls()
        bfsAgent = Agent.Agent(bfsEnviro)
        # a length 3 list is returned with (steps of that run)
        # , (1 for solved/ 0 if unsolved)
        # , (list of visited nodes/ 0 if unsolved)
        stepsANDsolution = bfs(bfsAgent, (0, 0))
        numSteps += int(stepsANDsolution[0])
        numSolutions += int(stepsANDsolution[1])

    print("BFS")
    print("Times exit found: " + str(numSolutions) + "\nThe average unique nodes visited: " + str(round(numSteps/ numSolutions)) + "\nTotal Path: " + str(stepsANDsolution[2]) + "\n")

    # DFS
    numSolutions = 0
    numSteps = 0
    # Here the number of test runs can be changed in the range
    for test in range(100):
        # A copy of the main environment is made to preserve costs
        # but walls are randomized for each test, start & end can be block in
        dfsEnviro = copy.deepcopy(mainEnviro)
        dfsEnviro.makeWalls()
        dfsAgent = Agent.Agent(dfsEnviro)
        # a length 3 list is returned with (realistic steps, like backtracking steps, of that run)
        # , (1 for solved/ 0 if unsolved)
        # , (list of visited nodes/ 0 if unsolved)
        stepsANDsolution = dfs(dfsAgent, (0, 0))
        numSteps += int(stepsANDsolution[0])
        numSolutions += int(stepsANDsolution[1])

    print("DFS")
    print("Times exit found: " + str(numSolutions) + "\nThe average steps: " + str(round(numSteps / numSolutions)) + "\nTotal Path: " + str(stepsANDsolution[2]) + "\n")

    # A*
    numSolutions = 0
    numSteps = 0
    # Here the number of test runs can be changed in the range
    for test in range(100):
        # A copy of the main environment is made to preserve costs
        # but walls are randomized for each test, start & end can be block in
        aStarEnviro = copy.deepcopy(mainEnviro)
        aStarEnviro.makeWalls()
        aStarAgent = Agent.Agent(aStarEnviro)
        # a length 3 list is returned with (steps of that run)
        # , (1 for solved/ 0 if unsolved)
        # , (list of visited nodes/ 0 if unsolved)
        stepsANDsolution = aStar(aStarAgent, (0, 0))
        numSteps += int(stepsANDsolution[0])
        numSolutions += int(stepsANDsolution[1])

    print("A*")
    print("Times exit found: " + str(numSolutions) + "\nThe average unique nodes visited: " + str(round(numSteps/numSolutions)) + "\nTotal Path: " + str(stepsANDsolution[2]) + "\n")

    # Greedy
    numSolutions = 0
    numSteps = 0
    # Here the number of test runs can be changed in the range
    for test in range(100):
        # A copy of the main environment is made to preserve costs
        # but walls are randomized for each test, start & end can be block in
        greedyEnviro = copy.deepcopy(mainEnviro)
        greedyEnviro.makeWalls()
        greedyAgent = Agent.Agent(greedyEnviro)
        # a length 3 list is returned with (steps of that run)
        # , (1 for solved/ 0 if unsolved)
        # , (list of visited nodes/ 0 if unsolved)
        stepsANDsolution = greedy(greedyAgent, (0, 0))
        numSteps += int(stepsANDsolution[0])
        numSolutions += int(stepsANDsolution[1])

    print("Greedy")
    print("Times exit found: " + str(numSolutions) + "\nThe average unique nodes visited: " + str(round(numSteps/numSolutions)) + "\nPath: " + str(stepsANDsolution[2]) + "\n")

    print("----------End of Tests----------")


"""
Preforms a depth first search algorithm on adjacency(graph) list from a given starting point.
@param agent The agent containing the graph/adjacency list that is to be iterated through in the DFS search.
@param startingPoint The vertex/node in the graph/adjacency list from which the search will start from.
@return A tuple: (Number of realistic steps taken to reach end/ 0 if no end found, 1 for end reached/ 0 if no end found, path/ 0 if no end found)
"""
def dfs(agent, startingPoint):
    dfsAgent = agent
    dfsEnviro = dfsAgent.environment.graph
    # The stack acts as the primary data structure in DFS
    stack = list()
    start = startingPoint
    # Total number of uniquely visited nodes/vertices
    numVisited = 0
    # A list of those uniquely visited node/vertices, used as path
    visitedNodes = list()
    # Used to determine steps to backtrack
    path = list()
    steps = 0
    stack.append(start)
    # When the number visited is the length of all possible nodes/vertices
    # there is no more to be found and no solution is made
    while numVisited < len(dfsEnviro):
        # If the exit is a disconnected node/graph, there is no path and no solution
        if len(stack) == 0 and (9, 9) not in visitedNodes:
            return 0, 0, 0
        popped = stack.pop()
        # if the node hasn't been visited
        if popped not in visitedNodes:
            # Add node to visited
            visitedNodes.append(popped)
            # This statement is for adding backtracking steps
            # If a popped node cannot be reached by the previous
            # steps is incremented until something in the previous
            # list is connected to that new node
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
                # If it's connected to the end it is solved
                if node == (9, 9):
                    return steps+1, 1, visitedNodes
            # If solutions isn't found yet its nodes are added to stack and increment number visited
                stack.append(node)
            numVisited += 1
    return 0, 0, 0


"""
Preforms a breadth first search algorithm on adjacency(graph) list from a given starting point.
@param agent The agent containing the graph/adjacency list that is to be iterated through in the BFS search.
@param startingPoint The vertex/node in the graph/adjacency list from which the search will start from.
@return (Number of steps taken to reach end/ 0 if no end found, 1 for end reached/ 0 if no end found, path/ 0 if no end found)
"""
def bfs(agent, startingPoint):
    bfsAgent = agent
    bfsEnviro = bfsAgent.environment.graph
    # The queue acts as the primary data structure in BFS
    queue = list()
    start = startingPoint
    # Total number of uniquely visited nodes/vertices
    numVisited = 0
    # A list of those uniquely visited node/vertices, used as path
    visitedNodes = list()
    queue.append(start)
    # When the number visited is the length of all possible nodes/vertices
    # there is no more to be found and no solution is made
    while numVisited < len(bfsEnviro):
        # If the exit is a disconnected node/graph, there is no path and no solution
        if len(queue) == 0 and (9, 9) not in visitedNodes:
            return 0, 0, 0
        popped = queue.pop(0)
        # if the node hasn't been visited
        if popped not in visitedNodes:
            # Add node to visited
            visitedNodes.append(popped)
            # Appends all connecting nodes/vertices to the new popped location
            for node in bfsEnviro[popped]:
                # If it's connected to the end it is solved
                if node == (9, 9):
                    return numVisited, 1, visitedNodes
            # If solutions isn't found yet its nodes are added to queue and increment number visited
                queue.append(node)
            numVisited += 1
    return 0, 0, 0


"""
Preforms an A* search algorithm on adjacency(graph) list from a given starting point.
@param agent The agent containing the graph/adjacency list that is to be iterated through in the A* search.
@param startingPoint The vertex/node in the graph/adjacency list from which the search will start from.
@return (Number of steps taken to reach end/ 0 if no end found, 1 for end reached/ 0 if no end found, path/ 0 if no end found)
"""
def aStar(agent, startingPoint):
    aStarAgent = agent
    aStarEnviro = aStarAgent.environment.graph
    # The priority queue acts as the primary data structure in A*
    # since as a heap it will autosort by lowest value (cost + heuristic)
    priorityQueue = list()
    # A list of those uniquely visited node/vertices, used as path
    visitedNodes = list()
    start = startingPoint
    # Total number of uniquely visited nodes/vertices
    numVisited = 0
    # If the start is boxed in there is no point in moving forward
    if len(aStarEnviro.get(start)) == 0:
        return 0, 0, 0
    else:
        # The heuristic of getting to (0,0) is not stored in (0,0) but inside the keys it's connected to,
        # so the value is retrieved from there to add it to the heap with is cost of 0
        heapq.heappush(priorityQueue, (0 + [aStarEnviro[[key for key in aStarEnviro[start]][0]].get(start)][0][1], (start, 0)))
    # When the number visited is the length of all possible nodes/vertices
    # there is no more to be found and no solution is made
    while numVisited < len(aStarEnviro):
        # If the exit is a disconnected node/graph, there is no path and no solution
        if len(priorityQueue) == 0 and (9, 9) not in visitedNodes:
            return 0, 0, 0
        # Since the heap is sorted by smallest value, you don't have to search for it, just pop
        smallestValue = heapq.heappop(priorityQueue)
        # if the node hasn't been visited
        if smallestValue[1][0] not in visitedNodes:
            # Add node to visited
            visitedNodes.append(smallestValue[1][0])
            numVisited += 1
            # Appends all connecting nodes/vertices to the new popped location
            for node in aStarEnviro[smallestValue[1][0]]:
                # If it's connected to the end it is solved
                if node == (9, 9):
                    return numVisited, 1, visitedNodes
                # Cost is individual cost plus the cost to get their from parent and so on
                cost = smallestValue[1][1] + [aStarEnviro[smallestValue[1][0]].get(node)][0][0]
                # Value is the heuristic plus total cost
                value = cost + [aStarEnviro[smallestValue[1][0]].get(node)][0][1]
                heapq.heappush(priorityQueue, (value, (node, cost)))

    return 0, 0, 0


"""
Preforms a Greedy best search algorithm on adjacency(graph) list from a given starting point.
@param agent The agent containing the graph/adjacency list that is to be iterated through in the Greedy search.
@param startingPoint The vertex/node in the graph/adjacency list from which the search will start from.
@return (Number of steps taken to reach end/ 0 if no end found, 1 for end reached/ 0 if no end found, path/ 0 if no end found)
"""
def greedy(agent, startingPoint):
    greedyAgent = agent
    greedyEnviro = greedyAgent.environment.graph
    # Acts as the primary data structure in Greed best search
    # since as a min heap it will autosort by lowest value (cost + heuristic)
    heap = list()
    # A list of those uniquely visited node/vertices, used as path
    visited = list()
    start = startingPoint
    # Total number of uniquely visited nodes/vertices
    numVisited = 0

    # If the start is boxed in there is no point in moving forward
    if len(greedyEnviro.get(start)) == 0:
        return 0, 0, 0
    else:
        # The heuristic of getting to (0,0) is not stored in (0,0) but inside the keys it's connected to,
        # so the value is retrieved from there to add it to the heap
        heapq.heappush(heap, ([greedyEnviro[[key for key in greedyEnviro[start]][0]].get(start)][0][1], start))
    # When the number visited is the length of all possible nodes/vertices
    # there is no more to be found and no solution is made
    while numVisited < len(greedyEnviro):
        # If the exit is a disconnected node/graph, there is no path and no solution
        if len(heap) == 0 and (9, 9) not in visited:
            return 0, 0, 0
        # Since the heap is sorted by smallest value, you don't have to search for it, just pop
        smallestValue = heapq.heappop(heap)
        # if the node hasn't been visited
        if smallestValue[1] not in visited:
            # Add node to visited
            visited.append(smallestValue[1])
            numVisited += 1
            # Appends all connecting nodes/vertices to the new popped location
            for node in greedyEnviro[smallestValue[1]]:
                # If it's connected to the end it is solved
                if node == (9, 9):
                    return numVisited, 1, visited
                # The (x,y) of the node is stored with is heuristic value
                heuristic = [greedyEnviro[smallestValue[1]].get(node)][0][1]
                heapq.heappush(heap, (heuristic, node))
    return 0, 0, 0


main()
