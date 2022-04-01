import AdjacencyMatrix


NumColors = 3


class CSP:

	def __init__(self, mostConstrained=False, mostConstraining=False,
				 forwardChecking=False, leastConstraining=False):
		self.mostConstrained = mostConstrained
		self.mostConstraining = mostConstraining
		self.forwardChecking = forwardChecking
		self.leastConstraining = leastConstraining
		self.adjacency = AdjacencyMatrix.AdjacencyMatrix(5, 25)
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
				self.adjacency.Alist[currentNode][0] = color
				nextNode = 0
				if self.mostConstrained:
					if self.mostConstraining:
						pass
					else:
						constrained = (1, 4)
						for i in range(len(self.adjacency.Alist)):
							if self.adjacency.Alist[i][0] == 0:
								colorsAvailable = [0, 1, 1, 1]
								for c in self.adjacency.Alist[i][2]:
									colorsAvailable[self.adjacency.Alist[c][0]] = 0
								count = 0
								for j in colorsAvailable:
									count += j
								if count < constrained[1]:
									constrained = (i, count)
						nextNode = constrained[0]

				elif self.mostConstraining:
					pass
				else:
					nextNode = currentNode + 1

				if self.backtracking(nextNode):
					return True
				self.adjacency.Alist[currentNode][0] = 0
		return False

	def solveCSP(self):
		start = 0
		new = True
		if self.mostConstraining:
			start = self.mostConstrainingVariable(new)
		result = self.backtracking(start)
		if not result:
			print("Solution does not exist")
			return 0
		else:
			print("***** Solution found after "+str(self.recursionCounter)+" recursions *****")
			return self.recursionCounter

	def mostConstrainingVariable(self):
		new = True
		if new:
			mostConnects = [0,0]
			for i in range(len(self.adjacency.Alist)):
				if len(self.adjacency.Alist[i][2]) > mostConnects[1]:
					mostConnects = [len(self.adjacency.Alist[i][2]), i]
			return mostConnects[1]
