import sys
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

winBoards = [Set([0,1,2]),Set([3,4,5]),Set([6,7,8]),Set([0,3,6]),Set([1,4,7]),Set([2,5,8]),Set([0,4,8]),Set([2,4,6])]

def fullBoard(board):
	for i in board:
		if i == 0:
			return False
	return True

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
		if s.issubset(player1):
			return 1
		elif s.issubset(player2):
			return 2
	return False

	
if __name__=="__main__":
	args = sys.argv
	# Make args useful here
	minimax()
