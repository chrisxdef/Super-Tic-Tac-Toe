import sys
sys.path.append("../view")
from tic-tac-toe import winBoard
from random import randint
from sets import Set

class Node():
	def __init__(self, player, gameBoard):
		self.children = []
		self.gameBoard = gameBoard
		# Player is indicating which player's turn it is for the current gameboard
		self.player = player

	def createTree(self, max_depth, depth=0):
		depth += 1
		# p represents the next player to move
		p = 2 if self.player == 1 else 1
		for index in range(len(self.gameBoard)):
			if self.gameBoard[index] == 0:
				tempBoard = self.gameBoard[:]
				tempBoard[index] = self.player
				self.children.append(Node(p, tempBoard))
		if depth == max_depth:
			return
		for child in self.children:
			if not winBoard(child.gameBoard):
				child.createTree(max_depth, depth)
		
	def h(self, ai):
		foo = winBoard(self.gameBoard)
		if not foo:
			return 0
		elif foo == ai:
			return 10
		return -10

	def minimax(self, mini, ai, origin=False):
		if len(self.children) == 0:
			return self.h(ai)
		values = []
		for child in self.children:
			values.append(child.minimax(not mini, ai))
		if origin:
			if mini:
				v = min(values)
			else:
				v = max(values)
			index = values.index(v)
			return self.children[index].gameBoard
		if mini:
			return min(values)
		return max(values)

	
if __name__=="__main__":
	args = sys.argv
	# Make args useful here
	minimax()
