"""
Christian Johansson
Artificial Intelligence, Homework 5
4/1/2022
Professor Silveyra
This file solves the constraint satisfaction coloring problem. In this problem connected nodes in a passed adjacency
list are assigned a number 1-3, in which no connected node can have the same number as itself. The base solution is
obtained through backtracking recursion. 3 upgrades to this base algorithm can be activated independently of each
other in the constructor. These improve performance.
"""
import AdjacencyMatrix

# Number of colors as 1-3, adjustable
NumColors = 3


class CSP:

	"""
	Constructor for constraint satisfaction coloring problem, with boolean controlled upgrades and recursion counter.
	@param mostConstrained Boolean to turn on Most Constrained Variable upgrade to the backtracking algorithm
	@param mostConstraining Boolean to turn on Most Constraining Variable upgrade to the backtracking algorithm
	@param leastConstraining Boolean to turn on Least Constrained Value upgrade to the backtracking algorithm
	"""
	def __init__(self, mostConstrained=False, mostConstraining=False, leastConstraining=False):
		self.mostConstrained = mostConstrained
		self.mostConstraining = mostConstraining
		self.leastConstraining = leastConstraining
		self.adjacency = AdjacencyMatrix.AdjacencyMatrix(3, 50)
		self.recursionCounter = 0

	"""
	Method for determining if given color would match with directly connected node's color.
	@param currentNode The current node in the adjacency list.
	@param color An integer 1-3 representing a color to be tested at a given node
	@return False is color is already taken by connection, true if available
	"""
	def isSafeColor(self, currentNode, color):
		# Iterate through all connected nodes and check color
		for connected in self.adjacency.Alist[currentNode][2]:
			if color == self.adjacency.Alist[connected][0]:
				return False
		return True

	"""
	Method for solving coloring problem using backtracking recursively with conditional
	callouts for upgrades to produce fewer recursion.
	@param currentNode The current node in the adjacency list.
	@return False to backtrack, True if solved
	"""
	def backtracking(self, currentNode):
		# Counts how many recursions take place per solve
		self.recursionCounter += 1
		# Since some solutions require terrifying amounts of time, they are treated
		# like failures at 1 million recursions, to not get stuck
		if self.recursionCounter > 1000000:
			return False

		# If everything is filled with color the problem is solved
		finished = True
		for n in self.adjacency.Alist:
			if n[0] == 0:
				finished = False
		if finished:
			return True

		# Colors are typically tried 1 to 3, but if
		# least constraining value is True, it will pick the color
		colors = range(1, NumColors+1)
		if self.leastConstraining:
			colors = [self.leastConstrainingValue(currentNode)]

		# Iterate through color(s)
		for color in colors:
			# See if color is a legal options before assigning it
			if self.isSafeColor(currentNode, color):
				self.adjacency.Alist[currentNode][0] = color

				# Statements for the multitude of combinations that the
				# upgrades can be toggled on
				if self.mostConstrained:
					mostConstrainedList = self.mostConstrainedVarible()
					if mostConstrainedList:
						nextNode = mostConstrainedList[0]
						if self.mostConstraining:
							for n in mostConstrainedList:
								if len(self.adjacency.Alist[n][2]) > len(self.adjacency.Alist[nextNode][2]):
									nextNode = n
					else:
						return True
				elif self.mostConstraining:
					mostConstrainingList = self.mostConstrainingVariable()
					if mostConstrainingList:
						nextNode = mostConstrainingList[0]
					else:
						return True
				else:
					# Standard backtracking goes to next node in list
					nextNode = currentNode + 1
				# If a solution is found a cascade of Trues will exit backtracking
				if self.backtracking(nextNode):
					return True
				# If backtracking the color is reset
				self.adjacency.Alist[currentNode][0] = 0
		return False

	"""
	Method to call starting algorithm method and relay result of solution or lack of back to tester.
	@return A 0 for the amount of recursion in an unsuccessful solution, or number of recursions if successful.
	"""
	def solveCSP(self):
		# Starting node index
		start = 0
		# Starts with the most well-connected node if true
		if self.mostConstraining:
			start = self.mostConstrainingVariable()[0]
		# Stores boolean for success in solving CSP
		result = self.backtracking(start)
		if not result:
			#print("Solution does not exist")
			return 0
		else:
			#print("***** Solution found after "+str(self.recursionCounter)+" recursions *****")
			return self.recursionCounter

	"""
	Method upgrade to the backtracking algorithm by finding the most well-connected
	node in a list or adjacency-list, as part of a smarting coloring method.
	@return A list of the indexes of the most connected nodes.
	"""
	def mostConstrainingVariable(self):
		# Starting point for connection quantity comparison
		mostConnections = 0
		# list to hold the indexes of the most connections
		mostConstrainingList = list()
		# Iterate through whole list, only caring about uncolored
		for i in range(len(self.adjacency.Alist)):
			if self.adjacency.Alist[i][0] == 0:
				# Check length of every node's connections list
				j = len(self.adjacency.Alist[i][2])
				if j > mostConnections:
					# List starts over if a new high is found
					mostConstrainingList = list()
					mostConstrainingList.append(i)
					mostConnections = j
				# Multiple can be added to list if they have the same number
				elif j == mostConnections:
					mostConstrainingList.append(i)
		return mostConstrainingList

	"""
	Method upgrade to the backtracking algorithm by finding the node in a list or adjacency-list
	with the fewest legal colors left, as part of a smarting coloring method.
	@return A list of the indexes of the nodes with the fewest options left
	"""
	def mostConstrainedVarible(self):
		# An unobtainable level of colors available
		# and list to store lowest(s)
		levelOfConstraint = NumColors+1
		constrainedList = list()
		# Iterate through whole list, only caring about uncolored
		for i in range(len(self.adjacency.Alist)):
			if self.adjacency.Alist[i][0] == 0:
				colorsAvailable = [0, 1, 1, 1]
				# If a connection already has a color, that color's index is removed
				# from the possibility of the uncolored it is connected to
				for c in self.adjacency.Alist[i][2]:
					colorsAvailable[self.adjacency.Alist[c][0]] = 0
				# count how many colors remain for each connection
				count = 0
				for j in colorsAvailable:
					count += j
				# List starts over if a new low is found
				if count < levelOfConstraint:
					constrainedList = list()
					constrainedList.append(i)
					levelOfConstraint = count
				# Multiple can be added to list if they have the same number
				elif count == levelOfConstraint:
					constrainedList.append(i)
		return constrainedList

	"""
	Method upgrade to the backtracking algorithm by finding the color that restricts the
	connected node's potential colors the least, as part of a smarting coloring method.
	@param node The current node in the adjacency list to be colored.
	@return A list of the indexes of the nodes with the fewest options left
	"""
	def leastConstrainingValue(self, node):
		# Start with unobtainable high constraint [4,4,4]
		leastConstrainingColor = [NumColors+1] * 3
		# For each color make sure that you can legally have it
		for color in range (1, NumColors+1):
			if self.isSafeColor(node, color):
				# For a safe color remove that from connections options
				# only caring about uncolored connections
				for neighbor in self.adjacency.Alist[node][2]:
					if self.adjacency.Alist[neighbor][0] == 0:
						colorRange = [c for c in range(1, NumColors+1)]
						colorRange.remove(color)
						counter = 0
						# Make sure remaining colors for connections are
						# even legal, then count them
						for neighborcolor in colorRange:
							if self.isSafeColor(neighbor, neighborcolor):
								counter += 1
						# We want the smallest in each set
						if counter < leastConstrainingColor[color-1]:
							leastConstrainingColor[color-1] = counter
			else:
				leastConstrainingColor[color-1] = 0

		# The largest smallest number of legal colors, corresponds to right color
		i = 0
		for c in range(len(leastConstrainingColor)):
			if leastConstrainingColor[i] < leastConstrainingColor[c]:
				i = c

		return i + 1
