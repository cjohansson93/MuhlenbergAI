import AdjacencyMatrix


NumColors = 3


class CSP:

	def __init__(self, mostConstrained=False, mostConstraining=False,
				 forwardChecking=False, leastConstraining=False):
		self.mostConstrained = mostConstrained
		self.mostConstraining = mostConstraining
		self.forwardChecking = forwardChecking
		self.leastConstraining = leastConstraining
		self.adjacency = AdjacencyMatrix.AdjacencyMatrix(3, 50)
		self.recursionCounter = 0

	def isSafeColor(self, currentNode, color):
		for connected in self.adjacency.Alist[currentNode][2]:
			if color == self.adjacency.Alist[connected][0]:
				return False
		return True

	def backtracking(self, currentNode):
		self.recursionCounter += 1
		if self.recursionCounter > 1000000:
			return False
		
		finished = True
		for n in self.adjacency.Alist:
			if n[0] == 0:
				finished = False
		
		if finished:
			return True

		for color in range(1, NumColors+1):
			if self.isSafeColor(currentNode, color):
				nextNode = 0
				if self.mostConstrained:
					if self.mostConstraining:
						nextNode = self.mostConstrainingVariable
						if self.leastConstraining:
							color = self.leastConstrainingValue(nextNode)
							if self.forwardChecking:
								if not self.forwardCheckingValue(color):
									return False
					else:
						nextNode = self.mostConstrainedVarible()[0][1]
						if self.leastConstraining:
							color = self.leastConstrainingValue(nextNode)
							if self.forwardChecking:
								if not self.forwardCheckingValue(color):
									return False
				elif self.mostConstraining:
					nextNode = self.mostConstrainingVariable()
					if self.leastConstraining:
						color = self.leastConstrainingValue(nextNode)
				elif self.leastConstraining:
					color = self.leastConstrainingValue(nextNode)
				elif not self.forwardCheckingValue(color):
					return False
				else:
					nextNode = currentNode + 1

				self.adjacency.Alist[currentNode][0] = color
				if self.backtracking(nextNode):
					return True
				self.adjacency.Alist[currentNode][0] = 0
		return False

	def solveCSP(self):
		start = 0
		new = True
		if self.mostConstraining:
			start = self.mostConstrainingVariable()
		result = self.backtracking(start)
		if not result:
			print("Solution does not exist")
			return 0
		else:
			print("***** Solution found after "+str(self.recursionCounter)+" recursions *****")
			return self.recursionCounter

	def mostConstrainingVariable(self):
		if self.mostConstrained:
			mostConnects = [0, 0]
			for i in self.mostConstrainedVarible():
				if len(self.adjacency.Alist[i[0]][2]) > mostConnects[1]:
					mostConnects = [len(self.adjacency.Alist[i[0]][2]), i[0]]
			return mostConnects[1]
		mostConnects = [0,0]
		for i in range(len(self.adjacency.Alist)):
			if len(self.adjacency.Alist[i][2]) > mostConnects[1]:
				mostConnects = [len(self.adjacency.Alist[i][2]), i]
		return mostConnects[1]

	def mostConstrainedVarible(self):
		constrained = [(1, 4)]
		for i in range(len(self.adjacency.Alist)):
			if self.adjacency.Alist[i][0] == 0:
				colorsAvailable = [0, 1, 1, 1]
				for c in self.adjacency.Alist[i][2]:
					colorsAvailable[self.adjacency.Alist[c][0]] = 0
				count = 0
				for j in colorsAvailable:
					count += j
				if count < constrained[0][1]:
					constrained = list()
					constrained.append((i, count))
				elif count == constrained[0][1]:
					constrained.append((i, count))
		return constrained

	def leastConstrainingValue(self, node):
		nodesConnectedValues = list()
		for connected in self.adjacency.Alist[node][2]:
			if self.adjacency.Alist[connected][0] == 0:
				values = [1, 2, 3]
				for neighbors in self.adjacency.Alist[connected][2]:
					if self.adjacency.Alist[neighbors][0] in values:
						values.remove(self.adjacency.Alist[neighbors][0])
				nodesConnectedValues.append(values)

		allColors = list()
		for color in range(1, 3):
			lowestForColor = [0, 4]
			for values in nodesConnectedValues:
				if color in values:
					values.remove(color)
				if len(values) < lowestForColor[1]:
					lowestForColor = (color, len(values))
					allColors.append(lowestForColor)

		rightColor = [0, 0]
		for color in allColors:
			if color[1] > rightColor[1]:
				rightColor = color

		return rightColor[0]

	def forwardCheckingValue(self, color):
		pass