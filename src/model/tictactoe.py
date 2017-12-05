import sys
from game_utils import winBoard, fullBoard
sys.path.append("../controller")
from ai import Node

def game(gameBoard, index, humanTurn):
	if humanTurn == True:
                if(gameBoard[index] != 0):
                        return (gameBoard, humanTurn, False)
                else:
                        gameBoard[index] = 1
                        return (gameBoard, not humanTurn, False)
	else:
		node = Node(2, gameBoard)
		node.createTree(3)
		gameBoard = node.minimax(False, 2, True)
		return (gameBoard, not humanTurn, False) 
	if winBoard(gameBoard) == 1:
		return (gameBoard, not humanTurn, "GG! You Win!")
	elif winBoard(gameBoard) == 2:
		return (gameBoard, not humanTurn, "GG! Robot Wins!")
	elif fullBoard(gameBoard):
		return (gameBoard, not humanTurn, "GG! Its' a draw!")		

superBoard = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]

#class GameState:
#	def __init__(self, gameBoard=superBoard, human=1):
#		self.gameBoard = gameBoard
#		self.human = human
#		self.ai = 2 if human == 1 else 1
#		self.prompts = { self.human : "Show me your moves!", self.ai : "Robot's move."}
#		self.turn = 1
#		self.prompt = "Welcome to Super Tic-Tac-Toe!\n" + self.prompts[self.turn]
#		self.gameOver = False
#
#	def update(self, move=None):
#		if move == None:
#			n = SuperNode(self.turn, self.gameBoard)
#			n.createTree(4)
#			move = ai.minimax(False, self.ai)
#		self.gameBoard = move
#		self.gameOver = self.checkEnd()
#		if(self.gameOver):
#			self.prompt = "Game Over"
#		else:			
#			self.turn = 1 if self.turn == 2 else 1
#			self.prompt = self.prompts[self.turn]
#	
#	def checkEnd(self):
#		if(fullBoard(self.gameBoard)):
#			return 3
#		else:
#			return winBoard(self.gameBoard)	
