import sys
sys.path.append("../controller")
from ai import Node
sys.path.append("../model")
from game_utils import winBoard, fullBoard

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


if __name__ == "__main__":
	gameBoard = [0,0,0,0,0,0,0,0,0]
	human = 1
	ai = 2
	game(gameBoard, human, ai)	
