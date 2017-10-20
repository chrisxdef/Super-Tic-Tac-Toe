import sys
from random import randint

class Node():
	def __init__(self, player, gameBoard):
		self.children = []
		self.gameBoard = gameBoard
		# Player is indicating which player's turn it is for the current gameboard
		self.player = player

	def createTree(self):
		# p represents the next player to move
		p = 2 if self.player == 1 else 1
		for index in range(len(self.gameBoard)):
			if self.gameBoard[index] == 0:
				tempBoard = self.gameBoard[:]
				tempBoard[index] = self.player
				self.children.append(Node(p, tempBoard))
		for child in self.children:
			child.createTree()
		
	def h(self):
		return randint(0, 100)

def minimax(node, depth, maximizingPlayer):
	if depth == 0 or node.children is None:
		return h(node)
	
	if maximizingPlayer:
		bestValue = -1 - sys.maxint
		for child in node.children:
			v = minimax(child, depth-1, FALSE)
			bestValue = v if (v > bestValue) else bestValue
		return bestValue
	else:
		bestValue = sys.maxint
		for child in node.children:
			v = minimax(child, depth - 1, TRUE)
			bestValue = v if (v < bestValue) else bestValue
		return bestValue


if __name__=="__main__":
	args = sys.argv
	# Make args useful here
	minimax()
