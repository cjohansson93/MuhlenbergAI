"""
Christian Johansson & Michael Norton
Artificial Intelligence, Homework 4
3/1/2022
Professor Silveyra
This file main, has DFS and BFS methods
"""


"""
Main method contains the loop supporting Main menu, also handles result printing.
"""
def main():
    graph = dict()

    # # Reading in of text lines from file and splitting
    # f = open("graphValues.txt")
    # val = f.readline()
    # line1 = val.split()
    # nodes = int(line1[0])
    # edges = int(line1[1])
    #
    # # Create separate list container for each node
    # for i in range(nodes):
    #     graph[i] = list()
    #
    # # Populating each graph node with its connection and weight
    # for i in range(edges):
    #     temp = f.readline().split()
    #     origin = int(temp[0])
    #     destination = int(temp[1])
    #     weight = int(temp[2])
    #     graph[origin].append((destination, weight))

#     # Boolean controlled loop menu for graph manipulation
#     loop = True
#     while loop:
#         mainMenuOptions()
#         choice = input("Enter selection number: ")
#
#         # 1. Vertices connected to [x]
#         if choice == "1":
#             vertex = input("Please enter a vertex: ")
#             # Checking to see if vertex exists in graph
#             if graph.get(int(vertex)) is None:
#                 print("Error! " + vertex + " is an invalid vertex!")
#             # If the vertex exists, print the vertex connections
#             else:
#                 print(vertex + ": " + str(graph.get(int(vertex))))
#         # 2. Print Graph using list comprehension
#         elif choice == "2":
#             [print(key, ':', value) for key, value in graph.items()]
#         # 3. Add connection
#         elif choice == "3":
#             origin = input("Enter origin vertex: ")
#             # Checking to see if vertex exists in graph
#             if graph.get(int(origin)) is None:
#                 print("Error! " + origin + " is an invalid vertex!")
#             else:
#                 destination = input("Enter destination vertex: ")
#                 # Checking to see if destination exists in graph
#                 # as edge is presumed to only be formed between existing vertices
#                 if graph.get(int(destination)) is None:
#                     print("Error! " + destination + " is an invalid destination!")
#                 else:
#                     weight = input("Enter weight of connection: ")
#                     # Checks to see if weight is numerical, if it is a new connections
#                     # is added to the graph between origin & destination with weight
#                     if weight.isdigit():
#                         graph[int(origin)].append((int(destination), int(weight)))
#                     else:
#                         print("Error! Non-numeric weight!")
#         # 4. Store to file
#         elif choice == "4":
#             # Makes new file if given name doesn't exist or can overwrite file
#             newFile = open((input("Enter a new file name: ") + ".txt"), "w")
#             numConnections = 0
#             # Gather number of connection in graph
#             for x in range(len(graph)):
#                 numConnections += len(graph[x])
#             # Adds a line to the file with the number of vertices and connections
#             newFile.write(str(len(graph)) + " " + str(numConnections) + "\n")
#             # Adds a line(s) to the file with the origin, destination and weight
#             for x in range(len(graph)):
#                 for j in range(len(graph[x])):
#                     newFile.write(str(x) + " " + str(graph[x][j][0]) + " " + str(graph[x][j][1]) + "\n")
#         # 5. BFS
#         elif choice == "5":
#             # Getting starting vertex to pass to BFS method
#             start = input("Enter the starting vertex: ")
#             # Checking to see if vertex exists in graph
#             if graph.get(int(start)) is None:
#                 print("Error! " + start + " is an invalid vertex!")
#             else:
#                 print("BFS: " + bfs(graph, start))
#         # 6. DFS
#         elif choice == "6":
#             # Getting starting vertex to pass to DFS method
#             start = input("Enter the starting vertex: ")
#             # Checking to see if vertex exists in graph
#             if graph.get(int(start)) is None:
#                 print("Error! " + start + " is an invalid vertex!")
#             else:
#                 print("DFS: " + dfs(graph, start))
#         # 7. Exit Program
#         elif choice == "7":
#             loop = False
#         # Catch for any invalid entries to the menu
#         else:
#             print("Invalid selection entry! Try again!")
#
# """
# Contains the print out statements of menu the options.
# """
# def mainMenuOptions():
#     print("----------Main Menu----------")
#     print("1. Vertices connected to [x]")
#     print("2. Print Graph")
#     print("3. Add connection")
#     print("4. Store to file")
#     print("5. BFS")
#     print("6. DFS")
#     print("7. Exit Program")


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
