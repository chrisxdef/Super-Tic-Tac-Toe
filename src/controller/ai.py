import sys
from random import randint
from sets import Set

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
			if not winBoard(child.gameBoard):
				child.createTree()
		
	def h(self):
		return randint(0, 100)

	def minimax(self, mini):
		if len(self.children) == 0:
			return self.h()
		values = []
		for child in self.children:
			values.append(child.minimax(not mini))
		print values
		if mini:
			return min(values)
		return max(values)

winBoards = [Set([0,1,2]),Set([3,4,5]),Set([6,7,8]),Set([0,3,6]),Set([1,4,7]),Set([2,5,8]),Set([0,4,8]),Set([2,4,6])]

def winBoard(board):
	player1 = []
	player2 = []
	for i in range(len(board)):
		if board[i] == 1:
			player1.append(i)
		elif board[i] == 2:
			player2.append(i)
	player1 = Set(player1)
	player2 = Set(player2)
	for s in winBoards:
		if s.issubset(player1) or s.issubset(player2):
			return True
	return False

	
if __name__=="__main__":
	args = sys.argv
	# Make args useful here
	minimax()
