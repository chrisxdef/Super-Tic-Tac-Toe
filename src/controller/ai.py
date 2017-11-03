import sys
from copy import deepcopy
sys.path.append("../view")
from random import randint
sys.path.append("../model")
from game_utils import winBoard, fullBoard

class Node(object):
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

class SuperNode(Node):
	def __init__(self, player, gameBoard, gameIndex=-1):
		self.gameIndex = gameIndex
		super(SuperNode, self).__init__(player, gameBoard)

	def createTree(self, max_depth, depth=0):
		depth += 1
		# p represents the next player to move
		p = 2 if self.player == 1 else 1
		if self.gameIndex == -1 or type(self.gameBoard[self.gameIndex]) is int:
			indices = []
			for i in range(len(self.gameBoard)):
				if type(self.gameBoard[i]) is not int:
					indices.append(i)
		else:
			indices = [self.gameIndex]
		for index in indices:	
			for sub_index in range(len(self.gameBoard[index])):
				if self.gameBoard[index][sub_index] == 0:
					tempBoard = deepcopy(self.gameBoard)
					tempBoard[index][sub_index] = self.player
					win = winBoard(tempBoard[index])
					if win:
						tempBoard[index] = win
					self.children.append(SuperNode(p, tempBoard, gameIndex = sub_index))
		if depth == max_depth:
			return
		for child in self.children:
			if not winBoard(child.gameBoard):
				child.createTree(max_depth, depth)
		

	def h(self, ai):
		pass	
