import sys
from game_utils import winBoard, fullBoard
sys.path.append("../controller")
from ai import Node

def game(gameBoard, human, ai):
	running = True
	turn = 1
	while(running):
		print gameBoard
		if turn == human:
			index = int(raw_input("Show me your moves!\t"))
			while(gameBoard[index] != 0):
				index = int(raw_input("Show me your moves!\t"))
			gameBoard[index] = human
			turn = ai
		else:
			print "Robot's Turn\n"
			node = Node(ai, gameBoard)
			node.createTree(3)
			gameBoard = node.minimax(False, ai, True)
			turn = human
		if winBoard(gameBoard) == human:
			print "GG! You Win!"
			running = False
		elif winBoard(gameBoard) == ai:
			print "GG! Robot Wins!"
			print gameBoard
			running = False
		elif fullBoard(gameBoard):
			print "GG! It's a draw!"
			running = False		

superBoard = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]

class GameState:
	def __init__(self, gameBoard=superBoard, human=1):
		self.gameBoard = gameBoard
		self.human = human
		self.ai = 2 if human == 1 else 1
		self.prompts = { self.human : "Show me your moves!", self.ai : "Robot's move."}
		self.turn = 1
		self.prompt = "Welcome to Super Tic-Tac-Toe!\n" + self.prompts[self.turn]
		self.gameOver = False

	def update(self, move):
		self.gameBoard = move
		self.gameOver = self.checkEnd()
		if(self.gameOver):
			self.prompt = "Game Over"
		else:			
			self.turn = 1 if self.turn == 2 else 1
			self.prompt = self.prompts[self.turn]
	
	def checkEnd(self):
		if(fullBoard(self.gameBoard)):
			return 3
		else:
			return winBoard(self.gameBoard)

if __name__ == "__main__":
	gameBoard = [0,0,0,0,0,0,0,0,0]
	human = 1
	ai = 2
	game(gameBoard, human, ai)	
