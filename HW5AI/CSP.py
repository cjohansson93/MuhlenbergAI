import AdjacencyMatrix


NumColors = 3


class CSP:

	def __init__(self, mostConstrained=False, mostConstraining=False,
				 forwardChecking=False, leastConstraining=False):
		self.mostConstrained = mostConstrained
		self.mostConstraining = mostConstraining
		self.forwardChecking = forwardChecking
		self.leastConstraining = leastConstraining
		self.adjacency = AdjacencyMatrix.AdjacencyMatrix()
		self.recursionCounter = 0
		solveCSP(self.adjacency.matrix, self.mostConstrained, self.mostConstraining,
				 self.forwardChecking, self.leastConstraining)


def isSafeColor(matrix, currentNode, color):
	for connected in matrix[currentNode][2]:
		if color == matrix[connected][0]:
			return False
	return True


def backtracking(matrix, currentNode, counter, mostConstrained,
				 mostConstraining, forwardChecking, leastConstraining):
	innerCounter = counter
	print(innerCounter)
	if currentNode >= len(matrix):
		return True,innerCounter

	visited = list()
	if currentNode not in visited:
		visited.append(currentNode)
		for connection in matrix[currentNode][2]:
			for color in range(NumColors):

				if isSafeColor(matrix, currentNode, color+1):
					matrix[currentNode][0] = color+1
					recursiveResult = backtracking(matrix, connection, counter+1)
					innerCounter = recursiveResult[1]
					if recursiveResult[0]:
						return True,innerCounter
					matrix[currentNode][0] = 0

			return False,innerCounter


def solveCSP(matrix, mostConstrained, mostConstraining,
				 forwardChecking, leastConstraining):
	start = 0
	new = True
	if mostConstraining:
		start = mostConstrainingVariable(matrix, new)
	result = backtracking(matrix, start, 0, mostConstrained, mostConstraining,
				 forwardChecking, leastConstraining)
	if not result[0]:
		print("Solution does not exist")
	else:
		print("***** Solution found after "+str(result[1])+" recursions *****")
		print(matrix, sep="\n")


def mostConstrainingVariable(matrix, new):
	if new:
		mostConnects = [0,0]
		for i in range(len(matrix)):
			if len(matrix[i][2]) > mostConnects[1]:
				mostConnects = [len(matrix[i][2]), i]
		return mostConnects[1]
