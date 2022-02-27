"""
Christian Johansson & Michael Norton
Artificial Intelligence, Homework 4
3/1/2022
Professor Silveyra
This file main, has DFS and BFS methods
"""

import Environment
import Agent

"""
Main method contains the loop supporting Main menu, also handles result printing.
"""
def main():

    mainEnviro = Environment


"""
Preforms a depth first search algorithm on adjacency(graph) list from a given starting point.
@param graph The graph/adjacency list that is to be iterated through in the DFS search.
@param startingPoint The vertex/node in the graph/adjacency list from which the search will start from.
@return A string containing the vertices/nodes as integer indexes, separated by "," and "|" for disconnected vertex/node.
"""
def dfs(graph, startingPoint):
    # The stack acts as the primary data structure in DFS
    stack = list()
    start = startingPoint
    # Visited is a list composed of boolean falses top be turned true when
    # their corresponding index in the graph/adjacency list is visited
    visited = [False for i in range(len(graph))]
    # Total number of uniquely visited nodes/vertices
    numVisited = 0
    # String that will contain the DFS print out to be returned
    dfsPrint = ""
    stack.append(start)
    # When the number visited is the length of all possible nodes/vertices
    # there is no more to be found
    while numVisited < len(visited):
        # Special case to find detached node/vertex, this is done when a stack
        # is empty but not all visited are true
        if len(stack) == 0:
            for i in range(len(visited)):
                if not visited[i]:
                    stack.append(i)
                    dfsPrint += "|"
                    break
        popped = int(stack.pop())
        if not visited[popped]:
            # Appends all connecting nodes/vertices to the new popped location
            for x in range(len(graph[popped])):
                stack.append(graph[popped][x][0])
            visited[popped] = True
            numVisited += 1
            dfsPrint += str(popped) + ","
    return dfsPrint


"""
Preforms a breadth first search algorithm on adjacency(graph) list from a given starting point.
@param graph The graph/adjacency list that is to be iterated through in the BFS search.
@param startingPoint The vertex/node in the graph/adjacency list from which the search will start from.
@return A string containing the vertices/nodes as integer indexes, separated by "," and "|" for disconnected vertex/node.
"""
def bfs(graph, startingPoint):
    # The queue acts as the primary data structure in BFS
    queue = list()
    start = startingPoint
    # Visited is a list composed of boolean falses top be turned true when
    # their corresponding index in the graph/adjacency list is visited
    visited = [False for i in range(len(graph))]
    # Total number of uniquely visited nodes/vertices
    numVisited = 0
    # String that will contain the BFS print out to be returned
    bfsPrint = ""
    queue.append(start)
    # When the number visited is the length of all possible nodes/vertices
    # there is no more to be found
    while numVisited < len(visited):
        # Special case to find detached node/vertex, this is done when a queue
        # is empty but not all visited are true
        if len(queue) == 0:
            for i in range(len(visited)):
                if not visited[i]:
                    queue.append(i)
                    bfsPrint += "|"
                    break
        popped = int(queue.pop(0))
        if not visited[popped]:
            # Appends all connecting nodes/vertices to the new popped location
            for x in range(len(graph[popped])):
                queue.append(graph[popped][x][0])
            visited[popped] = True
            numVisited += 1
            bfsPrint += str(popped) + ","
    return bfsPrint


main()
